import requests
from typing import Optional

def get_card(card_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a single card by its ID.
    """
    url = f"https://api.tcgdex.net/v2/en/cards/{card_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_cards(name: Optional[str] = None, sort_field: Optional[str] = None, sort_order: Optional[str] = 'ASC', 
                 page: Optional[int] = 1, items_per_page: Optional[int] = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for cards based on various filters and sorting options.
    """
    url = "https://api.tcgdex.net/v2/en/cards"
    params = {
        'name': name,
        'sort:field': sort_field,
        'sort:order': sort_order,
        'pagination:page': page,
        'pagination:itemsPerPage': items_per_page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_set(set_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific set by its ID.
    """
    url = f"https://api.tcgdex.net/v2/en/sets/{set_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_sets(sort_field: Optional[str] = None, sort_order: Optional[str] = 'ASC', 
                page: Optional[int] = 1, items_per_page: Optional[int] = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for sets and apply sorting and pagination.
    """
    url = "https://api.tcgdex.net/v2/en/sets"
    params = {
        'sort:field': sort_field,
        'sort:order': sort_order,
        'pagination:page': page,
        'pagination:itemsPerPage': items_per_page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_series(series_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a single series by ID.
    """
    url = f"https://api.tcgdex.net/v2/en/series/{series_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_series(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for series.
    """
    url = "https://api.tcgdex.net/v2/en/series"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_categories(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List different card categories.
    """
    url = "https://api.tcgdex.net/v2/en/categories"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_illustrators(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List different card illustrators.
    """
    url = "https://api.tcgdex.net/v2/en/illustrators"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_rarities(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List different card rarities.
    """
    url = "https://api.tcgdex.net/v2/en/rarities"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_retreats(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List different Pokémon retreat costs.
    """
    url = "https://api.tcgdex.net/v2/en/retreats"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_types(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List different Pokémon types.
    """
    url = "https://api.tcgdex.net/v2/en/types"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}