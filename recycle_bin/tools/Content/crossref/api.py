import requests

BASE_URL = "https://api.crossref.org"

def get_work_metadata(doi: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve metadata for a specific work identified by DOI.
    """
    url = f"{BASE_URL}/works/{doi}"
    response = requests.get(url)
    try:
        data = response.json()
    except:
        data = response.text
    return data

def search_works(query: str, rows: int = 20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for works based on a query.
    """
    url = f"{BASE_URL}/works"
    params = {
        "query": query,
        "rows": rows
    }
    response = requests.get(url, params=params)
    try:
        data = response.json()
    except:
        data = response.text
    return data
