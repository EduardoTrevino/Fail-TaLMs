import requests
from typing import Optional, List

BASE_URL = "https://api.magicthegathering.io/v1"

def get_all_cards(page: Optional[int] = 1, page_size: Optional[int] = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **filters):
    """
    Get all cards with optional filtering.

    Parameters:
    - page: The page number to retrieve.
    - page_size: The number of cards to retrieve per page.
    - filters: Additional query parameters to filter cards.

    Returns:
    A JSON response containing cards.
    """
    url = f"{BASE_URL}/cards"
    params = {
        'page': page,
        'pageSize': page_size,
        **filters
    }
    response = requests.get(url, params=params)
    return response.json()

# def get_card_by_id(card_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Get a specific card by its ID.

#     Parameters:
#     - card_id: The unique id or multiverseid of the card.

#     Returns:
#     A JSON response containing the card details.
#     """
#     url = f"{BASE_URL}/cards/{card_id}"
#     response = requests.get(url)
#     return response.json()

def get_all_sets(name: Optional[str] = None, block: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all sets with optional filtering by name and block.

    Parameters:
    - name: Filter sets by set name.
    - block: Filter sets by block name.

    Returns:
    A JSON response containing sets.
    """
    url = f"{BASE_URL}/sets"
    params = {
        'name': name,
        'block': block
    }
    response = requests.get(url, params=params)
    return response.json()

def get_set_by_code(set_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a specific set by set code.

    Parameters:
    - set_code: The code of the set.

    Returns:
    A JSON response containing the set details.
    """
    url = f"{BASE_URL}/sets/{set_code}"
    response = requests.get(url)
    return response.json()

# def generate_booster_pack(set_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Generate a booster pack for a specific set.

#     Parameters:
#     - set_code: The code of the set to generate a booster pack for.

#     Returns:
#     A JSON response containing the booster pack details.
#     """
#     url = f"{BASE_URL}/sets/{set_code}/booster"
#     response = requests.get(url)
#     return response.json()

def get_all_types(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all card types.

    Returns:
    A JSON response containing all card types.
    """
    url = f"{BASE_URL}/types"
    response = requests.get(url)
    return response.json()

def get_all_subtypes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all card subtypes.

    Returns:
    A JSON response containing all card subtypes.
    """
    url = f"{BASE_URL}/subtypes"
    response = requests.get(url)
    return response.json()

def get_all_supertypes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all card supertypes.

    Returns:
    A JSON response containing all card supertypes.
    """
    url = f"{BASE_URL}/supertypes"
    response = requests.get(url)
    return response.json()

def get_all_formats(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all game formats.

    Returns:
    A JSON response containing all game formats.
    """
    url = f"{BASE_URL}/formats"
    response = requests.get(url)
    return response.json()

def get_cards_by_name(name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get cards by name.

    Parameters:
    - name: The name of the card to search for.

    Returns:
    A JSON response containing cards matching the name.
    """
    url = f"{BASE_URL}/cards"
    params = {'name': name}
    response = requests.get(url, params=params)
    return response.json()

def get_cards_by_foreign_name(name: str, language: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get cards by foreign name.

    Parameters:
    - name: The name of the card to search for.
    - language: The language to search the card name in.

    Returns:
    A JSON response containing cards matching the foreign name.
    """
    url = f"{BASE_URL}/cards"
    params = {'name': name, 'language': language}
    response = requests.get(url, params=params)
    return response.json()