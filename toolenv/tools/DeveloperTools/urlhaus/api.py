import requests
from typing import Optional

def recent_urls(limit: Optional[int] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of recent malware URLs added to URLhaus.
    """
    url = "https://urlhaus-api.abuse.ch/v1/urls/recent/"
    if limit:
        url = f"https://urlhaus-api.abuse.ch/v1/urls/recent/limit/{limit}/"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def host_info(host: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific host (IP address, hostname, or domain name) related to malware activity.
    """
    url = "https://urlhaus-api.abuse.ch/v1/host/"
    payload = {"host": host}

    response = requests.post(url, data=payload)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def payload_info(sha256_hash: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific payload (malware sample) based on its SHA256 hash.
    """
    url = "https://urlhaus-api.abuse.ch/v1/payload/"
    payload = {"sha256_hash": sha256_hash}

    response = requests.post(url, data=payload)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
