import requests
from typing import Optional


def get_public_ip_v4(format: Optional[str] = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> dict:
    """
    Get the public IPv4 address in the specified format.
    
    :param format: The format in which to retrieve the IP address ('json', 'jsonp', or 'text').
    :return: A dictionary with the IP address or an error message.
    """
    url = "https://api.ipify.org"
    params = {'format': format}
    try:
        response = requests.get(url, params=params)
        if format == 'json':
            return response.json()
        elif format == 'jsonp' or format == 'text':
            return {"ip": response.text}
    except Exception as e:
        return {"error": str(e)}


def get_public_ip(format: Optional[str] = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> dict:
    """
    Get the public IP address (IPv4/IPv6) in the specified format.

    :param format: The format in which to retrieve the IP address ('json', 'jsonp', or 'text').
    :return: A dictionary with the IP address or an error message.
    """
    url = "https://api64.ipify.org"
    params = {'format': format}
    try:
        response = requests.get(url, params=params)
        if format == 'json':
            return response.json()
        elif format == 'jsonp' or format == 'text':
            return {"ip": response.text}
    except Exception as e:
        return {"error": str(e)}