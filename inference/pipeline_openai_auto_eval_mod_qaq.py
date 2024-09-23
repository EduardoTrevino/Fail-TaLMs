import argparse
import json
import os
import litellm
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default="openai/neulab/gpt-4o-2024-05-13", help='Model name')
    parser.add_argument('--openai_key', type=str, required=True, help='OpenAI API key')
    parser.add_argument('--input_query_file', type=str, required=True, help='Input query file')
    parser.add_argument('--output_answer_file', type=str, required=True, help='Output answer file')
    parser.add_argument('--tool_root_dir', type=str, required=True, help='Directory with tool definitions')
    parser.add_argument('--use_human_interact', type=lambda x: (str(x).lower() == 'true'), default=False,
                        help='Whether to use human interaction')
    args = parser.parse_args()

    # Read input queries
    with open(args.input_query_file, 'r') as f:
        queries = json.load(f)

    # Check for already processed queries
    if os.path.exists(args.output_answer_file):
        with open(args.output_answer_file, 'r') as f:
            existing_results = json.load(f)
    else:
        existing_results = []

    processed_ids = {result['query_id'] for result in existing_results}

    results = existing_results

    for query_data in queries:
        query_id = query_data.get('query_id', None)
        if query_id in processed_ids:
            print(f"Skipping query_id {query_id} as it already exists.")
            continue

        print(f"\nProcessing query_id: {query_id}")

        # Process the query with tool and information awareness
        result = process_query(query_data, args)

        if result is not None:
            results.append(result)

        # Write results to output file
        with open(args.output_answer_file, 'w') as f:
            json.dump(results, f, indent=2)

def extract_yes_no_idk(response):
    """
    Attempts to extract 'yes', 'no', or 'idk' from the model's response.
    Returns the extracted response or None if not found.
    """
    # Normalize response by removing leading/trailing spaces and lowering case
    response = response.strip().lower()

    # Look for 'yes', 'no', or 'idk' at the start of the sentence
    match = re.match(r'^(yes|no|idk)', response)
    if match:
        return match.group(1)
    return None

def evaluate_tool_awareness(query, functions, args):
    prompt = f"Based on the available tools' functionality and your knowledge of the world, determine whether you have the necessary tools, knowledge, or a combination of both to answer the query. Start with 'Yes,' 'No,' or 'IDK,' followed by an explanation. 'Yes' means you have the knowledge, tools, or a combination of both, and you will attempt to answer. 'IDK' means you are uncertain but willing to try to answer. 'No' means you cannot answer the query with your knowledge, the available tools, or a combination of both, and you will skip it. Query: {query}, Your knowledge of the world, Available Tools: {functions}"
    system_prompt = """
Your task is to determine whether you can answer the user's query using:

1. Your existing knowledge (regardless of the tools).
2. The functionality of the available tools you have access to.
3. A combination of both.

When evaluating the query, consider whether:
The functionality of the tools can help you obtain the answer.
Your existing knowledge allows you to answer directly.
Or if a combination of a tool's functionality and your existing knowledge helps you obtain the answer.

Based on this evaluation:
Respond with 'Yes' if you can answer the query using your knowledge, the tools, or a combination of both.
Respond with 'IDK' if you are unsure but are willing to attempt an answer.
Respond with 'No' if you cannot answer the query at all, even with your knowledge and the tools available, or a combination of both. This means the query is completely unanswerable given the current resources, and you will skip attempting to answer the query.

Important: Always start your response with 'Yes,' 'No,' or 'IDK,' followed by a brief explanation of your reasoning. If you respond with 'No,' you will skip attempting to answer the query. If you respond with 'Yes' or 'IDK,' you are willing to try to answer.
"""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    response = litellm.completion(
        api_key=args.openai_key,
        base_url="https://cmu.litellm.ai",
        model=args.model,
        messages=messages
    )
    tool_aware = None
    retries = 0
    max_retries = 3

    while retries < max_retries:
        response = litellm.completion(
            api_key=args.openai_key,
            base_url="https://cmu.litellm.ai",
            model=args.model,
            messages=messages
        )
        tool_aware = extract_yes_no_idk(response.choices[0].message.content)
        tool_aware_reasoning = response.choices[0].message.content

        if tool_aware:
            return tool_aware, tool_aware_reasoning
        else:
            print(f"Retrying tool awareness evaluation. Attempt {retries + 1}/{max_retries}...")
            retries += 1

    # If retries exhausted, prompt user for manual extraction
    print("Unable to extract tool awareness response after 3 attempts.")
    print("Model's response: ", response.choices[0].message.content)
    tool_aware = input("Please provide a manual response for tool awareness (yes, no, idk): ").strip().lower()
    
    return tool_aware, tool_aware_reasoning

