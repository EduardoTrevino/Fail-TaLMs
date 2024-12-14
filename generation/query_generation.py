import os
import itertools
from openai import OpenAI
import regex as re

# Load the API key from the openaikey.txt file
with open("openaikey.txt", "r") as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)

seed_api_question_example = '''
api_list-question example
```json
[
  {
    "api_list": [
        {
            "category_name": "Art",
            "tool_name": "metmuseum",
            "api_name": "search_objects",
            "api_description": "Search for objects in the Met's collection",
            "required_parameters": [
                {
                    "name": "q",
                    "type": "STRING",
                    "description": "Search term",
                    "default": "Impressionist paintings"
                }
            ],
            "optional_parameters": [
                {
                    "name": "departmentId",
                    "type": "INTEGER",
                    "description": "ID of the department",
                    "default": "11"
                }
            ],
            "method": "GET",
            "template_response": {
                "total": "int",
                "objectIDs": ["int"]
            }
        },
      {
            "category_name": "Art",
            "tool_name": "artchicago",
            "api_name": "artworks_search",
            "api_description": "Search artworks in the Art Institute of Chicago data in the aggregator. Artworks in the groups of essentials are boosted so they'll show up higher in results.",
            "required_parameters": [
                {
                    "name": "q",
                    "type": "STRING",
                    "description": "Your search query.",
                    "default": "monet"
                }
            ],
            "optional_parameters": [
                {
                    "name": "size",
                    "type": "INTEGER",
                    "description": "Number of results to return. Pagination via Elasticsearch conventions.",
                    "default": "10"
                },
                {
                    "name": "sort",
                    "type": "STRING",
                    "description": "Used in conjunction with query to sort results.",
                    "default": ""
                }
            ],
            "method": "GET",
            "template_response": {
                "pagination": {
                    "total": "int",
                    "limit": "int",
                    "offset": "int",
                    "total_pages": "int",
                    "current_page": "int"
                },
                "data": [
                    {
                        "id": "int",
                        "title": "str",
                        "artist_display": "str",
                        "place_of_origin": "str",
                        "date_display": "str",
                        "medium_display": "str",
                        "dimensions": "str",
                        "thumbnail": {
                            "alt_text": "str",
                            "width": "int",
                            "height": "int",
                            "iiif_url": "str"
                        }
                    }
                ]
            }
        }
    ],
    "query": "I want to find Impressionist paintings in the European Paintings department in the Met's collection. Additionally, can you find artworks related to Monet in the Art Institute of Chicago?",
    "relevant APIs": [],
    "query_id": 2
  }
]
```
'''

def read_file_content(file_path):
    """Read and return the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading {file_path}: {e}"

def generate_prompt(tool1, tool2, category_folder, category_path):
    """Generate the fstring prompt for two tools."""
    # Paths for Tool 1
    tool1_json_path = os.path.join(category_path, f"{tool1}.json")
    tool1_py_path = os.path.join(category_path, tool1, "api.py")
    tool1_test_py_path = os.path.join(category_path, tool1, "api_test.py")

    # Paths for Tool 2
    tool2_json_path = os.path.join(category_path, f"{tool2}.json")
    tool2_py_path = os.path.join(category_path, tool2, "api.py")
    tool2_test_py_path = os.path.join(category_path, tool2, "api_test.py")

    # Read the content of each file
    tool1_json_content = read_file_content(tool1_json_path)
    tool1_py_content = read_file_content(tool1_py_path)
    tool1_test_py_content = read_file_content(tool1_test_py_path)

    tool2_json_content = read_file_content(tool2_json_path)
    tool2_py_content = read_file_content(tool2_py_path)
    tool2_test_py_content = read_file_content(tool2_test_py_path)

    # Generate the prompt
    prompt = f'''
Below I have attached 2 Tools "{tool1}", and "{tool2}" which are python files that make requests to endpoints, from the "{category_folder}" category, and their corresponding meta data json files which provides additional information about the tools, as well as unittests ran on these endpoints, as some endpoints use parameters, so you can use these for your task. 
Your task is to create a api_list-question json file which asks questions a human would ask which requires the use of at least 1 API from each tool. 
Note the questions should be independent of any other API's. 
Note: for the api_list-question json file, be sure to have the name of the api function from the python files inside in the api_list, they should be the same name and format as the function provided in the python code. 

"{tool1}" tool
```python
{tool1_py_content}
```

"{tool1}" unittest
```python
{tool1_test_py_content}
```

"{tool1}" tool metadata
```json
{tool1_json_content}
```


"{tool2}" tool
```python
{tool2_py_content}
```

"{tool2}" unittest
```python
{tool2_test_py_content}
```

"{tool2}" tool metadata
```json
{tool2_json_content}
```
{seed_api_question_example}
'''
    return prompt

def save_response(category_folder, category_name, response, query_id):
    """Save the AI model response to the appropriate directory structure."""
    base_dir = os.path.join(category_name)
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Save raw output
    raw_output_path = os.path.join(base_dir, f"raw_output_{query_id}.txt")
    with open(raw_output_path, 'w', encoding='utf-8') as file:
        file.write(response)
    
    # Extract and save the JSON content from the AI response
    json_content = extract_json_from_response(response)
    if json_content:
        json_output_path = os.path.join(base_dir, f"query_{query_id}.json")
        with open(json_output_path, 'w', encoding='utf-8') as file:
            file.write(json_content)

def extract_json_from_response(response):
    """Extract JSON content from the response text enclosed within triple backticks."""
    start_idx = response.find("```json")
    end_idx = response.find("```", start_idx + 7)
    
    if start_idx != -1 and end_idx != -1:
        return response[start_idx + 7:end_idx].strip()
    return ""

def process_tool_combination(tool1, tool2, category_folder, category_path, query_id):
    """Process a pair of tools, generate the fstring prompt, and make the API call."""
    prompt = generate_prompt(tool1, tool2, category_folder, category_path)
    
    # Make the API call to OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "Your system prompt here"},
            {"role": "user", "content": prompt},
        ]
    )

    response = completion.choices[0].message.content
    
    # Save the response
    save_response(category_folder, category_folder, response, query_id)
    print(f"Saved query {query_id} for combination: {tool1} and {tool2}")
    print("-" * 100)

def process_category_combinations(category_path):
    """Process the category folder and handle all unique tool combinations."""
    category_folder = os.path.basename(category_path)
    tools = [item.replace('.json', '') for item in os.listdir(category_path) if item.endswith('.json')]
    
    query_id = 1
    for tool1, tool2 in itertools.combinations(tools, 2):
        process_tool_combination(tool1, tool2, category_folder, category_path, query_id)
        query_id += 1

# sample usage 
# category_path = 'fail-talms\tools\OpenData'
# process_category_combinations(category_path)