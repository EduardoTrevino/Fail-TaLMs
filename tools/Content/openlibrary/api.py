import requests
from typing import Optional

def openlibrary_search(q: str, fields: Optional[str] = "*", sort: Optional[str] = None, page: Optional[int] = 1, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    OpenLibrary Search API - Search for books by title, author, and other criteria.
    
    Parameters:
    - q: The query term for the search.
    - fields: Fields to include in the response. Use '*' to include all fields.
    - sort: Sorting order (e.g., 'new', 'old', 'random', etc.).
    - page: Page number for results pagination.
    - limit: Number of results per page.
    """
    url = "https://openlibrary.org/search.json"
    params = {
        'q': q,
        'fields': fields,
        'sort': sort,
        'page': page,
        'limit': limit
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def works_by_id(work_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a work using its Open Library work ID.
    
    Parameters:
    - work_id: The Open Library ID of the work.
    """
    url = f"https://openlibrary.org/works/{work_id}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def editions_by_work(work_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch editions of a work using its Open Library work ID.
    
    Parameters:
    - work_id: The Open Library ID of the work.
    """
    url = f"https://openlibrary.org/works/{work_id}/editions.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def author_search(q: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for authors by name.
    
    Parameters:
    - q: The query term to search for authors.
    """
    url = "https://openlibrary.org/search/authors.json"
    params = {
        'q': q
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def author_data(author_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve data about an author using their Open Library ID.
    
    Parameters:
    - author_id: The ID of the author.
    """
    url = f"https://openlibrary.org/authors/{author_id}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def author_works(author_id: str, limit: Optional[int] = 50, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch works by a specific author using their Open Library author ID.
    
    Parameters:
    - author_id: The Open Library ID of the author.
    - limit: Number of works to return.
    - offset: The starting point in the collection of works. 
    """
    url = f"https://openlibrary.org/authors/{author_id}/works.json"
    params = {
        'limit': limit,
        'offset': offset
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def book_by_isbn(isbn: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve book information using its ISBN.
    
    Parameters:
    - isbn: The ISBN of the book (either ISBN-10 or ISBN-13).
    """
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}