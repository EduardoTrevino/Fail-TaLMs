import requests
import json
from typing import Optional, Dict, Union, List

def age_estimation(name: str, country_id: Optional[str]=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Estimate the age of a person based on their first name.
    
    Parameters:
    - name: The first name of the person to estimate the age for.
    - country_id: Optional, ISO 3166-1 alpha-2 country code to improve estimation accuracy.
    
    Returns:
    A dictionary with the estimated age and additional information.
    """
    url = "https://api.agify.io"
    querystring = {'name': name}
    if country_id:
        querystring['country_id'] = country_id
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def batch_age_estimation(names: List[str], country_id: Optional[str]=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Estimate the age of multiple people based on their first names.
    
    Parameters:
    - names: A list of first names to estimate ages for.
    - country_id: Optional, ISO 3166-1 alpha-2 country code to improve estimation accuracy for all names in the batch.
    
    Returns:
    A list of dictionaries with the estimated ages and additional information.
    """
    url = "https://api.agify.io"
    querystring = {'name[]': names}
    if country_id:
        querystring['country_id'] = country_id
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
