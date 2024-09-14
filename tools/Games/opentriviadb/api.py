import requests
from typing import Optional

def get_random_joke(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches a random joke
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_joke_types(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves the types of jokes available
    """
    url = "https://official-joke-api.appspot.com/types"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ten_random_jokes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches ten random jokes
    """
    url = "https://official-joke-api.appspot.com/random_ten"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_random_jokes(number: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches a specified number of random jokes
    """
    url = f"https://official-joke-api.appspot.com/jokes/random/{number}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_jokes_by_type(joke_type: str, quantity: Optional[str] = 'random', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches jokes by type with specified quantity, either 'random' or 'ten'
    """
    url = f"https://official-joke-api.appspot.com/jokes/{joke_type}/{quantity}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_joke_by_id(joke_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch a joke by its ID
    """
    url = f"https://official-joke-api.appspot.com/jokes/{joke_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}