def evaluate_information_awareness(query, functions, args):
    prompt = f"Based on the user's query, your knowledge of the world, and the functionality of the available tools, determine if you can gather, infer, or have all the information needed to answer the request. Remember: Start with 'Yes,' 'No,' or 'IDK,' followed by an explanation. 'Yes' means you have enough information, you can infer it, or can obtain it using the tools, and you will attempt to answer. 'IDK' means you are uncertain but willing to try using your knowledge, tools, or a combination of both. 'No' means you cannot answer the query with your knowledge, the available tools, or a combination of both and you will skip it. Query: {query}, Your knowledge of the world, Available Tools and Their Functionalities: {functions}"
    system_prompt = """
Your task is to determine if you can gather, infer, or have all the information needed to answer the user's query using:
1. Your existing knowledge (regardless of the tools).
2. The functionality of the available tools you have access to.
3. A combination of both.

When evaluating the query, consider whether:
The query provides enough information for you to answer directly.
The available tools can help you obtain the necessary information or clarify the query.
Or if a combination of a tool's functionality and your existing knowledge helps you infer, gather, or have the necessary information you need to answer.

Based on this evaluation:
Respond with 'Yes' if you can gather, infer, or have all the information needed to answer the query using your knowledge, the tools, or both.
Respond with 'IDK' if you are unsure but are willing to attempt an answer.
Respond with 'No' if you cannot answer the query at all, even with your knowledge and the tools available. This means the query is completely unanswerable given the current resources.
Important: Always start your response with 'Yes,' 'No,' or 'IDK,' followed by a brief explanation of your reasoning. If you respond with 'No,' you will skip attempting to answer the query. If you respond with 'Yes' or 'IDK,' you are willing to try to answer.
"""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    response = litellm.completion(
            api_key=args.openai_key,
            base_url="https://cmu.litellm.ai",
            model=args.model,
            messages=messages
    )
    info_aware = None
    retries = 0
    max_retries = 3

    while retries < max_retries:
        response = litellm.completion(
            api_key=args.openai_key,
            base_url="https://cmu.litellm.ai",
            model=args.model,
            messages=messages
        )
        info_aware = extract_yes_no_idk(response.choices[0].message.content)
        info_aware_reasoning = response.choices[0].message.content

        if info_aware:
            return info_aware, info_aware_reasoning
        else:
            print(f"Retrying information awareness evaluation. Attempt {retries + 1}/{max_retries}...")
            retries += 1

    # If retries exhausted, prompt user for manual extraction
    print("Unable to extract information awareness response after 3 attempts.")
    print("Model's response: ", response.choices[0].message.content)
    info_aware = input("Please provide a manual response for information awareness (yes, no, idk): ").strip().lower()

    return info_aware, info_aware_reasoning

