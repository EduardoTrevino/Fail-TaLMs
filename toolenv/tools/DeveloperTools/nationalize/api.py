import requests
import json
from typing import Optional, Dict, Union, List

def predict_single_name(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Predict the nationality of a single name.
    """
    url = f"https://api.nationalize.io/"
    querystring = {'name': name}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def predict_multiple_names(names: List[str], toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Predict the nationality of multiple names.
    """
    url = f"https://api.nationalize.io/"
    querystring = {'name[]': names}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
