import requests
from typing import Optional, List


def get_cards(name: Optional[str] = None, supertype: Optional[str] = None, types: Optional[List[str]] = None, hp: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve all cards, or filter them by name, supertype, types, and hp.
    
    Parameters:
    name [Optional]: string [Description: The name of the card to filter by.]
    supertype [Optional]: string [Description: The supertype of the card, such as Pokémon, Energy, or Trainer.]
    types [Optional]: list of strings [Description: The energy types for a card, such as Fire, Water, Grass, etc.]
    hp [Optional]: string [Description: The hit points of the card to filter by.]
    """
    url = "https://api.pokemontcg.io/v2/cards"
    params = {
        'name': name,
        'supertype': supertype,
        'types': types,
        'hp': hp
    }
    
    response = requests.get(url, params={key: value for key, value in params.items() if value is not None})
    
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_sets(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a list of all available sets in the Pokémon TCG.
    """
    url = "https://api.pokemontcg.io/v2/sets"
    
    response = requests.get(url)
    
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_card_by_id(card_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a specific card by its unique ID.
    
    Parameters:
    card_id [Required]: string [Description: The unique identifier for the specific card.]
    """
    url = f"https://api.pokemontcg.io/v2/cards/{card_id}"

    response = requests.get(url)
    
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}