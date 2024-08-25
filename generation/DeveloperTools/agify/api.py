import requests
from typing import Optional, List, Dict, Union

def estimate_age(
    name: str,
    country_id: Optional[str] = None,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Union[str, int]]:
    """
    Estimate the age of a person based on their first name.
    
    Parameters:
    - name (str): The first name to estimate age for.
    - country_id (str, optional): The country code to improve estimation accuracy.
    
    Returns:
    - A dictionary with the predicted age and count of data rows examined.
    """
    url = "https://api.agify.io"
    params = {
        'name': name,
    }
    if country_id:
        params['country_id'] = country_id

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def estimate_age_batch(
    names: List[str],
    country_id: Optional[str] = None,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> List[Dict[str, Union[str, int]]]:
    """
    Estimate the age for a batch of names.
    
    Parameters:
    - names (List[str]): A list of first names (up to 10) to estimate ages for.
    - country_id (str, optional): The country code to improve estimation accuracy across all names.
    
    Returns:
    - A list of dictionaries with predicted ages and counts for each name.
    """
    url = "https://api.agify.io"
    params = [('name[]', name) for name in names]
    if country_id:
        params.append(('country_id', country_id))

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}