import requests
from typing import Optional, List, Dict

# Define the API key as a parameter
toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

def search_universities(name: str, country: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> List[Dict]:
    """
    Search for universities by name and optionally filter by country.
    Supports pagination with limit and offset.

    Parameters:
    - name (str): The name or part of the name of the university to search for.
    - country (Optional[str]): The country to filter results by.
    - limit (Optional[int]): A limit on the number of results to return.
    - offset (Optional[int]): The number of results to skip.

    Returns:
    List[Dict]: A list of dictionaries containing university data.
    """
    url = "http://universities.hipolabs.com/search"
    params = {
        'name': name
    }
    if country:
        params['country'] = country
    if limit is not None:
        params['limit'] = limit
    if offset is not None:
        params['offset'] = offset

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}