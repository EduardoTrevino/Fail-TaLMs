import requests
from typing import Optional, List

def get_quote(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[str]:
    """
    Fetches a single random Ron Swanson quote.
    """
    url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_quotes(count: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[str]:
    """
    Fetches a specified number of random Ron Swanson quotes.
    
    Parameters:
    - count: Integer specifying the number of quotes to return.
    """
    url = f"https://ron-swanson-quotes.herokuapp.com/v2/quotes/{count}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_quotes(term: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[str]:
    """
    Searches for Ron Swanson quotes that match a given term.
    
    Parameters:
    - term: String with the term to search for in the quotes.
    """
    url = f"https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/{term}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}