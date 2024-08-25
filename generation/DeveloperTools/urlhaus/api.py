import requests
from typing import Optional, Union

def query_recent_urls(limit: Optional[int] = 1000, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of recent URLs added to URLhaus.

    Parameters:
        limit (Optional[int]): Limit the number of results returned (max 1000).
    """
    url = f"https://urlhaus-api.abuse.ch/v1/urls/recent/limit/{limit}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def query_recent_payloads(limit: Optional[int] = 1000, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of recent payloads seen by URLhaus.

    Parameters:
        limit (Optional[int]): Limit the number of results returned (max 1000).
    """
    url = f"https://urlhaus-api.abuse.ch/v1/payloads/recent/limit/{limit}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def query_url_info(url: Optional[str] = None, id: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific URL or URL ID.

    Parameters:
        url (Optional[str]): The URL to query.
        id (Optional[int]): The ID of the URL to query.
    """
    if url:
        request_url = "https://urlhaus-api.abuse.ch/v1/url/"
        data = {'url': url}
    elif id:
        request_url = "https://urlhaus-api.abuse.ch/v1/urlid/"
        data = {'urlid': id}
    else:
        return {"error": "Either 'url' or 'id' must be provided."}

    response = requests.post(request_url, data=data)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def query_host_info(host: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific host.

    Parameters:
        host (str): The host to query (IPv4 address, hostname, or domain name).
    """
    url = "https://urlhaus-api.abuse.ch/v1/host/"
    data = {'host': host}
    response = requests.post(url, data=data)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def query_payload_info(md5_hash: Optional[str] = None, sha256_hash: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific payload.

    Parameters:
        md5_hash (Optional[str]): The MD5 hash of the payload.
        sha256_hash (Optional[str]): The SHA256 hash of the payload.
    """
    if md5_hash:
        url = "https://urlhaus-api.abuse.ch/v1/payload/"
        data = {'md5_hash': md5_hash}
    elif sha256_hash:
        url = "https://urlhaus-api.abuse.ch/v1/payload/"
        data = {'sha256_hash': sha256_hash}
    else:
        return {"error": "Either 'md5_hash' or 'sha256_hash' must be provided."}

    response = requests.post(url, data=data)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def query_tag_info(tag: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific tag.

    Parameters:
        tag (str): The tag to query.
    """
    url = "https://urlhaus-api.abuse.ch/v1/tag/"
    data = {'tag': tag}
    response = requests.post(url, data=data)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def query_signature_info(signature: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific malware signature.

    Parameters:
        signature (str): The signature to query.
    """
    url = "https://urlhaus-api.abuse.ch/v1/signature/"
    data = {'signature': signature}
    response = requests.post(url, data=data)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def download_malware_sample(sha256: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Download a malware sample by its SHA256 hash.

    Parameters:
        sha256 (str): The SHA256 hash of the payload to download.
    """
    url = f"https://urlhaus-api.abuse.ch/v1/download/{sha256}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        try:
            return response.json()
        except Exception as e:
            return {"error": str(e), "response": response.text}