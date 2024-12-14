from openai import OpenAI
import regex as re
import os

# Load the API key from the openaikey.txt file
with open("openaikey.txt", "r") as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)

# Directory containing the API documentation files
documentation_dir = "fail-talms/api_docs/Art"

system_prompt = '''
You are a helpful assistant designed to generate Python code, test cases, and metadata JSON files based on API documentation. 
Your task is to create Python functions to interact with all relevant endpoints that a human might need based on the API's documentation. 
Ensure that the function names are properly formatted and include necessary parameters. 
Additionally, generate corresponding test cases to verify the API's functionality, and create a JSON file with metadata about the API.
'''

seed_api_example = '''
```python
import requests
from typing import Optional, List


def artworks(limit: Optional[int] = 2, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: A list of all artworks sorted by last updated date in descending order.
Parameters:
 limit [Optional]: integer [Description: ...]
page [Optional]: integer [Description: ...]
    """
    url = "https://api.artic.edu/api/v1/artworks"
    params = {
        'limit': limit,
        'page': page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def artworks_search(q: str, size: Optional[int] = 10, sort: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
  Endpoint description: Search artworks data in the aggregator. Artworks in the groups of essentials are boosted so they'll show up higher in results.
Parameters:
 q [Required]: string [Description: ...]
size [Optional]: integer [Description: ...]
sort [Optional]: sting [Description: ...]
    """
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {
        'q': q,
        'size': size
    }
    if sort:
        params['sort'] = sort

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def agents(limit: Optional[int] = 2, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: A list of all agents sorted by last updated date in descending order.
Parameters:
 limit [Optional]:  integer [Description: ...]
page [Optional]: integer [Description: ...]
    """
    url = "https://api.artic.edu/api/v1/agents"
    params = {
        'limit': limit,
        'page': page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}
```
'''
seed_json_example = '''
```json
{
    "tool_name": "artchicago",
    "tool_description": "API to access a wealth of data about the Art Institute of Chicago's collection, including artworks, artists, exhibitions, and more.",
    "title": "Art Institute of Chicago API",
    "pricing": "FREE",
    "score": {
        "avgServiceLevel": 95,
        "avgLatency": 150,
        "avgSuccessRate": 98,
        "popularityScore": 9.5,
        "__typename": "Score"
    },
    "home_url": "https://api.artic.edu/docs/",
    "host": "api.artic.edu",
    "api_list": [
        {
            "name": "artworks",
            "url": "https://api.artic.edu/api/v1/artworks",
            "description": "A list of all artworks sorted by last updated date in descending order.",
            "method": "GET",
            "required_parameters": [],
            "optional_parameters": [
                {
                    "name": "limit",
                    "type": "INTEGER",
                    "description": "The number of resources to return per page.",
                    "default": "2"
                },
                {
                    "name": "page",
                    "type": "INTEGER",
                    "description": "The page of resources to retrieve.",
                    "default": "1"
                }
            ],
            "code": "import requests\n\nurl = 'https://api.artic.edu/api/v1/artworks'\nparams = {'limit': limit, 'page': page}\nresponse = requests.get(url, params=params)\nprint(response.json())",
            "statuscode": 200,
            "body": {
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
            },
            "headers": {},
            "schema": {
                "type": "object",
                "properties": {
                    "pagination": {
                        "type": "object"
                    },
                    "data": {
                        "type": "array"
                    }
                }
            }
        },
        {
            "name": "artworks_search",
            "url": "https://api.artic.edu/api/v1/artworks/search",
            "description": "Search artworks data in the aggregator. Artworks in the groups of essentials are boosted so they'll show up higher in results.",
            "method": "GET",
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
            "code": "import requests\n\nurl = 'https://api.artic.edu/api/v1/artworks/search'\nparams = {'q': q, 'size': size, 'sort': sort}\nresponse = requests.get(url, params=params)\nprint(response.json())",
            "statuscode": 200,
            "body": {
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
            },
            "headers": {},
            "schema": {
                "type": "object",
                "properties": {
                    "pagination": {
                        "type": "object"
                    },
                    "data": {
                        "type": "array"
                    }
                }
            }
        },
        {
            "name": "agents",
            "url": "https://api.artic.edu/api/v1/agents",
            "description": "A list of all agents sorted by last updated date in descending order.",
            "method": "GET",
            "required_parameters": [],
            "optional_parameters": [
                {
                    "name": "limit",
                    "type": "INTEGER",
                    "description": "The number of resources to return per page.",
                    "default": "2"
                },
                {
                    "name": "page",
                    "type": "INTEGER",
                    "description": "The page of resources to retrieve.",
                    "default": "1"
                }
            ],
            "code": "import requests\n\nurl = 'https://api.artic.edu/api/v1/agents'\nparams = {'limit': limit, 'page': page}\nresponse = requests.get(url, params=params)\nprint(response.json())",
            "statuscode": 200,
            "body": {
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
                        "description": "str",
                        "birth_date": "int",
                        "death_date": "int"
                    }
                ]
            },
            "headers": {},
            "schema": {
                "type": "object",
                "properties": {
                    "pagination": {
                        "type": "object"
                    },
                    "data": {
                        "type": "array"
                    }
                }
            }
        }
    ]
}
```
'''

