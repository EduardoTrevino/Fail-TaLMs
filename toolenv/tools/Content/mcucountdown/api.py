import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def nextmcuproduction(date: str = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details of the next MCU production including days until release, overview, poster URL, release date, title, and type.
    """
    url = "https://mcucountdown.example.com/api"
    querystring = {}
    if date:
        querystring['date'] = date

    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key,
        "X-RapidAPI-Host": "mcucountdown.example.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def followingproduction(date: str = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get details of the MCU production following the next one including days until release, overview, poster URL, release date, title, and type.
    """
    url = "https://mcucountdown.example.com/api"
    querystring = {}
    if date:
        querystring['date'] = date

    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key,
        "X-RapidAPI-Host": "mcucountdown.example.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
