import requests
from typing import Optional

BASE_URL = "https://hacker-news.firebaseio.com/v0"
TOOLBENCH_RAPIDAPI_KEY = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'


def get_item(item_id: int, toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get a specific item by ID.
    Parameters:
        item_id [Required]: integer - The item's unique ID.
    """
    url = f"{BASE_URL}/item/{item_id}.json"
    response = requests.get(url)
    return response.json()


def get_user(user_id: str, toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get a specific user by ID.
    Parameters:
        user_id [Required]: string - The user's unique username (case-sensitive).
    """
    url = f"{BASE_URL}/user/{user_id}.json"
    response = requests.get(url)
    return response.json()


def get_max_item(toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get the current largest item ID.
    """
    url = f"{BASE_URL}/maxitem.json"
    response = requests.get(url)
    return response.json()


def get_top_stories(toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get up to 500 of the top stories.
    """
    url = f"{BASE_URL}/topstories.json"
    response = requests.get(url)
    return response.json()


def get_new_stories(toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get up to 500 of the newest stories.
    """
    url = f"{BASE_URL}/newstories.json"
    response = requests.get(url)
    return response.json()


def get_best_stories(toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get up to 500 of the best stories.
    """
    url = f"{BASE_URL}/beststories.json"
    response = requests.get(url)
    return response.json()


def get_ask_stories(toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get up to 200 of the latest Ask HN stories.
    """
    url = f"{BASE_URL}/askstories.json"
    response = requests.get(url)
    return response.json()


def get_show_stories(toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get up to 200 of the latest Show HN stories.
    """
    url = f"{BASE_URL}/showstories.json"
    response = requests.get(url)
    return response.json()


def get_job_stories(toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get up to 200 of the latest Job stories.
    """
    url = f"{BASE_URL}/jobstories.json"
    response = requests.get(url)
    return response.json()


def get_updates(toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY):
    """
    Get changed items and profiles.
    """
    url = f"{BASE_URL}/updates.json"
    response = requests.get(url)
    return response.json()