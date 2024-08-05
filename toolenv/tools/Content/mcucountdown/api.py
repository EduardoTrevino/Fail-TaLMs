import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List

def nextmcuproduction(date: Optional[str] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details of the next MCU production including days until release, overview, poster URL, release date, title, and type.
    """
    url = f"https://mcucountdown.api/next"
    querystring = {}
    if date:
        querystring['date'] = date
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def followingproduction(date: Optional[str] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details of the MCU production following the next one including days until release, overview, poster URL, release date, title, and type.
    """
    url = f"https://mcucountdown.api/following"
    querystring = {}
    if date:
        querystring['date'] = date
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
