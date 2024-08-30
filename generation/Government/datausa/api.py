import requests
from typing import Optional, List

def get_population_data(drilldowns: str = 'Nation', measures: str = 'Population', year: Optional[str] = 'latest', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get population data for specified geographical drilldowns and measures.
    Parameters:
        drilldowns [Optional]: string [Description: The geographical level to retrieve data for, e.g., 'Nation' or 'State'. Default is 'Nation'.]
        measures [Optional]: string [Description: The measure to retrieve data for, e.g., 'Population'. Default is 'Population'.]
        year [Optional]: string [Description: The year of data to retrieve, 'latest' for the most recent. Default is 'latest'.]
    """
    url = "https://datausa.io/api/data"
    params = {
        'drilldowns': drilldowns,
        'measures': measures,
        'year': year
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}