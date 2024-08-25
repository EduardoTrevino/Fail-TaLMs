import requests
from typing import Optional, Dict, Any

def get_animal_adr(limit: Optional[int] = 10, skip: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve animal and veterinary adverse event reports.
    
    Parameters:
    - limit: Optional; number of records to return.
    - skip: Optional; number of records to skip.
    """
    url = "https://api.fda.gov/animalandveterinary/event.json"
    params = {'limit': limit, 'skip': skip}
    response = requests.get(url, params=params)
    return response.json()

def get_drug_event(limit: Optional[int] = 10, skip: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve drug adverse event reports.
    
    Parameters:
    - limit: Optional; number of records to return.
    - skip: Optional; number of records to skip.
    """
    url = "https://api.fda.gov/drug/event.json"
    params = {'limit': limit, 'skip': skip}
    response = requests.get(url, params=params)
    return response.json()

def get_drug_label(limit: Optional[int] = 10, skip: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve drug labeling information.
    
    Parameters:
    - limit: Optional; number of records to return.
    - skip: Optional; number of records to skip.
    """
    url = "https://api.fda.gov/drug/label.json"
    params = {'limit': limit, 'skip': skip}
    response = requests.get(url, params=params)
    return response.json()

def get_device_event(limit: Optional[int] = 10, skip: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve device adverse event reports.
    
    Parameters:
    - limit: Optional; number of records to return.
    - skip: Optional; number of records to skip.
    """
    url = "https://api.fda.gov/device/event.json"
    params = {'limit': limit, 'skip': skip}
    response = requests.get(url, params=params)
    return response.json()

def get_device_udi(limit: Optional[int] = 10, skip: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve device unique device identifier (UDI) information.
    
    Parameters:
    - limit: Optional; number of records to return.
    - skip: Optional; number of records to skip.
    """
    url = "https://api.fda.gov/device/udi.json"
    params = {'limit': limit, 'skip': skip}
    response = requests.get(url, params=params)
    return response.json()