def calculate_validity(dataset_type, tool_response, info_response, pass_rate):
    """
    Calculates the tool and information awareness validity (ground truth labels on if the model appropriately decided to skip a question/risk answering a question) based on the dataset type,
    the model's responses, and the pass rate (ie it said idk/ was uncertain but got it correct! (Train an RL policy on this?)).
    """
    # Ground truth for each dataset type
    ground_truth = {
        'Original': {'tool_awareness': 'yes', 'info_awareness': 'yes'},
        'Replaceable': {'tool_awareness': ['yes', 'idk'], 'info_awareness': 'yes'},
        'Non-replaceable': {'tool_awareness': 'no', 'info_awareness': 'yes'},
        'Underspecified': {'tool_awareness': 'yes', 'info_awareness': 'no'},
        'No-tools': {'tool_awareness': ['no', 'idk'], 'info_awareness': 'yes'}
    }

    # Get the ground truth for the given dataset type
    expected_responses = ground_truth.get(dataset_type)

    # Initialize validity scores as None
    tool_validity = None
    info_validity = None

    # Calculate tool validity if tool_response is not None
    if tool_response is not None:
        if tool_response == 'idk':
            tool_validity = 1 if pass_rate == 1 else 0
        else:
            expected_tool_awareness = expected_responses['tool_awareness']
            if isinstance(expected_tool_awareness, list):
                tool_validity = 1 if tool_response in expected_tool_awareness else 0
            else:
                tool_validity = 1 if tool_response == expected_tool_awareness else 0

    # Calculate info validity if info_response is not None
    if info_response is not None:
        if info_response == 'idk':
            info_validity = 1 if pass_rate == 1 else 0
        else:
            expected_info_awareness = expected_responses['info_awareness']
            if info_response == expected_info_awareness:
                info_validity = 1
            else:
                info_validity = 0

    return tool_validity, info_validity

def get_dataset_type(filename):
    # Determine the dataset type based on filename convention
    if 'Original' in filename:
        return 'Original'
    elif 'Replaceable' in filename:
        return 'Replaceable'
    elif 'Non-replaceable' in filename:
        return 'Non-replaceable'
    elif 'Underspecified' in filename:
        return 'Underspecified'
    elif 'No-tools' in filename:
        return 'No-tools'
    else:
        raise ValueError(f"Unknown dataset type for filename: {filename}")
    
def get_evaluation_plan(dataset_type):
    plan = {
        'Original': {'tool_awareness': True, 'info_awareness': True, 'pass_rate': True},
        'Replaceable': {'tool_awareness': True, 'info_awareness': False, 'pass_rate': True},
        'Non-replaceable': {'tool_awareness': True, 'info_awareness': False, 'pass_rate': True},
        'Underspecified': {'tool_awareness': False, 'info_awareness': True, 'pass_rate': True},
        'No-tools': {'tool_awareness': False, 'info_awareness': False, 'pass_rate': True}
    }
    return plan.get(dataset_type, {'tool_awareness': True, 'info_awareness': True, 'pass_rate': True})

