import requests
from typing import List, Optional

def predictgender(name: str, country_id: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Predict the gender based on a single name.
    """
    url = "https://api.genderize.io"
    params = {'name': name}
    
    if country_id:
        params['country_id'] = country_id
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def predictbatchgender(names: List[str], country_id: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Predict the gender for multiple names in a single request.
    """
    url = "https://api.genderize.io"
    params = {'name[]': names}
    
    if country_id:
        params['country_id'] = country_id
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
