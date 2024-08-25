import requests
from typing import Optional, Dict, Any

API_BASE_URL = "https://www.amiiboapi.com/api"

def get_amiibos(name: Optional[str] = None, id: Optional[str] = None, head: Optional[str] = None, tail: Optional[str] = None, type: Optional[str] = None, game_series: Optional[str] = None, amiibo_series: Optional[str] = None, character: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches a list of amiibos or specific amiibo based on the filters provided.
    """
    url = f"{API_BASE_URL}/amiibo/"
    params = {
        'name': name,
        'id': id,
        'head': head,
        'tail': tail,
        'type': type,
        'gameseries': game_series,
        'amiiboSeries': amiibo_series,
        'character': character
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_amiibo_type(key: Optional[str] = None, name: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches amiibo types based on key or name.
    """
    url = f"{API_BASE_URL}/type"
    params = {
        'key': key,
        'name': name
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_game_series(key: Optional[str] = None, name: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches game series information based on key or name.
    """
    url = f"{API_BASE_URL}/gameseries"
    params = {
        'key': key,
        'name': name
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_amiibo_series(key: Optional[str] = None, name: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches amiibo series based on key or name.
    """
    url = f"{API_BASE_URL}/amiiboseries"
    params = {
        'key': key,
        'name': name
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_character(key: Optional[str] = None, name: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches character information based on key or name.
    """
    url = f"{API_BASE_URL}/character"
    params = {
        'key': key,
        'name': name
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_last_updated(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches the last updated timestamp of the amiibo database.
    """
    url = f"{API_BASE_URL}/lastupdated"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}