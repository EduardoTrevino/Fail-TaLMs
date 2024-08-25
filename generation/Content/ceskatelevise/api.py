import requests
from typing import Optional

def get_tv_schedule(user: str, date: str, channel: str, regiony: Optional[int] = None, json_format: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the TV schedule for a specific date and channel.

    Parameters:
    - user: The username required to access the API.
    - date: The date for which you want the schedule in the format dd.mm.yyyy.
    - channel: The channel identifier (ct1, ct2, ct24, ct4, ct5, ct6, ct7).
    - regiony: Optional; Set to 1 to include regional broadcasts.
    - json_format: Optional; Set to 1 to retrieve data in JSON format.

    Returns:
    The response containing the schedule in XML or JSON format based on the `json_format` parameter.
    """
    base_url = "https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php"
    params = {
        'user': user,
        'date': date,
        'channel': channel
    }
    if regiony is not None:
        params['regiony'] = regiony
    if json_format is not None:
        params['json'] = json_format
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.text