import argparse
import json
import os
import litellm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default="openai/neulab/gpt-4o-2024-05-13", help='Model name')
    parser.add_argument('--openai_key', type=str, required=True, help='OpenAI API key')
    parser.add_argument('--input_query_file', type=str, required=True, help='Input query file')
    parser.add_argument('--output_answer_file', type=str, required=True, help='Output answer file')
    parser.add_argument('--tool_root_dir', type=str, required=True, help='Directory with tool definitions')
    args = parser.parse_args()

    # Read input queries
    with open(args.input_query_file, 'r') as f:
        queries = json.load(f)

    results = []

    for query_data in queries:
        query_id = query_data.get('query_id', None)

        # Process the query
        answer = process_query(query_data, args)

        results.append({
            'query_id': query_id,
            'query': query_data['query'],
            'answer': answer
        })

    # Write results to output file
    with open(args.output_answer_file, 'w') as f:
        json.dump(results, f, indent=2)


def process_query(query_data, args):
    query_text = query_data['query']
    # Load functions
    functions = load_functions(args.tool_root_dir, query_data)

    # Prepare messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant that can use tools to help the user."},
        {"role": "user", "content": query_text}
    ]

    assistant_reply = None
    for _ in range(5):  # Limit the number of steps
        # Call the model
        response = litellm.completion(
            api_key=args.openai_key,
            base_url="https://cmu.litellm.ai",
            model=args.model,
            messages=messages,
            functions=functions
        )

        # Extract the assistant's reply
        assistant_message = response['choices'][0]['message']

        messages.append(assistant_message)

        if 'function_call' in assistant_message:
            # Assistant is calling a function
            function_name = assistant_message['function_call']['name']
            function_args_str = assistant_message['function_call']['arguments']
            try:
                function_args = json.loads(function_args_str)
            except json.JSONDecodeError:
                function_args = {}

            # Execute the function
            function_response = execute_function(function_name, function_args, args.tool_root_dir, query_data)

            # Add the function response to messages
            messages.append({
                "role": "function",
                "name": function_name,
                "content": function_response
            })
        else:
            # Assistant provided the final answer
            assistant_reply = assistant_message['content']
            break

    return assistant_reply

def load_functions(tool_root_dir, query_data):
    import os
    import json
    functions = []

    # Only load functions specified in the query_data
    for api in query_data.get('api_list', []):
        category_name = api['category_name']
        tool_name = api['tool_name']
        api_name = api['api_name']
        tool_json_path = os.path.join(tool_root_dir, category_name, tool_name + '.json')
        
        if not os.path.exists(tool_json_path):
            continue

        with open(tool_json_path, 'r') as f:
            tool_data = json.load(f)

        # Find the specific API
        api_data = None
        for api_item in tool_data.get('api_list', []):
            if api_item['name'] == api_name:
                api_data = api_item
                break

        if api_data:
            # Convert API to OpenAI function format
            function = api_to_openai_function(api_data, tool_name)
            functions.append(function)

    return functions

def api_to_openai_function(api, tool_name):
    function = {
        "name": api['name'],
        "description": api.get('description', ''),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }

    # Handle required parameters
    required_params = api.get('required_parameters', [])
    for param in required_params:
        param_name = param['name']
        param_type = map_param_type(param['type'])
        param_desc = param.get('description', '')
        function['parameters']['properties'][param_name] = {
            "type": param_type,
            "description": param_desc
        }
        function['parameters']['required'].append(param_name)

    # Handle optional parameters
    optional_params = api.get('optional_parameters', [])
    for param in optional_params:
        param_name = param['name']
        param_type = map_param_type(param['type'])
        param_desc = param.get('description', '')
        function['parameters']['properties'][param_name] = {
            "type": param_type,
            "description": param_desc
        }
        # Optional parameters are not added to 'required'

    return function

def map_param_type(param_type):
    type_map = {
        "NUMBER": "number",
        "INTEGER": "integer",
        "STRING": "string",
        "BOOLEAN": "boolean",
        "LIST": "array",
        "OBJECT": "object"
    }
    return type_map.get(param_type.upper(), "string")

def execute_function(function_name, function_args, tool_root_dir, query_data):
    # function_name is the name of the function to execute (api_name)
    # function_args are the arguments for the function
    # query_data contains the 'api_list' with 'category_name' and 'tool_name'
    
    # Find the corresponding API entry in query_data
    api_entry = None
    for api in query_data.get('api_list', []):
        if api['api_name'] == function_name:
            api_entry = api
            break
    
    if not api_entry:
        return f"API '{function_name}' not found in query data."
    
    category_name = api_entry['category_name']
    tool_name = api_entry['tool_name']
    
    # Construct the path to api.py
    api_py_path = os.path.join(tool_root_dir, category_name, tool_name, 'api.py')
    if not os.path.exists(api_py_path):
        return f"API file not found at {api_py_path}"
    
    # Import the module from api.py
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(f"{category_name}.{tool_name}.api", api_py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        return f"Error loading module: {e}"
    
    # Get the function from the module
    func = getattr(module, function_name, None)
    if not func:
        return f"Function '{function_name}' not found in module."
    
    # Execute the function with provided arguments
    try:
        result = func(**function_args)
        # If the result is not serializable, convert it to string
        if not isinstance(result, (str, int, float, dict, list)):
            result = str(result)
        return json.dumps(result)
    except Exception as e:
        return f"Error executing function '{function_name}': {e}"

if __name__ == '__main__':
    main()
