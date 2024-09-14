import requests
import json
from typing import Optional, Dict, Union, List

def create(url: str, format: Optional[str] = 'simple', shorturl: Optional[str] = None, logstats: Optional[bool] = False, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Shortens a given URL and returns the shortened version in the specified format.
    """
    api_url = "https://is.gd/create.php"
    querystring = {
        'url': url,
        'format': format
    }
    if shorturl:
        querystring['shorturl'] = shorturl
    if logstats:
        querystring['logstats'] = '1'
    
    response = requests.get(api_url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def logstats(shorturl: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves detailed statistics for a shortened URL if logging is enabled.
    """
    stats_url = f"https://is.gd/stats.php?url={shorturl}&format=json"
    
    response = requests.get(stats_url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
