import requests
from typing import Optional, List


def ip_geolocation(ip: Optional[str] = None, format: Optional[str] = 'json', lang: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get geolocation information for a given IP address.
    Parameters:
    ip [Optional]: string [Description: IP address (IPv4 or IPv6), if not provided, the caller's IP will be used]
    format [Optional]: string [Description: Response format, valid values: json | xml, default is json]
    lang [Optional]: string [Description: Translation language in ISO639-1, applicable for certain plans only]
    """
    url = "https://api.ip2location.io/"
    params = {
        'ip': ip,
        'key': toolbench_rapidapi_key,
        'format': format
    }
    if lang:
        params['lang'] = lang

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def domain_whois(domain: str, format: Optional[str] = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get WHOIS data for a given domain name.
    Parameters:
    domain [Required]: string [Description: Domain name for the WHOIS lookup]
    format [Optional]: string [Description: Response format, valid values: json | xml, default is json]
    """
    url = "https://api.ip2whois.com/v2"
    params = {
        'domain': domain,
        'key': toolbench_rapidapi_key,
        'format': format
    }

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def bulk_ip_geolocation(ips: List[str], format: Optional[str] = 'json', fields: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get geolocation information for multiple IP addresses in bulk.
    Parameters:
    ips [Required]: list of strings [Description: IP addresses (IPv4 or IPv6) to lookup]
    format [Optional]: string [Description: Response format, valid values: json | csv, default is json]
    fields [Optional]: string [Description: Custom fields to return, separated by commas, defaults to all fields]
    """
    url = "https://bulk.ip2location.io/"
    params = {
        'key': toolbench_rapidapi_key,
        'format': format,
    }
    if fields:
        params['fields'] = fields
    
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, params=params, headers=headers, json=ips)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}