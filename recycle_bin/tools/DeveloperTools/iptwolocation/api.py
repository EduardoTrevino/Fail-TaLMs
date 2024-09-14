import requests
from typing import Optional

def ipgeolocation(ip: str, format: Optional[str] = 'json', lang: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get geolocation information for a given IP address.
    """
    url = "https://api.ip2location.io/"
    querystring = {'ip': ip, 'format': format}
    if lang:
        querystring['lang'] = lang
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def domainwhois(domain: str, format: Optional[str] = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get WHOIS data for a given domain name.
    """
    url = "https://api.ip2whois.com/v2"
    querystring = {'domain': domain, 'format': format}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
