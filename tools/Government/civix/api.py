import requests
from typing import Optional


def get_content(aspect: str = 'complete', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of documents within an aspect of the CiviX Server API content library.
    
    Parameters:
    - aspect: str (default: 'complete'): Aspect to retrieve content from.
    """
    url = f"http://www.bclaws.ca/civix/content/{aspect}/"
    response = requests.get(url)
    try:
        return response.content  # Returning the XML content
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_document(index_id: str, document_id: str, aspect: str = 'complete', xml: bool = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a document from the CiviX Server API repository.
    
    Parameters:
    - index_id: str: Unique index identifier.
    - document_id: str: Unique document identifier.
    - aspect: str (default 'complete'): Aspect of the document.
    - xml: bool (default False): If True, retrieves the document in XML format.
    """
    url = f"http://www.bclaws.ca/civix/document/id/{aspect}/{index_id}/{document_id}"
    if xml:
        url += "/xml"
    response = requests.get(url)
    try:
        return response.content  # Returning the document content, either HTML or XML
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_content(query: str, aspect: str = 'complete', start: int = 0, end: int = 20, n_frag: int = 5, l_frag: int = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for occurrences of a query term within an aspect of the CiviX Server API.
    
    Parameters:
    - query: str: Query term to search for.
    - aspect: str (default 'complete'): Aspect to search within.
    - start: int (default 0): First hit to return.
    - end: int (default 20): Last hit to return. Cannot be more than 100 away from start.
    - n_frag: int (default 5): Number of fragment snippets to return. Must be less than 10.
    - l_frag: int (default 100): Length of each fragment. Must be less than 200.
    """
    params = {
        'q': query,
        's': start,
        'e': end,
        'nFrag': n_frag,
        'lFrag': l_frag
    }
    url = f"http://www.bclaws.ca/civix/search/{aspect}/fullsearch"
    response = requests.get(url, params=params)
    try:
        return response.content  # Returning the search results as XML
    except Exception as e:
        return {"error": str(e), "response": response.text}