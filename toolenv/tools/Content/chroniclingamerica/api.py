import requests

def search_titles(terms: str, format: str = 'html', page: int = 1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search the directory of newspaper titles using OpenSearch.
    """
    url = f"https://chroniclingamerica.loc.gov/search/titles/results/"
    params = {
        'terms': terms,
        'format': format,
        'page': page
    }
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_pages(andtext: str, format: str = 'html', page: int = 1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search digitized newspaper pages using OpenSearch.
    """
    url = f"https://chroniclingamerica.loc.gov/search/pages/results/"
    params = {
        'andtext': andtext,
        'format': format,
        'page': page
    }
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def suggest_titles(q: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Auto Suggest API for looking up newspaper titles.
    """
    url = f"https://chroniclingamerica.loc.gov/suggest/titles/"
    params = {'q': q}
    
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
