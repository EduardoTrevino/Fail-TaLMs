import requests
from typing import Optional


def get_random_quote(max_length: Optional[int] = None, min_length: Optional[int] = None, tags: Optional[str] = None, author: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a single random quote with optional filters.
    """
    url = "https://api.quotable.io/random"
    params = {
        'maxLength': max_length,
        'minLength': min_length,
        'tags': tags,
        'author': author,
    }
    response = requests.get(url, params=params)
    return response.json()


def get_random_quotes(limit: int = 1, max_length: Optional[int] = None, min_length: Optional[int] = None, tags: Optional[str] = None, author: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve one or more random quotes with optional filters.
    """
    url = "https://api.quotable.io/quotes/random"
    params = {
        'limit': limit,
        'maxLength': max_length,
        'minLength': min_length,
        'tags': tags,
        'author': author,
    }
    response = requests.get(url, params=params)
    return response.json()


def list_quotes(max_length: Optional[int] = None, min_length: Optional[int] = None, tags: Optional[str] = None, author: Optional[str] = None, sort_by: Optional[str] = 'dateAdded', order: Optional[str] = None, limit: Optional[int] = 20, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all quotes matching a given query with pagination and sorting options.
    """
    url = "https://api.quotable.io/quotes"
    params = {
        'maxLength': max_length,
        'minLength': min_length,
        'tags': tags,
        'author': author,
        'sortBy': sort_by,
        'order': order,
        'limit': limit,
        'page': page,
    }
    response = requests.get(url, params=params)
    return response.json()


def get_quote_by_id(quote_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a quote by its ID.
    """
    url = f"https://api.quotable.io/quotes/{quote_id}"
    response = requests.get(url)
    return response.json()


def list_authors(slug: Optional[str] = None, sort_by: Optional[str] = 'name', order: Optional[str] = None, limit: Optional[int] = 20, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all authors matching the given query, with several options for sorting and filtering.
    """
    url = "https://api.quotable.io/authors"
    params = {
        'slug': slug,
        'sortBy': sort_by,
        'order': order,
        'limit': limit,
        'page': page,
    }
    response = requests.get(url, params=params)
    return response.json()


def search_quotes(query: str, fields: str = 'content,author,tags', fuzzy_max_edits: Optional[int] = 0, fuzzy_max_expansions: Optional[int] = 50, limit: Optional[int] = 20, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for quotes by keywords, content, and/or author name.
    """
    url = "https://api.quotable.io/search/quotes"
    params = {
        'query': query,
        'fields': fields,
        'fuzzyMaxEdits': fuzzy_max_edits,
        'fuzzyMaxExpansions': fuzzy_max_expansions,
        'limit': limit,
        'page': page,
    }
    response = requests.get(url, params=params)
    return response.json()


def search_authors(query: str, autocomplete: Optional[bool] = True, match_threshold: Optional[int] = 2, limit: Optional[int] = 20, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for authors by name with autocomplete.
    """
    url = "https://api.quotable.io/search/authors"
    params = {
        'query': query,
        'autocomplete': autocomplete,
        'matchThreshold': match_threshold,
        'limit': limit,
        'page': page,
    }
    response = requests.get(url, params=params)
    return response.json()


def get_author_by_slug(slug: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a single Author by slug.
    """
    url = f"https://api.quotable.io/authors/{slug}"
    response = requests.get(url)
    return response.json()


def list_tags(sort_by: Optional[str] = 'name', order: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all tags with sorting options.
    """
    url = "https://api.quotable.io/tags"
    params = {
        'sortBy': sort_by,
        'order': order,
    }
    response = requests.get(url, params=params)
    return response.json()