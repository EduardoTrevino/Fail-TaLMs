import requests
import json
from typing import Optional, Dict, Union, List

def pageviews_per_article(project: str, access: str, agent: str, article: str, granularity: str, start: str, end: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get number of page views for a given article.
    """
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/{access}/{agent}/{article}/{granularity}/{start}/{end}"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_viewed_pages(project: str, access: str, year: str, month: str, day: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List the most viewed pages for a specific project and access type.
    """
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/top/{project}/{access}/{year}/{month}/{day}"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
