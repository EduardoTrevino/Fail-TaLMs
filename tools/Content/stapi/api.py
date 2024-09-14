import requests
from typing import Optional, List, Dict, Any

BASE_URL = "https://stapi.co/api"


def get_animal(uid: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve a single animal.
    
    Parameters:
    - uid: str - Animal unique ID
    """
    url = f"{BASE_URL}/v1/rest/animal"
    params = {'uid': uid}
    
    response = requests.get(url, params=params)
    return response.json()


def search_animals(page_number: Optional[int] = 0, page_size: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Pagination over animals.
    
    Parameters:
    - page_number: int (optional) - Zero-based page number
    - page_size: int (optional) - Page size
    """
    url = f"{BASE_URL}/v1/rest/animal/search"
    params = {
        'pageNumber': page_number,
        'pageSize': page_size
    }
    
    response = requests.get(url, params=params)
    return response.json()


def search_astronomical_objects(page_number: Optional[int] = 0, page_size: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Pagination over astronomical objects (V2).
    
    Parameters:
    - page_number: int (optional) - Zero-based page number
    - page_size: int (optional) - Page size
    """
    url = f"{BASE_URL}/v2/rest/astronomicalObject/search"
    params = {
        'pageNumber': page_number,
        'pageSize': page_size
    }
    
    response = requests.get(url, params=params)
    return response.json()


def get_book(uid: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve a single book (V2).

    Parameters:
    - uid: str - Book unique ID
    """
    url = f"{BASE_URL}/v2/rest/book"
    params = {'uid': uid}
    
    response = requests.get(url, params=params)
    return response.json()


def search_books(page_number: Optional[int] = 0, page_size: Optional[int] = 10, sort: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Pagination over books (V2).

    Parameters:
    - page_number: int (optional) - Zero-based page number
    - page_size: int (optional) - Page size
    - sort: str (optional) - Sorting format like 'fieldName,ASC;anotherFieldName,DESC'
    """
    url = f"{BASE_URL}/v2/rest/book/search"
    params = {'pageNumber': page_number, 'pageSize': page_size}
    
    if sort:
        params['sort'] = sort

    response = requests.get(url, params=params)
    return response.json()


def get_character(uid: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve a single character.
    
    Parameters:
    - uid: str - Character unique ID
    """
    url = f"{BASE_URL}/v1/rest/character"
    params = {'uid': uid}
    
    response = requests.get(url, params=params)
    return response.json()


def search_characters(page_number: Optional[int] = 0, page_size: Optional[int] = 10, sort: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Pagination over characters.

    Parameters:
    - page_number: int (optional) - Zero-based page number
    - page_size: int (optional) - Page size
    - sort: str (optional) - Sorting format like 'fieldName,ASC;anotherFieldName,DESC'
    """
    url = f"{BASE_URL}/v1/rest/character/search"
    params = {'pageNumber': page_number, 'pageSize': page_size}
    
    if sort:
        params['sort'] = sort

    response = requests.get(url, params=params)
    return response.json()


def get_data_version(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve the data version of the STAPI instance.
    """
    url = f"{BASE_URL}/v1/rest/common/dataVersion"
    
    response = requests.get(url)
    return response.json()


def get_episode(uid: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Retrieve a single episode.
    
    Parameters:
    - uid: str - Episode unique ID
    """
    url = f"{BASE_URL}/v1/rest/episode"
    params = {'uid': uid}
    
    response = requests.get(url, params=params)
    return response.json()


def search_episodes(page_number: Optional[int] = 0, page_size: Optional[int] = 10, sort: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Pagination over episodes.

    Parameters:
    - page_number: int (optional) - Zero-based page number
    - page_size: int (optional) - Page size
    - sort: str (optional) - Sorting format like 'fieldName,ASC;anotherFieldName,DESC'
    """
    url = f"{BASE_URL}/v1/rest/episode/search"
    params = {'pageNumber': page_number, 'pageSize': page_size}
    
    if sort:
        params['sort'] = sort

    response = requests.get(url, params=params)
    return response.json()