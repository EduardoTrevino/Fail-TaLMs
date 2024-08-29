import requests
from typing import Optional, List

def list_competitions(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', areas: Optional[str] = None):
    """
    List all available competitions.
    
    Parameters:
    areas (str): Comma separated list of area IDs.
    """
    url = "https://api.football-data.org/v4/competitions"
    params = {}
    if areas:
        params['areas'] = areas
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}
