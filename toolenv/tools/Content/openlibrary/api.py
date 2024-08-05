import requests
import json
from typing import Optional, Dict, List

def search(query: str, fields: Optional[str]=None, sort: Optional[str]=None, lang: Optional[str]=None, page: Optional[int]=1, limit: Optional[int]=10, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search results for books, authors, and more"
    """
    url = "https://openlibrary.org/search.json"
    querystring = {'q': query, 'page': page, 'limit': limit}
    if fields:
        querystring['fields'] = fields
    if sort:
        querystring['sort'] = sort
    if lang:
        querystring['lang'] = lang

    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def author(author_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve an author and their works by author identifier"
    """
    url = f"https://openlibrary.org/authors/{author_id}.json"
    
    headers = {
        "X-RapidAPI-Key": toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
