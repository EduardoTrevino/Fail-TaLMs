import requests
from typing import Optional

# Define the base URL for the API
BASE_URL = 'https://wikimedia.org/api'

def get_category_metrics(category: str, start: str, end: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/commons-analytics/category-metrics-snapshot/{category}/{start}/{end}"
    response = requests.get(url)
    return response.json()

def get_edits_per_category(category: str, category_scope: str, edit_type: str, start: str, end: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/commons-analytics/edits-per-category-monthly/{category}/{category_scope}/{edit_type}/{start}/{end}"
    response = requests.get(url)
    return response.json()

def get_pageviews_per_category(category: str, category_scope: str, wiki: str, start: str, end: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/commons-analytics/pageviews-per-category-monthly/{category}/{category_scope}/{wiki}/{start}/{end}"
    response = requests.get(url)
    return response.json()

def get_top_edited_categories(category_scope: str, edit_type: str, year: int, month: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/commons-analytics/top-edited-categories-monthly/{category_scope}/{edit_type}/{year}/{month}"
    response = requests.get(url)
    return response.json()

def get_top_viewed_categories(category_scope: str, wiki: str, year: int, month: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/commons-analytics/top-viewed-categories-monthly/{category_scope}/{wiki}/{year}/{month}"
    response = requests.get(url)
    return response.json()

def get_top_pages_per_category(category: str, category_scope: str, wiki: str, year: int, month: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/commons-analytics/top-pages-per-category-monthly/{category}/{category_scope}/{wiki}/{year}/{month}"
    response = requests.get(url)
    return response.json()

def get_unique_devices(project: str, access_site: str, granularity: str, start: str, end: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/unique-devices/{project}/{access_site}/{granularity}/{start}/{end}"
    response = requests.get(url)
    return response.json()

def get_edits_aggregate(project: str, editor_type: str, page_type: str, granularity: str, start: str, end: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/edits/aggregate/{project}/{editor_type}/{page_type}/{granularity}/{start}/{end}"
    response = requests.get(url)
    return response.json()

def get_pageviews_aggregate(project: str, access: str, agent: str, granularity: str, start: str, end: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/pageviews/aggregate/{project}/{access}/{agent}/{granularity}/{start}/{end}"
    response = requests.get(url)
    return response.json()