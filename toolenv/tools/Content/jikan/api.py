import requests
import json
from datetime import date, datetime, timedelta
import os
from typing import Optional, Dict, Union, List

def getAnimeById(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific anime by its MyAnimeList ID.
    """
    url = f"https://api.jikan.moe/v4/anime/{id}"
    
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key,
        "X-RapidAPI-Host": "api.jikan.moe"
    }
    
    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getAnimeCharacters(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the characters of a specific anime by its MyAnimeList ID.
    """
    url = f"https://api.jikan.moe/v4/anime/{id}/characters"
    
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key,
        "X-RapidAPI-Host": "api.jikan.moe"
    }
    
    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getAnimeStaff(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the staff of a specific anime by its MyAnimeList ID.
    """
    url = f"https://api.jikan.moe/v4/anime/{id}/staff"
    
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key,
        "X-RapidAPI-Host": "api.jikan.moe"
    }
    
    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
