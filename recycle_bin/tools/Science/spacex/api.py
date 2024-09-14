import requests
from typing import Optional, Dict, List, Union

def get_company_info(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about SpaceX company.
    """
    url = "https://api.spacexdata.com/v4/company"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def get_launches(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all SpaceX launches.
    """
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def get_rockets(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all SpaceX rockets.
    """
    url = "https://api.spacexdata.com/v4/rockets"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def get_capsules(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all SpaceX capsules.
    """
    url = "https://api.spacexdata.com/v4/capsules"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def get_one_capsule(id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve one SpaceX capsule by ID.
    """
    url = f"https://api.spacexdata.com/v4/capsules/{id}"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def query_capsules(query: Dict, options: Dict, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Query SpaceX capsules with specific parameters.
    """
    url = "https://api.spacexdata.com/v4/capsules/query"
    body = {
        "query": query,
        "options": options
    }
    response = requests.post(url, json=body)
    try:
        return response.json()
    except:
        return response.text
