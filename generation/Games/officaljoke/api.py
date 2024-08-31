import requests
from typing import Optional, List


def grab_random_joke(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Grab a random joke.
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def grab_random_joke_v2(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Grab a random joke (alternate endpoint).
    """
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_joke_types(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get available joke types.
    """
    url = "https://official-joke-api.appspot.com/types"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def grab_ten_random_jokes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Grab ten random jokes.
    """
    url = "https://official-joke-api.appspot.com/random_ten"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def grab_ten_random_jokes_v2(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Grab ten random jokes (alternate endpoint).
    """
    url = "https://official-joke-api.appspot.com/jokes/ten"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def grab_any_number_of_random_jokes(number: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Grab any number of random jokes.
    Parameters:
     number [Optional]: integer [Description: Number of jokes to fetch.]
    """
    url = f"https://official-joke-api.appspot.com/jokes/random/{number}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def grab_jokes_by_type(type: str, number: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Grab jokes by type.
    Parameters:
     type [Required]: string [Description: Type of jokes to fetch.]
     number [Optional]: integer [Description: Number of jokes to fetch (1 for 'random', others for 'ten').]
    """
    endpoint = 'random' if number == 1 else 'ten'
    url = f"https://official-joke-api.appspot.com/jokes/{type}/{endpoint}"
    response = requests.get(url)
    try:
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}", "response": response.text}
    except Exception as e:
        return {"error": str(e), "response": response.text}


def grab_joke_by_id(joke_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Grab joke by ID.
    Parameters:
     joke_id [Required]: integer [Description: ID of the joke to fetch.]
    """
    url = f"https://official-joke-api.appspot.com/jokes/{joke_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}