def process_query(query_data, args):
    query_text = query_data['query']
    query_id = query_data['query_id']
    dataset_type = get_dataset_type(args.input_query_file)
    print(f"\nProcessing query: {query_text}")

    # Load functions
    functions = load_functions(args.tool_root_dir, query_data, args.use_human_interact)
    print(f"Loaded {len(functions)} functions.")
    for function in functions:
        print(f"Function loaded: {function['name']}")
    
    function_call_log = []
    # Initialize a list to collect interaction data
    interaction_scores = []

    # Get evaluation plan
    evaluation_plan = get_evaluation_plan(dataset_type)

    # Initialize variables
    tool_awareness_annotation = None
    tool_awareness_reasoning = None
    info_awareness_annotation = None
    info_awareness_reasoning = None

    # Tool Awareness Evaluation
    if evaluation_plan['tool_awareness']:
        tool_awareness_annotation, tool_awareness_reasoning = evaluate_tool_awareness(query_text, functions, args)
        print(f"Tool Awareness Response: {tool_awareness_annotation}")

    # Information Awareness Evaluation
    if evaluation_plan['info_awareness']:
        info_awareness_annotation, info_awareness_reasoning = evaluate_information_awareness(query_text, functions, args)
        print(f"Information Awareness Response: {info_awareness_annotation}")

    # Decide whether to skip the query
    skip_query = False
    if evaluation_plan['tool_awareness'] and tool_awareness_annotation == "no":
        skip_query = True
    if evaluation_plan['info_awareness'] and info_awareness_annotation == "no":
        skip_query = True

    if skip_query:
        print(f"Skipping query {query_id} based on tool or information awareness.")
        pass_rate = None
        tool_validity, info_validity = calculate_validity (dataset_type, info_awareness_annotation, info_awareness_annotation, pass_rate)
        pass_rate = 1 if tool_validity == 1 and info_validity == 1 else 0
        result = {
            'query_id': query_id,
            'query': query_text,
            'skipped': True,
            'pass_rate': pass_rate
        }
        if evaluation_plan['tool_awareness']:
            result['tool_awareness'] = tool_awareness_reasoning
            result['tool_annotation'] = tool_awareness_annotation
            result['tool_aware_score'] = tool_validity
        if evaluation_plan['info_awareness']:
            result['info_awareness'] = info_awareness_reasoning
            result['info_annotation'] = info_awareness_annotation
            result['info_aware_score'] = info_validity
        return result
    # Proceed if the model thinks it has sufficient tools and information
    print(f"Proceeding with query {query_id}.")
    system_message = """
You are a helpful assistant that can use tools to help the user. The final answer should contain enough information to show to the user. 
Remember:
1.ALWAYS call \"Finish\" function at the end of the task. And the final answer should contain enough information to show to the user
"""

    # Prepare messages
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": query_text}
    ]

    assistant_reply = None
    max_steps = 5  # Increase the max steps if needed
    for step in range(max_steps):  # Limit the number of steps
        print(f"\n--- Step {step + 1} ---")
        print(messages)
        # Call the model
        if dataset_type == "No-tools":
            response = litellm.completion(
            api_key=args.openai_key,
            base_url="https://cmu.litellm.ai",
            model=args.model,
            messages=messages
        )
        else:
            response = litellm.completion(
                api_key=args.openai_key,
                base_url="https://cmu.litellm.ai",
                model=args.model,
                messages=messages,
                functions=functions
            )

        # Extract the assistant's reply
        assistant_message = response.choices[0].message

        # Convert assistant_message to dict format
        assistant_message_dict = {
            'role': assistant_message.role,
            'content': assistant_message.content,
        }

        if assistant_message.function_call is not None:
            assistant_message_dict['function_call'] = {
                'name': assistant_message.function_call.name,
                'arguments': assistant_message.function_call.arguments
            }

        messages.append(assistant_message_dict)

        if assistant_message.function_call is not None:
            # Assistant is calling a function
            function_name = assistant_message.function_call.name
            function_args_str = assistant_message.function_call.arguments
            print(f"Assistant is calling function '{function_name}' with arguments: {function_args_str}")

            try:
                function_args = json.loads(function_args_str)
            except json.JSONDecodeError as e:
                print(f"Error decoding function arguments: {e}")
                function_args = {}

            # If the assistant called the "Finish" function, extract the final answer and break
            if function_name == "Finish":
                assistant_reply = function_args.get('final_answer', '')
                print(f"Assistant final reply: {assistant_reply}")
                break


            # Execute the function
            function_response, interaction_data = execute_function(function_name, function_args, args.tool_root_dir, query_data)
            print(f"----\nFunction response: {function_response}")
            function_call_log.append(f"Called function '{function_name}' with response: {function_response}")

            # Add the function response to messages
            # messages.append({
            #     "role": "function",
            #     "name": function_name,
            #     "content": function_response
            # })
            messages.append({
                "role": "function",
                "name": "assistant",
                "content": f"{function_name}'s response is: {function_response}"
            })
            # If there is interaction data, collect it
            if interaction_data:
                interaction_scores.append(interaction_data)
        else:
            # Assistant provided a message without calling a function
            # Remind the assistant to call the "Finish" function
            # Assistant provided the final answer
            reminder_message = {
            "role": "system",
            "content": "Remember, you must ALWAYS call the \"Finish\" function at the end of your attempt. Please call the \"Finish\" function with your final answer."
        }
            messages.append(reminder_message)

        # Check if we have reached the max steps
        if step == max_steps - 1:
            # Assistant did not call the "Finish" function within the allowed steps
            print("Assistant did not call the 'Finish' function within the allowed steps.")
            assistant_reply = assistant_message.content or ''
            print(f"Assistant final reply: {assistant_reply}")
            break

    if assistant_reply is None:
        print("Assistant did not provide a final reply within the allowed steps.")

    # Concatenate the logged function calls and responses for evaluation context
    function_context = "\n".join(function_call_log)
    # Evaluate the pass rate using the assistant's reply and the user's query
    pass_rate = evaluate_pass_rate(assistant_reply, query_text, function_context, args)
    print("Pass score: ", pass_rate)
    tool_validity, info_validity = calculate_validity(dataset_type, tool_awareness_annotation, info_awareness_annotation, pass_rate)
    result = {
        'query_id': query_id,
        'query': query_text,
        'skipped': False,
        'pass_rate': pass_rate,
        'model_answer': assistant_reply
    }
    # Add interaction scores if any
    if interaction_scores:
        result['interaction_scores'] = interaction_scores

    if evaluation_plan['tool_awareness']:
        result['tool_awareness'] = tool_awareness_reasoning
        result['tool_annotation'] = tool_awareness_annotation
        result['tool_aware_score'] = tool_validity
    if evaluation_plan['info_awareness']:
        result['info_awareness'] = info_awareness_reasoning
        result['info_annotation'] = info_awareness_annotation
        result['info_aware_score'] = info_validity
    return result

