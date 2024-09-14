import requests
from typing import Optional, List, Dict

def get_metadata(item_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve metadata for an Archive.org item.

    Parameters:
    item_id (str): The identifier for the Archive.org item for which you want metadata.
    """
    url = f"https://archive.org/metadata/{item_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_items(query: str, fields: Optional[str] = 'title', sorts: Optional[str] = None, count: Optional[int] = 100, 
                 cursor: Optional[str] = None, total_only: Optional[bool] = False,
                 toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Search items in Archive.org using the scraping API.

    Parameters:
    query (str): The query string in Lucene-like syntax.
    fields (str): Metadata fields to return, comma-delimited.
    sorts (str): Fields to sort on, comma-delimited.
    count (int): Number of results to return.
    cursor (str): A cursor, if any, for paginated results.
    total_only (bool): If set to true, only returns the number of results.
    """
    url = "https://archive.org/services/search/v1/scrape"
    params = {
        'q': query,
        'fields': fields,
        'count': count,
        'total_only': total_only
    }
    if sorts:
        params['sorts'] = sorts
    if cursor:
        params['cursor'] = cursor

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}