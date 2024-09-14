import requests
from typing import Optional, Dict

def get_latest_version(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve the latest version of Data Dragon.
    Returns information about the latest patch version.
    """
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_champion_data(version: str = "12.6.1", language: str = "en_US", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve champion data for a specified version and language.
    Parameters:
    - version: version of the data files
    - language: language code (e.g., "en_US")
    """
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_item_data(version: str = "12.6.1", language: str = "en_US", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve item data for a specified version and language.
    Parameters:
    - version: version of the data files
    - language: language code (e.g., "en_US")
    """
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/item.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_rune_data(version: str = "12.6.1", language: str = "en_US", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve rune data for a specified version and language.
    Parameters:
    - version: version of the data files
    - language: language code (e.g., "en_US")
    """
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/runesReforged.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_language_data(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve available languages for Data Dragon.
    """
    url = "https://ddragon.leagueoflegends.com/cdn/languages.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}