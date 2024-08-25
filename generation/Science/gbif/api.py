import requests
from typing import Optional, List

BASE_URL = "https://api.gbif.org/v1"

def list_datasets(
    country: Optional[str] = None,
    type: Optional[str] = None,
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Lists all current datasets (deleted datasets are not listed).
    """
    url = f"{BASE_URL}/dataset"
    params = {
        'country': country,
        'type': type,
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_datasets(
    q: Optional[str] = "",
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Full-text search across all datasets. Results are ordered by relevance.
    """
    url = f"{BASE_URL}/dataset/search"
    params = {
        'q': q,
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_dataset_details(
    key: str,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Get details of a single dataset. Also works for deleted datasets.
    """
    url = f"{BASE_URL}/dataset/{key}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_organizations(
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Lists all current publishing organizations (deleted organizations are not listed).
    """
    url = f"{BASE_URL}/organization"
    params = {
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_organization_details(
    key: str,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Get details of a single publishing organization. Also works for deleted publishing organizations.
    """
    url = f"{BASE_URL}/organization/{key}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_nodes(
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Lists all current nodes (deleted nodes are not listed).
    """
    url = f"{BASE_URL}/node"
    params = {
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_node_details(
    key: str,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Get details of a single node. Also works for deleted nodes.
    """
    url = f"{BASE_URL}/node/{key}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}