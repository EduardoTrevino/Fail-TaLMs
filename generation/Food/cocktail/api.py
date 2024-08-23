import requests
from typing import Optional

def search_cocktail_by_name(s: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Search cocktail by name.
    Parameters:
    s [Required]: string [Cocktail name to search for].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    params = {'s': s}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_all_cocktails_by_first_letter(f: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: List all cocktails by first letter.
    Parameters:
    f [Required]: string [First letter to list cocktails by].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    params = {'f': f}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_ingredient_by_name(i: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Search ingredient by name.
    Parameters:
    i [Required]: string [Ingredient name to search for].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    params = {'i': i}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def lookup_full_cocktail_details_by_id(i: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Lookup full cocktail details by id.
    Parameters:
    i [Required]: integer [Cocktail ID to lookup].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php"
    params = {'i': i}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def lookup_ingredient_by_id(iid: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Lookup ingredient by ID.
    Parameters:
    iid [Required]: integer [Ingredient ID to lookup].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php"
    params = {'iid': iid}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def lookup_random_cocktail(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Lookup a random cocktail.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_by_ingredient(i: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Search by ingredient.
    Parameters:
    i [Required]: string [Ingredient to filter by].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    params = {'i': i}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def filter_by_alcoholic(a: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Filter by alcoholic.
    Parameters:
    a [Required]: string [Alcoholic or Non_Alcoholic].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    params = {'a': a}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def filter_by_category(c: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Filter by category.
    Parameters:
    c [Required]: string [Category to filter by].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    params = {'c': c}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def filter_by_glass(g: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: Filter by glass.
    Parameters:
    g [Required]: string [Glass type to filter by].
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    params = {'g': g}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_categories(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: List categories.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php"
    params = {'c': 'list'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_glasses(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: List glasses.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php"
    params = {'g': 'list'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_ingredients(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: List ingredients.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php"
    params = {'i': 'list'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_alcoholic(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint: List alcoholic filters.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php"
    params = {'a': 'list'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}