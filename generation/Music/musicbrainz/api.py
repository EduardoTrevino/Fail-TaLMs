import requests
from typing import Optional

BASE_URL = "https://musicbrainz.org/ws/2/"
HEADERS = {'User-Agent': 'MyMusicApp/1.0'}

def artist_search(query: str, limit: Optional[int] = 25, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for artists by name.
    Parameters:
    query (str): The search query for the artist name.
    limit (Optional[int]): The maximum number of results to return (default 25).
    offset (Optional[int]): The number of results to skip (default 0).
    """
    url = f"{BASE_URL}artist"
    params = {
        'query': query,
        'limit': limit,
        'offset': offset,
        'fmt': 'json'
    }
    response = requests.get(url, headers=HEADERS, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def release_lookup(mbid: str, inc: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Lookup a release by its MBID.
    Parameters:
    mbid (str): The MusicBrainz Identifier for the release.
    inc (Optional[str]): Include additional information, such as artists or recordings (separated by +).
    """
    url = f"{BASE_URL}release/{mbid}"
    params = {
        'fmt': 'json'
    }
    if inc:
        params['inc'] = inc

    response = requests.get(url, headers=HEADERS, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def release_group_browse(artist_mbid: str, limit: Optional[int] = 25, offset: Optional[int] = 0, type: Optional[str] = None, status: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Browse release groups for a given artist MBID.
    Parameters:
    artist_mbid (str): The MBID for the artist.
    limit (Optional[int]): The maximum number of results to return (default 25).
    offset (Optional[int]): The number of results to skip (default 0).
    type (Optional[str]): Filter release groups by type (e.g., album, single).
    status (Optional[str]): Filter releases by status (e.g., official, promotion).
    """
    url = f"{BASE_URL}release-group"
    params = {
        'artist': artist_mbid,
        'limit': limit,
        'offset': offset,
        'fmt': 'json'
    }
    if type:
        params['type'] = type
    if status:
        params['status'] = status

    response = requests.get(url, headers=HEADERS, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}