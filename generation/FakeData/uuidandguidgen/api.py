import requests
from typing import Optional

# Public API Key required for any request call
def generate_v1_uuid(count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate version-1 UUIDs. Max count is 100.
    """
    url = f"https://www.uuidtools.com/api/generate/v1/count/{count}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def generate_v3_uuid(namespace: str, name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate a version-3 UUID based on a namespace and name.
    """
    url = f"https://www.uuidtools.com/api/generate/v3/namespace/{namespace}/name/{name}"
    response = requests.get(url)
    try:
        result = response.json()
        if isinstance(result, list):  # If it's a list, return the first item
            return result[0]
        return result
    except Exception as e:
        return {"error": str(e), "response": response.text}

def generate_v4_uuid(count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate version-4 UUIDs. Max count is 100.
    """
    url = f"https://www.uuidtools.com/api/generate/v4/count/{count}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def generate_v5_uuid(namespace: str, name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate a version-5 UUID based on a namespace and name.
    """
    url = f"https://www.uuidtools.com/api/generate/v5/namespace/{namespace}/name/{name}"
    response = requests.get(url)
    try:
        result = response.json()
        if isinstance(result, list):  # If it's a list, return the first item
            return result[0]
        return result
    except Exception as e:
        return {"error": str(e), "response": response.text}

def generate_timestamp_first_uuid(count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate timestamp-first UUIDs. Max count is 100.
    """
    url = f"https://www.uuidtools.com/api/generate/timestamp-first/count/{count}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def decode_uuid(uuid: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Decode a UUID to find its version and variant.
    """
    url = f"https://www.uuidtools.com/api/decode/{uuid}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}