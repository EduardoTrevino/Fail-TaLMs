import requests
from typing import Optional, List

def get_all_resources(endpoint: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get list of all available resources for an endpoint.
    Parameters:
    endpoint [Required]: string - The endpoint to query for available resources.
    """
    url = f"https://www.dnd5eapi.co/api/{endpoint}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_ability_score(index: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get an ability score by index.
    Parameters:
    index [Required]: string - The index of the ability score to get.
    """
    url = f"https://www.dnd5eapi.co/api/ability-scores/{index}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_alignment(index: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get an alignment by index.
    Parameters:
    index [Required]: string - The index of the alignment to get.
    """
    url = f"https://www.dnd5eapi.co/api/alignments/{index}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_background(index: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a background by index.
    Parameters:
    index [Required]: string - The index of the background to get.
    """
    url = f"https://www.dnd5eapi.co/api/backgrounds/{index}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_class(index: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a class by index.
    Parameters:
    index [Required]: string - The index of the class to get.
    """
    url = f"https://www.dnd5eapi.co/api/classes/{index}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_condition(index: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a condition by index.
    Parameters:
    index [Required]: string - The index of the condition to get.
    """
    url = f"https://www.dnd5eapi.co/api/conditions/{index}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_damage_type(index: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a damage type by index.
    Parameters:
    index [Required]: string - The index of the damage type to get.
    """
    url = f"https://www.dnd5eapi.co/api/damage-types/{index}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_equipment(index: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get an equipment item by index.
    Parameters:
    index [Required]: string - The index of the equipment to get.
    """
    url = f"https://www.dnd5eapi.co/api/equipment/{index}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}