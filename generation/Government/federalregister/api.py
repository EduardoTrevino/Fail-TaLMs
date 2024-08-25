import requests
from typing import Optional, List

def fetch_single_document(fr_document_number: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch single Federal Register document using the FR document number.
    
    Parameters:
    fr_document_number [Required]: string - Federal Register document number.
    """
    url = f"https://www.federalregister.gov/api/v1/documents/{fr_document_number}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def fetch_multiple_documents(fr_document_numbers: List[str], toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch multiple Federal Register documents by their document numbers.
    
    Parameters:
    fr_document_numbers [Required]: list of strings - List of Federal Register document numbers.
    """
    url = "https://www.federalregister.gov/api/v1/documents/multiple.json"
    params = {
        'document_numbers[]': fr_document_numbers
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_documents(query: str, page: Optional[int] = 1, per_page: Optional[int] = 20, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search Federal Register documents using query parameters.
    
    Parameters:
    query [Required]: string - Search query.
    page [Optional]: integer - Page number for paginated results.
    per_page [Optional]: integer - Number of results per page.
    """
    url = "https://www.federalregister.gov/api/v1/documents.json"
    params = {
        'q': query,
        'page': page,
        'per_page': per_page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def fetch_single_pi_document(pi_document_number: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch metadata and PDF link for a Public Inspection document by its number.
    
    Parameters:
    pi_document_number [Required]: string - Public Inspection document number.
    """
    url = f"https://www.federalregister.gov/api/v1/public-inspection/{pi_document_number}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def fetch_multiple_pi_documents(pi_document_numbers: List[str], toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch multiple Public Inspection documents by their document numbers.
    
    Parameters:
    pi_document_numbers [Required]: list of strings - List of Public Inspection document numbers.
    """
    url = "https://www.federalregister.gov/api/v1/public-inspection/multiple.json"
    params = {
        'document_numbers[]': pi_document_numbers
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_pi_documents(query: str, page: Optional[int] = 1, per_page: Optional[int] = 20, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search Public Inspection documents using query parameters.
    
    Parameters:
    query [Required]: string - Search query.
    page [Optional]: integer - Page number for paginated results.
    per_page [Optional]: integer - Number of results per page.
    """
    url = "https://www.federalregister.gov/api/v1/public-inspection.json"
    params = {
        'q': query,
        'page': page,
        'per_page': per_page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_current_pi_documents(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all documents currently on public inspection.
    """
    url = "https://www.federalregister.gov/api/v1/public-inspection/current.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_pi_documents_by_date(date: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all the documents that were on public inspection on a given date.
    
    Parameters:
    date [Required]: string - Date in format YYYY-MM-DD.
    """
    url = f"https://www.federalregister.gov/api/v1/public-inspection/{date}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_agency_data(agency_id: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get basic data about agencies. Optionally filter by agency ID.
    
    Parameters:
    agency_id [Optional]: string - ID of the agency.
    """
    url = "https://www.federalregister.gov/api/v1/agencies.json"
    if agency_id:
        url = f"https://www.federalregister.gov/api/v1/agencies/{agency_id}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}