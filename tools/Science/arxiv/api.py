import requests
from typing import Optional, List


def query_arxiv(search_query: Optional[str] = None, id_list: Optional[List[str]] = None,
                start: int = 0, max_results: int = 10, sort_by: Optional[str] = None, 
                sort_order: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Queries arXiv's API for articles matching given search parameters.
    
    Parameters:
        search_query: The search terms or aguments.
        id_list: A list of arXiv article IDs (comma separated if in string form).
        start: The 0-based index to start from.
        max_results: Number of results to retrieve.
        sort_by: How to sort the results ('relevance', 'lastUpdatedDate', 'submittedDate').
        sort_order: Order of sort ('ascending', 'descending').
    
    Returns:
        Atom XML of articles matching search criteria.
    """
    base_url = "http://export.arxiv.org/api/query"
    params = {
        'search_query': search_query if search_query else '',
        'id_list': ','.join(id_list) if id_list else '',
        'start': start,
        'max_results': max_results,
        'sortBy': sort_by,
        'sortOrder': sort_order
    }
    
    response = requests.get(base_url, params=params)
    return response.text  # Atom feed as text