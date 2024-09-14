import requests
from typing import Optional

def showsearch(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search through all the shows in the database by the show's name. A fuzzy algorithm is used to find shows even if the query contains small typos. Results are returned in order of relevancy and contain each show's full information.
    """
    url = f"https://api.tvmaze.com/search/shows"
    querystring = {'q': query}

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def showepisodes(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    A complete list of episodes for the given show. Episodes are returned in their airing order, and include full episode information. By default, specials are not included in the list.
    """
    url = f"https://api.tvmaze.com/shows/{id}/episodes"

    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
