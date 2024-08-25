import requests
from typing import Optional

def get_next_mcu_production(date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Returns details of the next MCU production.
    Parameters:
    - date [Optional]: string [Description: ISO formatted date to get the next MCU production from this date. Uses today's date by default.]
    """
    url = "https://api.mcucountdown.com/api"
    params = {}
    if date:
        params['date'] = date

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}