# Check if the directory exists
if not os.path.exists(documentation_dir):
    print(f"Error: The directory '{documentation_dir}' does not exist.")
else:
    # Iterate over all .txt files in the specified directory
    for filename in os.listdir(documentation_dir):
        if filename.endswith(".txt"):
            api_name = os.path.splitext(filename)[0]  # Extract the API name from the filename
            documentation_path = os.path.join(documentation_dir, filename)

            # Read the documentation from the file
            with open(documentation_path, "r") as file:
                documentation_content = file.read()
            # print(documentation_content)
            # print(api_name)

            # Construct the prompt using an f-string
            prompt = f''' 
            The following is documentation for an API called "{api_name}". Your task is to create a Python file "api.py" to make requests to all the relevant endpoints that a human need the functionality for based on the API's documentation provided. 
            Note: the endpoint function names should be lowercased and never start with a number, include the "toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'" as a parameter but do not include it anywhere else (Note this key is public so there is no need to worry). 
            Please ensure there are defaults in place (especially IDs or resource tags, etc. that are specific to the endpoint). 
            Additionally, ensure you create a Test Cases separately to verify the API's endpoints work "api_test.py". 
            Finally, create a metadata JSON file that provides metadata about the API and all of its available endpoints "{api_name}.json".
            Here is an example API file for a tool named artchicago: {seed_api_example}
            Here is an example corresponding JSON file. Note how the names of the APIs in the `api_list` match the function names in the Python code calling the endpoints: {seed_json_example}
            Now, please do this for the tool named "{api_name}", Here is the documentation for it (Quick side note I am using
            code_blocks = re.findall(r'###.*?```(python|json)(.*?)```', response, re.DOTALL) regex to capture your output generation so be sure to bold the titles, ie. ### api.py then ```python or ```json before the codeblock as normal):
            """{documentation_content}"""
            '''
            # Make the API call to OpenAI
            completion = client.chat.completions.create(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ]
            )

            response = completion.choices[0].message.content
            # Save the raw output
            category_dir = os.path.basename(os.path.normpath(documentation_dir))  # Extracts "Health" from the path
            output_dir = os.path.join(category_dir, api_name)
            os.makedirs(output_dir, exist_ok=True)

            with open(os.path.join(output_dir, "raw_output.txt"), "w") as raw_output_file:
                raw_output_file.write(response)

            # Find all code blocks with their associated language
            code_blocks = re.findall(r'###.*?```(python|json)(.*?)```', response, re.DOTALL)

            # Initialize variables to store extracted code
            api_code = None
            test_code = None
            json_metadata = None

            # Loop through the matched code blocks to assign them to the correct variables
            for block in code_blocks:
                language, code = block
                if language == 'python':
                    if api_code is None:
                        api_code = code.strip()  # First Python block is assumed to be the API code
                    elif test_code is None:
                        test_code = code.strip()  # Second Python block is assumed to be the test code
                elif language == 'json' and json_metadata is None:
                    json_metadata = code.strip()  # JSON block is the metadata

            # Save the Python API code
            if api_code:
                with open(os.path.join(output_dir, "api.py"), "w") as api_file:
                    api_file.write(api_code)

            # Save the test code
            if test_code:
                with open(os.path.join(output_dir, "api_test.py"), "w") as test_file:
                    test_file.write(test_code)

            # Save the JSON metadata
            if json_metadata:
                with open(os.path.join(category_dir, f"{api_name}.json"), "w") as json_file:
                    json_file.write(json_metadata)

            # Run the test file
            print(f"Running tests for API '{api_name}'...")
            os.system(f"python3 {os.path.join(output_dir, 'api_test.py')}")
            print(f"Tests completed for API '{api_name}'")
            print("\n" + "="*50 + "\n")