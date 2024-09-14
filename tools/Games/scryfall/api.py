import requests
from typing import Optional

BASE_URL = "https://api.scryfall.com"

def card_search(q: str, unique: Optional[str] = "cards", order: Optional[str] = "name", dir: Optional[str] = "auto", include_extras: bool = False, page: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search Magic cards using a fulltext search string.
    
    Parameters:
        q (str): The fulltext search query.
        unique (Optional[str]): Strategy for omitting similar cards. Default is "cards".
        order (Optional[str]): The method to sort returned cards. Default is "name".
        dir (Optional[str]): The direction to sort cards. Default is "auto".
        include_extras (bool): If true, includes extra cards such as tokens. Default is False.
        page (int): The page number to return. Default is 1.
    """
    url = f"{BASE_URL}/cards/search"
    params = {
        "q": q,
        "unique": unique,
        "order": order,
        "dir": dir,
        "include_extras": str(include_extras).lower(),
        "page": page
    }
    headers = {
        "User-Agent": "ScryfallExampleApp/1.0",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def card_named_exact(exact: str, set: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve exact card details based on card name.
    
    Parameters:
        exact (str): The exact card name to search for.
        set (Optional[str]): A set code to limit the search to one set. Default is None.
    """
    url = f"{BASE_URL}/cards/named"
    params = {
        "exact": exact
    }
    if set:
        params["set"] = set
    headers = {
        "User-Agent": "ScryfallExampleApp/1.0",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def card_named_fuzzy(fuzzy: str, set: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve card details based on a fuzzy name search.
    
    Parameters:
        fuzzy (str): A fuzzy card name to search for.
        set (Optional[str]): A set code to limit the search to one set. Default is None.
    """
    url = f"{BASE_URL}/cards/named"
    params = {
        "fuzzy": fuzzy
    }
    if set:
        params["set"] = set
    headers = {
        "User-Agent": "ScryfallExampleApp/1.0",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def cards_autocomplete(q: str, include_extras: bool = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Autocomplete card names.
    
    Parameters:
        q (str): The string to autocomplete.
        include_extras (bool): If true, includes extra cards such as tokens. Default is False.
    """
    url = f"{BASE_URL}/cards/autocomplete"
    params = {
        "q": q,
        "include_extras": str(include_extras).lower()
    }
    headers = {
        "User-Agent": "ScryfallExampleApp/1.0",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def card_random(q: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a random card.
    
    Parameters:
        q (Optional[str]): An optional fulltext search query to filter the pool of random cards. Default is None.
    """
    url = f"{BASE_URL}/cards/random"
    params = {}
    if q:
        params["q"] = q
    headers = {
        "User-Agent": "ScryfallExampleApp/1.0",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()