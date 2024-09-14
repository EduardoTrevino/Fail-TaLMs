import requests
import json
from typing import Optional, Dict, Union, List

def search_books(query: str, fields: Optional[str] = None, sort: Optional[str] = None, 
                 lang: Optional[str] = None, page: Optional[int] = 1, limit: Optional[int] = 10, 
                 toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for books in Open Library.
    """
    url = "https://openlibrary.org/search.json"
    params = {'q': query, 'page': page, 'limit': limit}
    
    if fields:
        params['fields'] = fields
    if sort:
        params['sort'] = sort
    if lang:
        params['lang'] = lang
    
    response = requests.get(url, params=params)
    try:
        result = response.json()
    except:
        result = response.text
    
    return result

def get_author_details(author_id: str, 
                       toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve details of an author by author identifier.
    """
    url = f"https://openlibrary.org/authors/{author_id}.json"
    
    response = requests.get(url)
    try:
        result = response.json()
    except:
        result = response.text
    
    return result
