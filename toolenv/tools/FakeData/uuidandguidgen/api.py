import requests
import json

from typing import Optional, Dict, List


def generate_v1(count: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[str]:
    """
    Generate Version-1 UUIDs
    """
    url = f"https://www.uuidtools.com/api/generate/v1/count/{count}"
    
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key
    }
    
    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def generate_v3(namespace: str, name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> str:
    """
    Generate Version-3 UUIDs
    """
    url = f"https://www.uuidtools.com/api/generate/v3/namespace/{namespace}/name/{name}"
    
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key
    }
    
    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def decode(uuid: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Decode a UUID to get its details
    """
    url = f"https://www.uuidtools.com/api/decode/{uuid}"
    
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key
    }
    
    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
