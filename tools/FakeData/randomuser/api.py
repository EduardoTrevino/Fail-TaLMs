import requests
from typing import Optional, List


def get_random_user(results: Optional[int] = 1, seed: Optional[str] = None, gender: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a set of random users.
Parameters:
 results [Optional]: integer [Description: The number of users to return. Defaults to 1.]
 seed [Optional]: string [Description: Seed to get repeatable results. Defaults to None.]
 gender [Optional]: string [Description: Filter results by gender. Values can be 'male' or 'female'. Defaults to None.]
    """
    url = "https://randomuser.me/api/"
    params = {
        'results': results,
    }
    if seed:
        params['seed'] = seed
    if gender:
        params['gender'] = gender
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_random_user_in_format(format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a random user in a specified format.
Parameters:
 format [Optional]: string [Description: The format to return the data in. Values can be 'json', 'xml', 'csv', 'yaml'. Defaults to 'json'.]
    """
    url = f"https://randomuser.me/api/"
    params = {
        'format': format
    }
    response = requests.get(url, params=params)
    try:
        if format == 'json':
            return response.json()
        else:
            return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}