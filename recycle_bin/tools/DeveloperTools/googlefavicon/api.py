import requests
from typing import Optional

def getfavicon(domain: str, sz: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the favicon for a given domain. Optionally, specify the size of the favicon.
    
    :param domain: The domain from which to fetch the favicon.
    :param sz: The size of the favicon in pixels (optional).
    :param toolbench_rapidapi_key: Placeholder for the API key (not used).
    :return: URL of the fetched favicon.
    """
    url = "https://www.google.com/s2/favicons"
    params = {'domain': domain}
    if sz:
        params['sz'] = sz

    response = requests.get(url, params=params)
    try:
        favicon_url = response.url
    except Exception as e:
        favicon_url = str(e)
    return favicon_url


def getfaviconfallback(domain: str, sz: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the fallback favicon if the specified size is not available. Returns the default 16x16 favicon if the requested size is not found.
    
    :param domain: The domain from which to fetch the favicon.
    :param sz: The size of the favicon in pixels (optional).
    :param toolbench_rapidapi_key: Placeholder for the API key (not used).
    :return: URL of the fetched fallback favicon.
    """
    url = "https://www.google.com/s2/favicons"
    params = {'domain': domain}
    if sz:
        params['sz'] = sz

    response = requests.get(url, params=params)
    try:
        favicon_url = response.url
    except Exception as e:
        favicon_url = str(e)
    return favicon_url