def extract_correct_incorrect(response):
    """
    Attempts to extract 'pass' or 'fail' from the model's response.
    Returns 1 for pass, 0 for fail, or None if neither is found.
    """
    response = response.strip().lower()
    print("Response: ", response)
    match = re.match(r'^(pass|fail)', response)
    
    if match:
        if match.group(1) == 'pass':
            return 1
        elif match.group(1) == 'fail':
            return 0
    return None  # Return None if neither 'pass' nor 'fail' is found

def evaluate_pass_rate(assistant_reply, query_text, function_context, args):
    """
    Evaluates if the model's response to the user's query as a pass or fail attempt.
    Retries up to 3 times if the model's output is unclear, then falls back to manual input.
    """
    if function_context:
        api_responses_text = f"API's accessed and responses:\n{function_context}"
        answer_part = "assistant's answer, and attached API's accessed with their responses."
        system_part = "You will be given a user's instruction, assistant's answer, and the API's accessed along with their responses."
    else:
        api_responses_text = ""
        answer_part = "assistant's answer."
        system_part = "You will be given a user's instruction and assistant's answer."

    # Construct the prompt for the user
    prompt = (
        f"Below I have attached a user's instruction, {answer_part} "
        f"Did the assistant's answer complete the instruction given? Begin your response with either 'Pass' or 'Fail'.\n\n"
        f"Query: {query_text}\n Answer: {assistant_reply}\n\n"
        f"{api_responses_text}"
    )

    # Construct the system message
    system_message = (
        f"You are a grader. {system_part} Based on the answer given, "
        "determine if the instruction was completed or not. Always begin your response with either 'Pass' or 'Fail'."
    )

    # Messages to be sent to the grader system
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    max_attempts = 3
    max_retries = 3
    results = []  # Store results from 5 attempts

    for attempt in range(max_attempts):
        retries = 0
        pass_rate = None
        
        while retries < max_retries:
            response = litellm.completion(
                api_key=args.openai_key,
                base_url="https://cmu.litellm.ai",
                model="openai/neulab/gpt-4o-2024-05-13",
                messages=messages
            )
            
            pass_rate = extract_correct_incorrect(response.choices[0].message.content)

            if pass_rate is not None:
                results.append(pass_rate)
                break
            else:
                print(f"Retrying pass rate evaluation. Attempt {retries + 1}/{max_retries}...")
                retries += 1

        # If retries exhausted without valid response, log None
        if pass_rate is None:
            print(f"Failed to evaluate pass rate for attempt {attempt + 1}/{max_attempts}.")
            results.append(None)

    # Filter out None values and perform majority vote
    valid_results = [r for r in results if r is not None]

    if valid_results:
        # Perform majority vote if there are valid results
        count_passes = valid_results.count(1)
        count_fails = valid_results.count(0)

        # Return the majority if there's a clear winner, otherwise return None
        if count_passes > count_fails:
            return 1
        elif count_fails > count_passes:
            return 0
    else:
        # If all attempts failed, fall back to manual input
        print("Unable to extract pass rate response after 5 attempts.")
        print("Assistant's reply: \n", assistant_reply)
        print("Initial query: \n", query_text)
        pass_rate = int(input("Please manually evaluate the assistant's answer. Did it follow the instructions pass (1) or fail (0)?: ").strip())
        return pass_rate

