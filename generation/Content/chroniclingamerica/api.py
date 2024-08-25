import requests
from typing import Optional

def search_titles(terms: str, format: Optional[str] = 'html', page: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search the newspaper directory using OpenSearch.
    
    :param terms: The search query term.
    :param format: Format of response. 'html' (default), 'json', or 'atom'.
    :param page: Page number for paging results.
    :return: Response from Chronicling America API.
    """
    url = "https://chroniclingamerica.loc.gov/search/titles/results/"
    params = {
        'terms': terms,
        'format': format
    }
    if page:
        params['page'] = page

    response = requests.get(url, params=params)
    return response.json() if format == 'json' else response.text


def search_pages(andtext: str, format: Optional[str] = 'html', page: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search newspaper pages using OpenSearch.
    
    :param andtext: The search query text.
    :param format: Format of response. 'html' (default), 'json', or 'atom'.
    :param page: Page number for paging results.
    :return: Response from Chronicling America API.
    """
    url = "https://chroniclingamerica.loc.gov/search/pages/results/"
    params = {
        'andtext': andtext,
        'format': format
    }
    if page:
        params['page'] = page

    response = requests.get(url, params=params)
    return response.json() if format == 'json' else response.text


def suggest_titles(q: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Auto Suggest API for looking up newspaper titles.
    
    :param q: Query string for title suggestions.
    :return: JSON response of suggestions from Chronicling America API.
    """
    url = "https://chroniclingamerica.loc.gov/suggest/titles/"
    params = {
        'q': q
    }

    response = requests.get(url, params=params)
    return response.json()  # response should be application/x-suggestions+json


def get_newspapers_json(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all newspaper titles for which there is digital content.
    
    :return: JSON response from Chronicling America API.
    """
    url = "https://chroniclingamerica.loc.gov/newspapers.json"
    response = requests.get(url)
    return response.json()


def get_all_batches_json(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all batches of content that have been loaded.
    
    :return: JSON response from Chronicling America API.
    """
    url = "https://chroniclingamerica.loc.gov/batches.json"
    response = requests.get(url)
    return response.json()


def get_specific_batch_json(batch_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get detailed information about a specific batch.
    
    :param batch_id: Identifier of the batch.
    :return: JSON response from Chronicling America API.
    """
    url = f"https://chroniclingamerica.loc.gov/batches/{batch_id}.json"
    response = requests.get(url)
    return response.json()


def get_awardees_json(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all NDNP Awardees as JSON.
    
    :return: JSON response from Chronicling America API.
    """
    url = "https://chroniclingamerica.loc.gov/awardees.json"
    response = requests.get(url)
    return response.json()


def get_specific_awardee_json(awardee_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get detailed information about a specific awardee.
    
    :param awardee_id: Identifier of the awardee.
    :return: JSON response from Chronicling America API.
    """
    url = f"https://chroniclingamerica.loc.gov/awardees/{awardee_id}.json"
    response = requests.get(url)
    return response.json()