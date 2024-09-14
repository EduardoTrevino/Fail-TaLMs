import requests
from typing import Optional

def generate_v1(count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate Version-1 UUIDs
    """
    url = f"https://www.uuidtools.com/api/generate/v1"
    if count:
        url += f"/count/{count}"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def generate_v3(namespace: str, name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate Version-3 UUIDs
    """
    url = f"https://www.uuidtools.com/api/generate/v3/namespace/{namespace}/name/{name}"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def decode(uuid: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Decode a UUID to get its details
    """
    url = f"https://www.uuidtools.com/api/decode/{uuid}"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
