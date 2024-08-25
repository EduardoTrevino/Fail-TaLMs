import requests
from typing import Optional, Dict


def fetch_random_joke(accept: str = "application/json", user_agent: str = "My Library (https://github.com/username/repo)", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Fetch a random dad joke in the specified format.
    Parameters:
        accept: str - The format to accept the joke in. Options are 'application/json', 'text/plain', or 'text/html'.
        user_agent: str - Custom User-Agent header to include in the request.
    """
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": accept,
        "User-Agent": user_agent
    }
    
    response = requests.get(url, headers=headers)
    try:
        return response.json() if accept == "application/json" else {"joke": response.text, "status": response.status_code}
    except Exception as e:
        return {"error": str(e), "response": response.text}


def fetch_random_slack_joke(user_agent: str = "My Library (https://github.com/username/repo)", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Fetch a random dad joke formatted for Slack.
    Parameters:
        user_agent: str - Custom User-Agent header to include in the request.
    """
    url = "https://icanhazdadjoke.com/slack"
    headers = {
        "User-Agent": user_agent
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def fetch_joke_by_id(joke_id: str, accept: str = "application/json", user_agent: str = "My Library (https://github.com/username/repo)", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Fetch a specific dad joke by its ID.
    Parameters:
        joke_id: str - The ID of the joke to fetch.
        accept: str - The format to accept the joke in. Options are 'application/json' or 'text/plain'.
        user_agent: str - Custom User-Agent header to include in the request.
    """
    url = f"https://icanhazdadjoke.com/j/{joke_id}"
    headers = {
        "Accept": accept,
        "User-Agent": user_agent
    }
    
    response = requests.get(url, headers=headers)
    try:
        return response.json() if accept == "application/json" else {"joke": response.text, "status": response.status_code}
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_jokes(term: Optional[str] = None, page: int = 1, limit: int = 20, user_agent: str = "My Library (https://github.com/username/repo)", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Search for dad jokes.
    Parameters:
        term: Optional[str] - Search term to use.
        page: int - Page of results to fetch.
        limit: int - Number of results to return per page.
        user_agent: str - Custom User-Agent header to include in the request.
    """
    url = "https://icanhazdadjoke.com/search"
    params = {
        "page": page,
        "limit": limit,
    }
    if term:
        params["term"] = term

    headers = {
        "Accept": "application/json",
        "User-Agent": user_agent
    }
    
    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}