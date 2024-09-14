import requests
import json
from typing import Optional, Dict, Union, List

def lists(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Gets the list of FilterLists, including details such as the name, description, license, syntax, languages, tags, and maintainer information.
    """
    url = f"https://filterlistsapi.example.com/v1/lists"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def languages(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Gets the languages targeted by the FilterLists.
    """
    url = f"https://filterlistsapi.example.com/v1/languages"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def licenses(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Gets the licenses applied to the FilterLists, including details about modification, distribution, and commercial use permissions.
    """
    url = f"https://filterlistsapi.example.com/v1/licenses"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
