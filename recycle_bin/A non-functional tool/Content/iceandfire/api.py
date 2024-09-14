import requests
from typing import Optional, List, Dict


def get_books(page: Optional[int] = 1, page_size: Optional[int] = 10, name: Optional[str] = None, from_release_date: Optional[str] = None, to_release_date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: List all books with optional filters.
    """
    url = "https://www.anapioficeandfire.com/api/books"
    params = {
        'page': page,
        'pageSize': page_size,
        'name': name,
        'fromReleaseDate': from_release_date,
        'toReleaseDate': to_release_date
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_book(book_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get specific book by ID.
    """
    url = f"https://www.anapioficeandfire.com/api/books/{book_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_characters(page: Optional[int] = 1, page_size: Optional[int] = 10, name: Optional[str] = None, gender: Optional[str] = None, culture: Optional[str] = None, born: Optional[str] = None, died: Optional[str] = None, is_alive: Optional[bool] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: List all characters with optional filters.
    """
    url = "https://www.anapioficeandfire.com/api/characters"
    params = {
        'page': page,
        'pageSize': page_size,
        'name': name,
        'gender': gender,
        'culture': culture,
        'born': born,
        'died': died,
        'isAlive': is_alive
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_character(character_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get specific character by ID.
    """
    url = f"https://www.anapioficeandfire.com/api/characters/{character_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_houses(page: Optional[int] = 1, page_size: Optional[int] = 10, name: Optional[str] = None, region: Optional[str] = None, words: Optional[str] = None, has_words: Optional[bool] = None, has_titles: Optional[bool] = None, has_seats: Optional[bool] = None, has_died_out: Optional[bool] = None, has_ancestral_weapons: Optional[bool] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: List all houses with optional filters.
    """
    url = "https://www.anapioficeandfire.com/api/houses"
    params = {
        'page': page,
        'pageSize': page_size,
        'name': name,
        'region': region,
        'words': words,
        'hasWords': has_words,
        'hasTitles': has_titles,
        'hasSeats': has_seats,
        'hasDiedOut': has_died_out,
        'hasAncestralWeapons': has_ancestral_weapons
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_house(house_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get specific house by ID.
    """
    url = f"https://www.anapioficeandfire.com/api/houses/{house_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}