import requests
import json
from typing import Optional, Dict, Union, List

def summary(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a summary of the status page, including a status indicator, component statuses, unresolved incidents, 
    and any upcoming or in-progress scheduled maintenances.
    """
    url = "https://status.digitalocean.com/api/v2/summary.json"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def components(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the components for the page. Each component is listed along with its status.
    """
    url = "https://status.digitalocean.com/api/v2/components.json"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def all_incidents(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of the 50 most recent incidents, including unresolved, resolved, and postmortem states.
    """
    url = "https://status.digitalocean.com/api/v2/incidents.json"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
