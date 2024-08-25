import requests
from typing import Optional

BASE_URL = "https://api.jikan.moe/v4"


def get_anime_full_by_id(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get complete anime resource data by ID."""
    url = f"{BASE_URL}/anime/{id}/full"
    response = requests.get(url)
    return response.json()


def get_anime_by_id(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get anime resource by ID."""
    url = f"{BASE_URL}/anime/{id}"
    response = requests.get(url)
    return response.json()


def get_anime_characters(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get characters of a specific anime."""
    url = f"{BASE_URL}/anime/{id}/characters"
    response = requests.get(url)
    return response.json()


def get_anime_staff(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get staff information for a specific anime."""
    url = f"{BASE_URL}/anime/{id}/staff"
    response = requests.get(url)
    return response.json()


def get_anime_episodes(id: int, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get episodes of a specific anime."""
    url = f"{BASE_URL}/anime/{id}/episodes"
    response = requests.get(url, params={"page": page})
    return response.json()


def get_anime_episode_by_id(id: int, episode: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get a specific episode by ID and episode number."""
    url = f"{BASE_URL}/anime/{id}/episodes/{episode}"
    response = requests.get(url)
    return response.json()


def get_anime_news(id: int, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get news related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/news"
    response = requests.get(url, params={"page": page})
    return response.json()


def get_anime_forum(id: int, filter: Optional[str] = "all", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get forum topics related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/forum"
    response = requests.get(url, params={"filter": filter})
    return response.json()


def get_anime_videos(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get videos related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/videos"
    response = requests.get(url)
    return response.json()


def get_anime_videos_episodes(id: int, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get episode videos related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/videos/episodes"
    response = requests.get(url, params={"page": page})
    return response.json()


def get_anime_pictures(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get pictures related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/pictures"
    response = requests.get(url)
    return response.json()


def get_anime_statistics(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get statistics of a specific anime."""
    url = f"{BASE_URL}/anime/{id}/statistics"
    response = requests.get(url)
    return response.json()


def get_anime_more_info(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get more information about a specific anime."""
    url = f"{BASE_URL}/anime/{id}/moreinfo"
    response = requests.get(url)
    return response.json()


def get_anime_recommendations(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get recommendations related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/recommendations"
    response = requests.get(url)
    return response.json()


def get_anime_user_updates(id: int, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get user updates related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/userupdates"
    response = requests.get(url, params={"page": page})
    return response.json()


def get_anime_reviews(id: int, page: Optional[int] = 1, preliminary: Optional[bool] = False, spoilers: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get reviews related to a specific anime."""
    params = {"page": page, "preliminary": preliminary, "spoilers": spoilers}
    url = f"{BASE_URL}/anime/{id}/reviews"
    response = requests.get(url, params=params)
    return response.json()


def get_anime_relations(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get relations of a specific anime."""
    url = f"{BASE_URL}/anime/{id}/relations"
    response = requests.get(url)
    return response.json()


def get_anime_themes(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get themes related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/themes"
    response = requests.get(url)
    return response.json()


def get_anime_external(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get external links related to a specific anime."""
    url = f"{BASE_URL}/anime/{id}/external"
    response = requests.get(url)
    return response.json()


def get_anime_streaming(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get streaming links of a specific anime."""
    url = f"{BASE_URL}/anime/{id}/streaming"
    response = requests.get(url)
    return response.json()


def get_anime_search(q: Optional[str] = None, page: Optional[int] = 1, sfw: Optional[bool] = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Search anime."""
    params = {"q": q, "page": page, "sfw": sfw}
    url = f"{BASE_URL}/anime"
    response = requests.get(url, params=params)
    return response.json()


def get_character_full_by_id(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get full character resource data by ID."""
    url = f"{BASE_URL}/characters/{id}/full"
    response = requests.get(url)
    return response.json()


def get_character_by_id(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get character resource by ID."""
    url = f"{BASE_URL}/characters/{id}"
    response = requests.get(url)
    return response.json()


def get_character_anime(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get anime associated with a specific character."""
    url = f"{BASE_URL}/characters/{id}/anime"
    response = requests.get(url)
    return response.json()


def get_character_manga(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get manga associated with a specific character."""
    url = f"{BASE_URL}/characters/{id}/manga"
    response = requests.get(url)
    return response.json()


def get_character_voice_actors(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get voice actors for a specific character."""
    url = f"{BASE_URL}/characters/{id}/voices"
    response = requests.get(url)
    return response.json()


def get_character_pictures(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Get pictures related to a specific character."""
    url = f"{BASE_URL}/characters/{id}/pictures"
    response = requests.get(url)
    return response.json()


def get_characters_search(q: Optional[str] = None, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Search characters."""
    params = {"q": q, "page": page}
    url = f"{BASE_URL}/characters"
    response = requests.get(url, params=params)
    return response.json()

# Similar functions can be created for manga, people, clubs, genres, etc., following the provided pattern.