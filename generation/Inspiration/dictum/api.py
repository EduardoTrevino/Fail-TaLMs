import requests
from typing import Optional, Dict, Any, List

def get_authors(language: str, query: Optional[str] = None, offset: Optional[int] = 0, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict[str, Any]]:
    url = f"https://api.dictum.com/v1/authors/{language}"
    params = {
        'query': query,
        'offset': offset,
        'limit': limit
    }
    response = requests.get(url, params=params)
    return response.json()

def get_author(language: str, author_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    url = f"https://api.dictum.com/v1/authors/{language}/{author_id}"
    response = requests.get(url)
    return response.json()

def search_author_quotes(language: str, author_id: str, query: Optional[str] = None, offset: Optional[int] = 0, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict[str, Any]]:
    url = f"https://api.dictum.com/v1/authors/{language}/{author_id}/quotes"
    params = {
        'query': query,
        'offset': offset,
        'limit': limit
    }
    response = requests.get(url, params=params)
    return response.json()

def get_languages(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict[str, Any]]:
    url = "https://api.dictum.com/v1/languages"
    response = requests.get(url)
    return response.json()

def like_quote(language: str, quote_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    url = f"https://api.dictum.com/v1/likes/{language}"
    data = {'likeQuote': {'quote-id': quote_id}}
    response = requests.post(url, json=data)
    return response.json()

def search_quotes(language: str, query: Optional[str] = None, offset: Optional[int] = 0, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[Dict[str, Any]]:
    url = f"https://api.dictum.com/v1/quotes/{language}"
    params = {
        'query': query,
        'offset': offset,
        'limit': limit
    }
    response = requests.get(url, params=params)
    return response.json()

def create_quote(language: str, author_id: str, text: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    url = f"https://api.dictum.com/v1/quotes/{language}"
    data = {'quote': {'author-id': author_id, 'text': text}}
    response = requests.post(url, json=data)
    return response.json()

def get_random_quote(language: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    url = f"https://api.dictum.com/v1/quotes/{language}/random"
    response = requests.get(url)
    return response.json()

def get_quote(language: str, quote_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    url = f"https://api.dictum.com/v1/quotes/{language}/{quote_id}"
    response = requests.get(url)
    return response.json()

def get_statistics(language: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    url = f"https://api.dictum.com/v1/statistics/{language}"
    response = requests.get(url)
    return response.json()