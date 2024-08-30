import requests
from typing import Optional

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

def get_version(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns date information about the CCDB service, the Unicode version/date the data came from, and PHP/MySQL versions.
    """
    url = "http://ccdb.hemiola.com/version"
    
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_fields(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of all field names in the database.
    """
    url = "http://ccdb.hemiola.com/fields"
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_all_characters(filter: Optional[str] = None, fields: Optional[str] = None, count: bool = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns all characters, optionally filtered, or the count of characters.
    """
    url = "http://ccdb.hemiola.com/characters"
    params = {}
    if filter:
        params['filter'] = filter
    if fields:
        params['fields'] = fields
    if count:
        params['count'] = ''
    
    response = requests.get(url, params=params, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_characters_by_radical(radical: int, strokes: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns characters that use a specific Kangxi radical, optionally filtered by additional strokes.
    """
    url = f"http://ccdb.hemiola.com/characters/radicals/{radical}"
    params = {}
    if strokes is not None:
        params['strokes'] = strokes
    
    response = requests.get(url, params=params, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_strokes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of valid total strokes and a count of characters with each number of total strokes.
    """
    url = "http://ccdb.hemiola.com/strokes"
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_sounds_mandarin(with_pitch: bool = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of Mandarin sounds, optionally with pitch.
    """
    url = "http://ccdb.hemiola.com/sounds/mandarin"
    if with_pitch:
        url += "/with-pitch"
    
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}