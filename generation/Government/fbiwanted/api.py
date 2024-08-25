import requests
from typing import Optional

def get_wanted_list(field_offices: Optional[str] = None, page: Optional[int] = 1, 
                    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint that retrieves information from the FBI Wanted list.
    
    Parameters:
    field_offices [Optional]: string - Filter results by specific FBI field offices.
    page [Optional]: integer - The page of resources to retrieve.
    """
    url = "https://api.fbi.gov/wanted/v1/list"
    params = {
        'field_offices': field_offices,
        'page': page
    }
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}