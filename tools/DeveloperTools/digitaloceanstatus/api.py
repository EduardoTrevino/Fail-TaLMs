import requests
from typing import Optional

def get_summary(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a summary of the status page, including a status indicator, component statuses, unresolved incidents, 
    and any upcoming or in-progress scheduled maintenances.
    """
    url = "https://status.digitalocean.com/api/v2/summary.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_components(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the components for the page. 
    """
    url = "https://status.digitalocean.com/api/v2/components.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_unresolved_incidents(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of any unresolved incidents. 
    """
    url = "https://status.digitalocean.com/api/v2/incidents/unresolved.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_all_incidents(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of the 50 most recent incidents. 
    """
    url = "https://status.digitalocean.com/api/v2/incidents.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_upcoming_maintenances(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of any upcoming scheduled maintenances. 
    """
    url = "https://status.digitalocean.com/api/v2/scheduled-maintenances/upcoming.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_active_maintenances(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of any active scheduled maintenances. 
    """
    url = "https://status.digitalocean.com/api/v2/scheduled-maintenances/active.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_all_maintenances(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of the 50 most recent scheduled maintenances. 
    """
    url = "https://status.digitalocean.com/api/v2/scheduled-maintenances.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}