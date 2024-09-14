import requests

def get_random_joke(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a random Chuck Norris joke in JSON format.
    """
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_random_joke_by_category(category: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a random Chuck Norris joke from a given category.
    
    Parameters:
    category [Required]: string [Description: The category to retrieve a joke from.]
    """
    url = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_joke_categories(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of available categories for Chuck Norris jokes.
    """
    url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_jokes(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Free text search for Chuck Norris jokes.
    
    Parameters:
    query [Required]: string [Description: The search query for jokes.]
    """
    url = f"https://api.chucknorris.io/jokes/search?query={query}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}