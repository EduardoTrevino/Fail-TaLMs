import requests
from typing import Optional, List, Dict, Union

def check_gender(name: str, country_id: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, List[Dict]]:
    """
    Predicts the gender of a single name. Optionally, the country_id can be used for localization.
    
    Parameters:
    name [Required]: string - The name to predict gender for.
    country_id [Optional]: string - Country code for localization following ISO 3166-1 alpha-2.

    Returns a dictionary with keys 'name', 'gender', 'probability', 'count', and possibly 'country_id'.
    """
    url = "https://api.genderize.io"
    params = {
        'name': name
    }
    if country_id:
        params['country_id'] = country_id
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def check_genders(names: List[str], country_id: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, List[Dict]]:
    """
    Predicts the gender of multiple names in one request. Optionally, the country_id can be used for localization.
    
    Parameters:
    names [Required]: list of strings - The names to predict genders for, maximum 10 names.
    country_id [Optional]: string - Country code for localization following ISO 3166-1 alpha-2.

    Returns a list of dictionaries each containing 'name', 'gender', 'probability', 'count', and possibly 'country_id'.
    """
    url = "https://api.genderize.io"
    params = {
        'name[]': names
    }
    if country_id:
        params['country_id'] = country_id
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}