import requests
import json
from typing import Optional, Dict, Union, List

def search_cocktail_by_name(s: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for a cocktail by name.
    """
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php"
    querystring = {'s': s}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def lookup_cocktail_by_id(i: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Lookup full cocktail details by id.
    """
    url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php"
    querystring = {'i': i}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def filter_cocktail_by_ingredient(i: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter cocktails by ingredient.
    """
    url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    querystring = {'i': i}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
