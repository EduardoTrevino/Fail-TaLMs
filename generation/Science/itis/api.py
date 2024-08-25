import requests
from typing import Optional, Any, Dict

BASE_URL = "http://www.itis.gov/ITISWebService/services/ITISService/"

def search_for_any_match(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Returns matches found by comparing the search key to the ITIS common names, scientific names, and TSNs.
    """
    url = f"{BASE_URL}searchForAnyMatch"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return response.json()

def search_for_any_match_paged(srch_key: str, page_size: int = 100, page_num: int = 1, ascend: bool = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Returns paginated matches found by comparing the search key to the ITIS common names, scientific names, and TSNs.
    """
    url = f"{BASE_URL}searchForAnyMatchPaged"
    params = {
        'srchKey': srch_key,
        'pageSize': page_size,
        'pageNum': page_num,
        'ascend': 'true' if ascend else 'false'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_any_match_count(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> int:
    """
    Returns a count of matches found by comparing the search key to the ITIS common names, scientific names, and TSNs.
    """
    url = f"{BASE_URL}getAnyMatchCount"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return int(response.text)

def search_by_common_name(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Returns matches found by comparing the search key to the ITIS common names.
    """
    url = f"{BASE_URL}searchByCommonName"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return response.json()

def search_by_common_name_begins_with(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Returns matches found by comparing the search key to the beginning of the ITIS common names.
    """
    url = f"{BASE_URL}searchByCommonNameBeginsWith"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return response.json()

def search_by_common_name_ends_with(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Returns matches found by comparing the search key to the end of the ITIS common names.
    """
    url = f"{BASE_URL}searchByCommonNameEndsWith"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return response.json()

def search_by_scientific_name(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Returns matches found by comparing the search key to the ITIS full Scientific Names.
    """
    url = f"{BASE_URL}searchByScientificName"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return response.json()

def get_itis_terms(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Gets a list of ITIS Terms from a common or scientific name match.
    """
    url = f"{BASE_URL}getITISTerms"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return response.json()

def get_itis_terms_from_common_name(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Gets a list of ITIS Terms from a common name match.
    """
    url = f"{BASE_URL}getITISTermsFromCommonName"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return response.json()

def get_itis_terms_from_scientific_name(srch_key: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Gets a list of ITIS Terms from a scientific name match.
    """
    url = f"{BASE_URL}getITISTermsFromScientificName"
    params = {'srchKey': srch_key}
    response = requests.get(url, params=params)
    return response.json()

def get_tsn_by_vernacular_language(language: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Provide a listing of TSNs with vernaculars entered in the requested language.
    """
    url = f"{BASE_URL}getTsnByVernacularLanguage"
    params = {'language': language}
    response = requests.get(url, params=params)
    return response.json()

## Further implementation could continue with all other APIs as needed.