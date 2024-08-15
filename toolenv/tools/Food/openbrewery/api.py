import requests
from typing import Optional

def listbreweries(page: Optional[int] = 1, per_page: Optional[int] = 50, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of breweries.
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        "page": page,
        "per_page": per_page
    }
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def by_city(city: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter breweries by city.
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        "by_city": city
    }
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def by_type(brewery_type: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter breweries by type.
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        "by_type": brewery_type
    }
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
