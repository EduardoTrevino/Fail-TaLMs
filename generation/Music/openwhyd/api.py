import requests
from typing import Optional, List, Dict, Union

BASE_URL = "https://openwhyd.org"


def get_user_tracks(uHandle: str, playlistId: Optional[int] = None, format: str = "json", 
                    limit: Optional[int] = 20, after: Optional[str] = None, 
                    before: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the list of tracks posted by a user.
    """
    path = f"/{uHandle}/playlist/{playlistId}" if playlistId else f"/{uHandle}"
    params = {
        "format": format,
        "limit": limit,
        "after": after,
        "before": before
    }
    response = requests.get(f"{BASE_URL}{path}", params=params)
    return response.json()


def get_hot_tracks(format: str = "json", limit: Optional[int] = 20, skip: Optional[int] = 0, 
                   toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the list of hot tracks.
    """
    params = {
        "format": format,
        "limit": limit,
        "skip": skip
    }
    response = requests.get(f"{BASE_URL}/hot", params=params)
    return response.json()


def get_user_data(id: Optional[str] = None, isSubscr: Optional[bool] = False, 
                  countPosts: Optional[bool] = False, countLikes: Optional[bool] = False, 
                  includeSubscr: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve user data.
    """
    params = {
        "id": id,
        "isSubscr": isSubscr,
        "countPosts": countPosts,
        "countLikes": countLikes,
        "includeSubscr": includeSubscr
    }
    response = requests.get(f"{BASE_URL}/api/user", params=params)
    return response.json()


def get_playlist_data(id: Union[str, List[str]], toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve playlist data.
    """
    if isinstance(id, list):
        id = "&id=".join(id)
    response = requests.get(f"{BASE_URL}/api/playlist", params={"id": id})
    return response.json()


def list_followers(id: str, skip: Optional[int] = 0, limit: Optional[int] = 50, 
                   isSubscr: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the list of subscribers of a user.
    """
    params = {
        "skip": skip,
        "limit": limit,
        "isSubscr": isSubscr
    }
    response = requests.get(f"{BASE_URL}/api/follow/fetchFollowers/{id}", params=params)
    return response.json()


def list_following(id: str, skip: Optional[int] = 0, limit: Optional[int] = 50, 
                   isSubscr: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the list of users a user subscribes to.
    """
    params = {
        "skip": skip,
        "limit": limit,
        "isSubscr": isSubscr
    }
    response = requests.get(f"{BASE_URL}/api/follow/fetchFollowing/{id}", params=params)
    return response.json()