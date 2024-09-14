import requests
from typing import Optional

def search_shows(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for shows by name. A fuzzy search is used to find the shows matching the given query.

    Parameters:
    - query: The name of the show to search for.

    Returns:
    JSON response containing a list of shows matching the query.
    """
    url = "https://api.tvmaze.com/search/shows"
    params = {
        'q': query
    }
    response = requests.get(url, params=params)
    return response.json()

def show_single_search(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Perform a single search for a specific show by name.

    Parameters:
    - query: The name of the show.

    Returns:
    JSON response with the single show's details, or no result if not found.
    """
    url = "https://api.tvmaze.com/singlesearch/shows"
    params = {
        'q': query
    }
    response = requests.get(url, params=params)
    return response.json()

def show_lookup(the_tvdb_id: Optional[int] = None, imdb_id: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Lookup a show by its thetvdb or IMDB ID.

    Parameters:
    - the_tvdb_id: The TVDB ID of the show.
    - imdb_id: The IMDB ID of the show.

    Returns:
    JSON response with the show's details, or a 404 if not found.
    """
    if the_tvdb_id:
        url = f"https://api.tvmaze.com/lookup/shows?thetvdb={the_tvdb_id}"
    elif imdb_id:
        url = f"https://api.tvmaze.com/lookup/shows?imdb={imdb_id}"
    else:
        raise ValueError("Either the_tvdb_id or imdb_id must be provided.")

    response = requests.get(url)
    return response.json()

def search_people(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for people by name.

    Parameters:
    - query: The name of the person to search for.

    Returns:
    JSON response containing a list of people matching the query.
    """
    url = "https://api.tvmaze.com/search/people"
    params = {
        'q': query
    }
    response = requests.get(url, params=params)
    return response.json()

def schedule(country: Optional[str] = 'US', date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the schedule for a given country and date.

    Parameters:
    - country: An ISO 3166-1 code of the country; defaults to 'US'
    - date: An ISO 8601 formatted date; defaults to the current day

    Returns:
    JSON response with the schedule information.
    """
    url = "https://api.tvmaze.com/schedule"
    params = {
        'country': country,
        'date': date
    }
    response = requests.get(url, params=params)
    return response.json()

def web_schedule(country: Optional[str] = None, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the web/streaming schedule for a given country and date.

    Parameters:
    - country: An ISO 3166-1 code of the country
    - date: An ISO 8601 formatted date; defaults to the current day

    Returns:
    JSON response with the web schedule information.
    """
    url = "https://api.tvmaze.com/schedule/web"
    params = {
        'country': country,
        'date': date
    }
    response = requests.get(url, params=params)
    return response.json()

def show_main_information(show_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all primary information for a given show.

    Parameters:
    - show_id: The TVmaze ID of the show.

    Returns:
    JSON response with the show's main information.
    """
    url = f"https://api.tvmaze.com/shows/{show_id}"
    response = requests.get(url)
    return response.json()

def show_episode_list(show_id: int, specials: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a complete list of episodes for the given show.

    Parameters:
    - show_id: The TVmaze ID of the show.
    - specials: Include specials in the list.

    Returns:
    JSON response containing a list of episodes.
    """
    url = f"https://api.tvmaze.com/shows/{show_id}/episodes"
    params = {
        'specials': specials
    }
    response = requests.get(url, params=params)
    return response.json()

def show_seasons(show_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a complete list of seasons for the given show.

    Parameters:
    - show_id: The TVmaze ID of the show.

    Returns:
    JSON response containing a list of seasons.
    """
    url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    response = requests.get(url)
    return response.json()

def season_episodes(season_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of episodes for a specific season.

    Parameters:
    - season_id: The TVmaze ID of the season.

    Returns:
    JSON response containing a list of episodes in the season.
    """
    url = f"https://api.tvmaze.com/seasons/{season_id}/episodes"
    response = requests.get(url)
    return response.json()

def person_main_information(person_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all primary information for a given person.

    Parameters:
    - person_id: The TVmaze ID of the person.

    Returns:
    JSON response containing the person's information.
    """
    url = f"https://api.tvmaze.com/people/{person_id}"
    response = requests.get(url)
    return response.json()

def person_cast_credits(person_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all cast credits for a given person.

    Parameters:
    - person_id: The TVmaze ID of the person.

    Returns:
    JSON response containing the person's cast credits.
    """
    url = f"https://api.tvmaze.com/people/{person_id}/castcredits"
    response = requests.get(url)
    return response.json()

def person_crew_credits(person_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all crew credits for a given person.

    Parameters:
    - person_id: The TVmaze ID of the person.

    Returns:
    JSON response containing the person's crew credits.
    """
    url = f"https://api.tvmaze.com/people/{person_id}/crewcredits"
    response = requests.get(url)
    return response.json()

def updates_shows(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve updates on all shows in the TVmaze database.

    Returns:
    JSON response containing updates on all shows.
    """
    url = "https://api.tvmaze.com/updates/shows"
    response = requests.get(url)
    return response.json()

def updates_people(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve updates on all people in the TVmaze database.

    Returns:
    JSON response containing updates on all people.
    """
    url = "https://api.tvmaze.com/updates/people"
    response = requests.get(url)
    return response.json()