import requests
from typing import Optional

def get_schedule(user: str, date: str, channel: str, regiony: Optional[bool] = False, json_format: Optional[bool] = False, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> dict:
    """
    Fetches the TV schedule for a given date and channel.

    Parameters:
    - user: User login.
    - date: Date in dd.mm.yyyy format.
    - channel: Channel identifier.
    - regiony: Include regional broadcasts. Default is False.
    - json_format: Get response in JSON format. Default is False.

    Returns:
    - dict: The API response.
    """
    url = f"https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php"
    params = {
        'user': user,
        'date': date,
        'channel': channel,
        'regiony': int(regiony),
        'json': int(json_format)
    }

    response = requests.get(url, params=params)
    try:
        if json_format:
            return response.json()
        else:
            return response.text
    except Exception as e:
        return {'error': str(e)}

# Example usage:
# print(get_schedule(user='test', date='04.08.2024', channel='ct1', regiony=True, json_format=True))
