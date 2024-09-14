import requests
from typing import Optional, Dict, Any, List

def get_agency_details(toptier_agency_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Fetches the agency overview information for a specific agency.

    :param toptier_agency_code: The top-tier agency code to fetch data for.
    :param toolbench_rapidapi_key: The API key.
    :return: JSON response containing the agency details.
    """
    url = f"https://api.usaspending.gov/api/v2/agency/{toptier_agency_code}/"
    response = requests.get(url)
    return response.json()

def get_agency_awards_summary(toptier_agency_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Fetches agency summary information like number of transactions and award obligations.

    :param toptier_agency_code: The top-tier agency code to fetch data for.
    :param toolbench_rapidapi_key: The API key.
    :return: JSON response containing agency award summary.
    """
    url = f"https://api.usaspending.gov/api/v2/agency/{toptier_agency_code}/awards/"
    response = requests.get(url)
    return response.json()

def get_award_details(award_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Returns details about a specific award.

    :param award_id: The ID of the award.
    :param toolbench_rapidapi_key: The API key.
    :return: JSON response containing award details.
    """
    url = f"https://api.usaspending.gov/api/v2/awards/{award_id}/"
    response = requests.get(url)
    return response.json()

def search_spending_by_award(filters: Dict[str, Any], fields: List[str], sort: str, order: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Searches awards data using advanced filters and returns the search results.

    :param filters: Dictionary containing the filters for the search query.
    :param fields: List of fields to return in the search result.
    :param sort: Field to sort by.
    :param order: Sort order, either 'asc' or 'desc'.
    :param toolbench_rapidapi_key: The API key.
    :return: JSON response containing the search results.
    """
    url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
    payload = {
        "filters": filters,
        "fields": fields,
        "sort": sort,
        "order": order
    }
    response = requests.post(url, json=payload)
    return response.json()