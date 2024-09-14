import requests
from typing import Optional


def get_random_advice(callback: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a random advice slip as a slip object.
    Parameters:
    callback [Optional]: string To define your own callback function name and return the JSON in a function wrapper (as JSONP).
    """
    url = "https://api.adviceslip.com/advice"
    params = {}
    if callback:
        params['callback'] = callback

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_advice_by_id(slip_id: int, callback: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    If an advice slip is found with the corresponding slip_id, a slip object is returned.
    Parameters:
    slip_id [Required]: integer The ID of the advice slip.
    callback [Optional]: string To define your own callback function name and return the JSON in a function wrapper (as JSONP).
    """
    url = f"https://api.adviceslip.com/advice/{slip_id}"
    params = {}
    if callback:
        params['callback'] = callback

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_advice(query: str, callback: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    If an advice slip is found, containing the corresponding search term in query, an array of slip objects is returned inside a search object.
    Parameters:
    query [Required]: string The search query term for advice slips.
    callback [Optional]: string To define your own callback function name and return the JSON in a function wrapper (as JSONP).
    """
    url = f"https://api.adviceslip.com/advice/search/{query}"
    params = {}
    if callback:
        params['callback'] = callback

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}