def load_functions(tool_root_dir, query_data, use_human_interact=False):
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
            print(f"Tool JSON file not found at {tool_json_path}")
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
        else:
            print(f"API '{api_name}' not found in tool '{tool_name}'")

    # Conditionally add the human interact function
    if use_human_interact:
        # Append to query_data['api_list']
        query_data.setdefault('api_list', [])
        query_data['api_list'].append({
            'category_name': 'HumanInteract',
            'tool_name': 'humaninteract',
            'api_name': 'interact_with_human'
        })
        # Now load the 'interact_with_human' API as usual
        # Load the tool JSON
        human_interact_tool_path = os.path.join(tool_root_dir, 'HumanInteract', 'humaninteract.json')

        if os.path.exists(human_interact_tool_path):
            with open(human_interact_tool_path, 'r') as f:
                human_tool_data = json.load(f)

            # Find the 'interact_with_human' API
            api_data = None
            for api_item in human_tool_data.get('api_list', []):
                if api_item['name'] == 'interact_with_human':
                    api_data = api_item
                    break

            if api_data:
                function = api_to_openai_function(api_data, 'humaninteract')
                functions.append(function)
            else:
                print("API 'interact_with_human' not found in 'humaninteract.json'")
        else:
            print(f"Tool JSON file not found at {human_interact_tool_path}")

    # Add the finish function
    finish_func = {
        "name": "Finish",
        "description": "If you believe that you have obtained a result that can answer the task, please call this function to provide the final answer. Remember: you must ALWAYS call this function at the end of your attempt, and the only part that will be shown to the user is the final answer, so it should contain sufficient information.",
        "parameters": {
            "type": "object",
            "properties": {
                "final_answer": {
                    "type": "string",
                    "description": "The final answer you want to give the user."
                }
            },
            "required": ["final_answer"],
        }
    }
    functions.append(finish_func)

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
        param_schema = {
            "type": param_type,
            "description": param_desc
        }
        if param_type == "array":
            # Include 'items' in the schema
            param_schema["items"] = {"type": "string"}  # Assuming array of strings
        function['parameters']['properties'][param_name] = param_schema
        function['parameters']['required'].append(param_name)

    # Handle optional parameters
    optional_params = api.get('optional_parameters', [])
    for param in optional_params:
        param_name = param['name']
        param_type = map_param_type(param['type'])
        param_desc = param.get('description', '')
        param_schema = {
            "type": param_type,
            "description": param_desc
        }
        if param_type == "array":
            # Include 'items' in the schema
            param_schema["items"] = {"type": "string"}  # Assuming array of strings
        function['parameters']['properties'][param_name] = param_schema
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
    # Find the corresponding API entry in query_data
    api_entry = None
    for api in query_data.get('api_list', []):
        if api['api_name'] == function_name:
            api_entry = api
            break

    if not api_entry:
        print(f"API '{function_name}' not found in query data.")
        return f"API '{function_name}' not found in query data."

    category_name = api_entry['category_name']
    tool_name = api_entry['tool_name']

    # Construct the path to api.py
    api_py_path = os.path.join(tool_root_dir, category_name, tool_name, 'api.py')
    if not os.path.exists(api_py_path):
        print(f"API file not found at {api_py_path}")
        return f"API file not found at {api_py_path}"

    # Import the module from api.py
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(f"{category_name}.{tool_name}.api", api_py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"Error loading module: {e}")
        return f"Error loading module: {e}"

    # Get the function from the module
    func = getattr(module, function_name, None)
    if not func:
        print(f"Function '{function_name}' not found in module.")
        return f"Function '{function_name}' not found in module."

    # Execute the function with provided arguments
    try:
        print(f"Executing function '{function_name}' with arguments: {function_args}")
        if function_name == 'interact_with_human':
            # 'interact_with_human' returns a tuple
            function_response, interaction_data = func(**function_args)
        else:
            # Other functions return a single value
            function_response = func(**function_args)
            interaction_data = None

        print(f"Function '{function_name}' returned: {function_response}")
        # Ensure the function response is serializable
        if not isinstance(function_response, (str, int, float, dict, list)):
            function_response = str(function_response)
        return function_response, interaction_data
    
    except Exception as e:
        print(f"Error executing function '{function_name}': {e}")
        return f"Error executing function '{function_name}': {e}", None

if __name__ == '__main__':
    main()