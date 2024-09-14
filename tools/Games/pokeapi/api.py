import requests
from typing import Optional


def get_berry(berry_id_or_name: str = 'cheri', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get information about a specific berry by ID or name.
    """
    url = f"https://pokeapi.co/api/v2/berry/{berry_id_or_name}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_berry_firmness(firmness_id_or_name: str = 'very-soft', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get information about a specified berry firmness by ID or name.
    """
    url = f"https://pokeapi.co/api/v2/berry-firmness/{firmness_id_or_name}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_berry_flavor(flavor_id_or_name: str = 'spicy', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get information about a specific berry flavor by ID or name.
    """
    url = f"https://pokeapi.co/api/v2/berry-flavor/{flavor_id_or_name}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_ability(ability_id_or_name: str = 'stench', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details about a specific Pokemon ability by ID or name.
    """
    url = f"https://pokeapi.co/api/v2/ability/{ability_id_or_name}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_pokemon(pokemon_id_or_name: str = 'clefairy', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details about a specific Pokemon by ID or name.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_type(type_id_or_name: str = 'ground', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details about a specific Pokemon type by ID or name.
    """
    url = f"https://pokeapi.co/api/v2/type/{type_id_or_name}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}