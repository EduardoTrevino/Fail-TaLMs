import requests
from typing import Optional, List

base_url = "https://quote-garden.onrender.com/api/v3"

def get_random_quote(author: Optional[str] = None, genre: Optional[str] = None, count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a single or multiple random quotes from the server.
    
    Parameters:
    author [Optional]: The author of the quote.
    genre [Optional]: The genre of the quote.
    count [Optional]: Number of quotes to retrieve.
    """
    url = f"{base_url}/quotes/random"
    params = {
        'author': author,
        'genre': genre,
        'count': count
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_quotes(author: Optional[str] = None, genre: Optional[str] = None, query: Optional[str] = None, page: Optional[int] = 1, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get multiple quotes based on parameters provided.
    
    Parameters:
    author [Optional]: Filter quotes by author.
    genre [Optional]: Filter quotes by genre.
    query [Optional]: Search query within quotes.
    page [Optional]: Pagination for results.
    limit [Optional]: Limit number of quotes per page.
    """
    url = f"{base_url}/quotes"
    params = {
        'author': author,
        'genre': genre,
        'query': query,
        'page': page,
        'limit': limit
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_all_genres(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all available genres of quotes.
    """
    url = f"{base_url}/genres"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_all_authors(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all available authors of quotes.
    """
    url = f"{base_url}/authors"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}