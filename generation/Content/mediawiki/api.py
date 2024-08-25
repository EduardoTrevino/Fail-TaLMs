import requests
from typing import Optional


def parse_page(page: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', wiki: str = "https://en.wikipedia.org/w/api.php"):
    """
    Parses a given page from the specified wiki and returns its content in JSON format.
    Parameters:
    page [Required]: The title of the page to parse.
    wiki [Optional]: The wiki endpoint to use. Defaults to English Wikipedia.
    """
    url = wiki
    params = {
        'action': 'parse',
        'page': page,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_open_search(query: str, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', wiki: str = "https://en.wikipedia.org/w/api.php"):
    """
    Uses the OpenSearch protocol to search for the given query in the specified wiki.
    Parameters:
    query [Required]: The search query.
    limit [Optional]: The number of results to return. Defaults to 10.
    wiki [Optional]: The wiki endpoint to use. Defaults to English Wikipedia.
    """
    url = wiki
    params = {
        'action': 'opensearch',
        'search': query,
        'limit': limit,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_sitematrix(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of all Wikimedia sites.
    """
    url = "https://www.mediawiki.org/w/api.php"
    params = {
        'action': 'sitematrix',
        'format': 'json'
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}