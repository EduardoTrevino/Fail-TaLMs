import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List

def parse(page: str, prop: str='text', format: str='json', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the contents of a page in HTML format."
    """
    url = "https://en.wikipedia.org/w/api.php"
    querystring = {'action': 'parse', 'page': page, 'prop': prop, 'format': format}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def query(titles: str, prop: str='revisions|categories', format: str='json', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Fetch data from and about MediaWiki."
    """
    url = "https://en.wikipedia.org/w/api.php"
    querystring = {'action': 'query', 'titles': titles, 'prop': prop, 'format': format}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
