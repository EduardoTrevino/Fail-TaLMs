import requests
from typing import Optional


def search_cocktail_by_name(name: str = "margarita"):
    """
    Search cocktail by name.
    Parameters:
    name (str): The name of the cocktail to search for.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    params = {'s': name}
    response = requests.get(url, params=params)
    
    print(f"Request URL: {response.url}")  # Print the final URL
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return {"error": f"Status Code: {response.status_code}"}
    
    return response.json()


def list_cocktails_by_first_letter(letter: str = "a", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all cocktails by first letter.
    Parameters:
    letter (str): The letter to filter cocktails by.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    params = {'f': letter}
    response = requests.get(url, params=params)
    return response.json()


def search_ingredient_by_name(ingredient: str = "vodka", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search ingredient by name.
    Parameters:
    ingredient (str): The name of the ingredient to search for.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    params = {'i': ingredient}
    response = requests.get(url, params=params)
    return response.json()


def lookup_cocktail_by_id(cocktail_id: int = 11007, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Lookup full cocktail details by ID.
    Parameters:
    cocktail_id (int): The ID of the cocktail to look up.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php"
    params = {'i': cocktail_id}
    response = requests.get(url, params=params)
    return response.json()


def lookup_ingredient_by_id(ingredient_id: int = 552, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Lookup ingredient by ID.
    Parameters:
    ingredient_id (int): The ID of the ingredient to look up.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php"
    params = {'iid': ingredient_id}
    response = requests.get(url, params=params)
    return response.json()


def lookup_random_cocktail(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Lookup a random cocktail.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    return response.json()


def search_by_ingredient(ingredient: str = "Gin", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search by ingredient.
    Parameters:
    ingredient (str): The ingredient to filter cocktails by.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    params = {'i': ingredient}
    response = requests.get(url, params=params)
    return response.json()


def filter_by_alcoholic(alcoholic_type: str = "Alcoholic", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter by alcoholic.
    Parameters:
    alcoholic_type (str): The type ('Alcoholic' or 'Non_Alcoholic') to filter cocktails by.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    params = {'a': alcoholic_type}
    response = requests.get(url, params=params)
    return response.json()


def filter_by_category(category: str = "Ordinary_Drink", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter by category.
    Parameters:
    category (str): The category to filter cocktails by.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    params = {'c': category}
    response = requests.get(url, params=params)
    return response.json()


def filter_by_glass(glass: str = "Cocktail_glass", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Filter by glass.
    Parameters:
    glass (str): The glass type to filter cocktails by.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    params = {'g': glass}
    response = requests.get(url, params=params)
    return response.json()


def list_categories(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List the categories.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php"
    params = {'c': 'list'}
    response = requests.get(url, params=params)
    return response.json()


def list_glasses(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List the glasses.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php"
    params = {'g': 'list'}
    response = requests.get(url, params=params)
    return response.json()


def list_ingredients(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List the ingredients.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php"
    params = {'i': 'list'}
    response = requests.get(url, params=params)
    return response.json()


def list_alcoholic_filters(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List the alcoholic filters.
    """
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php"
    params = {'a': 'list'}
    response = requests.get(url, params=params)
    return response.json()