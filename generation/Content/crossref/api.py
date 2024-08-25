import requests
from typing import Optional

def search_works(query: str, rows: Optional[int] = 20, sort: Optional[str] = None, order: Optional[str] = 'desc', mailto: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for works by a free text query.

    Args:
        query: The query string to search for within the works.
        rows: The number of rows to return per page.
        sort: The field to sort results by.
        order: The order of results, either ascending ('asc') or descending ('desc').
        mailto: The email address used to identify requests in the polite pool.

    Returns:
        JSON response with details of the works.
    """
    url = "https://api.crossref.org/works"
    params = {
        'query': query,
        'rows': rows,
        'sort': sort,
        'order': order,
        'mailto': mailto
    }
    response = requests.get(url, params=params)
    return response.json()

def get_funders(query: Optional[str] = None, filter: Optional[str] = None, rows: Optional[int] = 20, mailto: Optional[str] = None, offset: Optional[int] = 0, toolbench_rapidapi_key: str ='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of funders.

    Args:
        query: Free text query for funders.
        filter: Filters for searching funders by specific criteria.
        rows: Number of results per page.
        mailto: Email address to identify requests in the polite pool.
        offset: Number of rows to skip before returning results.

    Returns:
        JSON response with details of the funders.
    """
    url = "https://api.crossref.org/funders"
    params = {
        'query': query,
        'filter': filter,
        'rows': rows,
        'mailto': mailto,
        'offset': offset
    }
    response = requests.get(url, params=params)
    return response.json()

def get_funder_details(funder_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve metadata for a specific funder and their suborganizations by funder ID.

    Args:
        funder_id: The ID of the funder.

    Returns:
        JSON response with details of the funder.
    """
    url = f"https://api.crossref.org/funders/{funder_id}"
    response = requests.get(url)
    return response.json()

def list_journals(query: Optional[str] = None, rows: Optional[int] = 20, mailto: Optional[str] = None, offset: Optional[int] = 0, sort: Optional[str] = None, order: Optional[str] = 'desc', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List journals based on a query.

    Args:
        query: Free text query for journals.
        rows: Number of results per page.
        mailto: Email address to identify requests in the polite pool.
        offset: Number of rows to skip before returning results.
        sort: The field to sort results by.
        order: The order of results, either ascending ('asc') or descending ('desc').

    Returns:
        JSON response with details of the journals.
    """
    url = "https://api.crossref.org/journals"
    params = {
        'query': query,
        'rows': rows,
        'mailto': mailto,
        'offset': offset,
        'sort': sort,
        'order': order
    }
    response = requests.get(url, params=params)
    return response.json()

def get_journal_details(issn: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a journal by its ISSN.

    Args:
        issn: The ISSN identifier associated with the journal.

    Returns:
        JSON response with details of the journal.
    """
    url = f"https://api.crossref.org/journals/{issn}"
    response = requests.get(url)
    return response.json()

def get_works_by_journal(issn: str, query: Optional[str] = None, rows: Optional[int] = 20, sort: Optional[str] = None, order: Optional[str] = 'desc', mailto: Optional[str] = None, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of works in a journal identified by ISSN.

    Args:
        issn: The ISSN identifier of the journal.
        query: Free text query for works.
        rows: Number of results per page.
        sort: The field to sort results by.
        order: The order of results, either ascending ('asc') or descending ('desc').
        mailto: Email address to identify requests in the polite pool.
        offset: Number of rows to skip before returning results.

    Returns:
        JSON response with details of the works in the journal.
    """
    url = f"https://api.crossref.org/journals/{issn}/works"
    params = {
        'query': query,
        'rows': rows,
        'sort': sort,
        'order': order,
        'mailto': mailto,
        'offset': offset
    }
    response = requests.get(url, params=params)
    return response.json()