import requests
from typing import Optional, List, Dict

def search_books(q: str, fields: Optional[str] = "*", sort: Optional[str] = None, lang: Optional[str] = None, page: Optional[int] = 1, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for books using Open Library Search API.
    Parameters:
    - q: Query string.
    - fields: Fields to return. Default is all fields.
    - sort: Sort the results by various facets.
    - lang: Language code. Influences the result preference.
    - page: Page number for pagination.
    - limit: Number of results per page (page size).
    """
    url = "https://openlibrary.org/search.json"
    params = {
        'q': q,
        'fields': fields,
        'sort': sort,
        'lang': lang,
        'page': page,
        'limit': limit
    }
    response = requests.get(url, params=params)
    return response.json()

def get_work_by_id(work_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a specific work by its Open Library work ID.
    Parameters:
    - work_id: Open Library Work ID.
    """
    url = f"https://openlibrary.org/works/{work_id}.json"
    response = requests.get(url)
    return response.json()

def get_edition_by_id(edition_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a specific edition by its Open Library edition ID.
    Parameters:
    - edition_id: Open Library Edition ID.
    """
    url = f"https://openlibrary.org/books/{edition_id}.json"
    response = requests.get(url)
    return response.json()

def get_author_by_id(author_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve author details and their works by author identifier.
    Parameters:
    - author_id: Open Library Author ID.
    """
    url = f"https://openlibrary.org/authors/{author_id}.json"
    response = requests.get(url)
    return response.json()

def search_authors(q: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for authors using Open Library Authors API.
    Parameters:
    - q: Query string for author's name.
    """
    url = f"https://openlibrary.org/search/authors.json"
    params = {'q': q}
    response = requests.get(url, params=params)
    return response.json()

def get_subject_works(subject_name: str, details: Optional[bool] = False, limit: Optional[int] = 10, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch works under a specific subject.
    Parameters:
    - subject_name: Name of the subject.
    - details: Whether to fetch detailed information.
    - limit: Number of works to include in the response.
    - offset: Starting offset for pagination.
    """
    url = f"https://openlibrary.org/subjects/{subject_name}.json"
    params = {
        'details': 'true' if details else 'false',
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    return response.json()

def get_book_cover(key: str, value: str, size: str = "M", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch book covers by ISBN or Open Library identifier
    Parameters:
    - key: The type of identifier used (ISBN, OLID, etc.)
    - value: The value of the chosen key
    - size: Size of the cover ('S', 'M', 'L')
    """
    url = f"https://covers.openlibrary.org/b/{key}/{value}-{size}.jpg"
    response = requests.get(url)
    if response.status_code == 404:
        return None
    return url

def recent_changes(limit: Optional[int] = 10, kind: Optional[str] = None, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get recent changes across Open Library.
    Parameters:
    - limit: Maximum number of entries in the response.
    - offset: Number of entries to skip.
    - kind: Type of change.
    - date: Specific date for changes in the format YYYY/MM/DD.
    """
    url = "https://openlibrary.org/recentchanges.json"
    if date:
        url = f"https://openlibrary.org/recentchanges/{date}.json"
    if kind:
        url = f"https://openlibrary.org/recentchanges/{kind}.json"
    
    params = {
        'limit': limit,
    }
    response = requests.get(url, params=params)
    return response.json()