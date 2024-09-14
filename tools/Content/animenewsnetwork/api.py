import requests
from typing import Optional


def get_reports(nskip: Optional[int] = 0, nlist: Optional[str] = '50', type: Optional[str] = None, name: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch reports with optional filtering by type and name.
    Parameters:
        nskip [Optional]: The number of entries to skip.
        nlist [Optional]: The number of entries to list. Can be a number or 'all'.
        type [Optional]: Filter the list by 'anime' or 'manga'.
        name [Optional]: Filter by entries whose main title starts with this value.
    """
    url = "https://cdn.animenewsnetwork.com/encyclopedia/reports.xml"
    params = {
        'nskip': nskip,
        'nlist': nlist
    }
    if type:
        params['type'] = type
    if name:
        params['name'] = name
    
    response = requests.get(url, params=params)
    return response.content


def get_anime_details(id: Optional[str] = None, anime: Optional[str] = None, manga: Optional[str] = None, title: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch detailed information for anime/manga titles by ID or name.
    Parameters:
        id [Optional]: Fetch details using anime/manga/title ID.
        anime [Optional]: Fetch details when id is an anime ID.
        manga [Optional]: Fetch details when id is a manga ID.
        title [Optional]: Fetch details by name or ID (slash-separated list).
    """
    url = "https://cdn.animenewsnetwork.com/encyclopedia/api.xml"
    params = {}
    if id:
        params['id'] = id
    if anime:
        params['anime'] = anime
    if manga:
        params['manga'] = manga
    if title:
        params['title'] = title
    
    response = requests.get(url, params=params)
    return response.content