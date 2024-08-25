import requests
from typing import Optional, List, Dict, Union

def get_country_data(country_code: str, format_type: str = "json", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific country using its ISO2 country code.
    
    Parameters:
    - country_code: Two-letter ISO code of the country.
    - format_type: The format in which to receive the data (default is 'json').
    """
    url = f"http://api.worldbank.org/v2/country/{country_code}"
    params = {
        'format': format_type
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format_type == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_countries(format_type: str = "json", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all countries available in the World Bank API.
    
    Parameters:
    - format_type: The format in which to receive the data (default is 'json').
    """
    url = f"http://api.worldbank.org/v2/country"
    params = {
        'format': format_type
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format_type == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_indicator_data(country_code: str, indicator_code: str, date: Optional[str] = None, format_type: str = "json", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve indicator data for a specific country and indicator.
    
    Parameters:
    - country_code: Two-letter ISO code of the country.
    - indicator_code: Indicator code to retrieve data for.
    - date: Date or date range for the data (e.g., '2000', '2000:2010').
    - format_type: The format in which to receive the data (default is 'json').
    """
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}"
    params = {
        'format': format_type
    }
    if date:
        params['date'] = date
    response = requests.get(url, params=params)
    try:
        return response.json() if format_type == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_indicators(format_type: str = "json", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all indicators available in the World Bank API.
    
    Parameters:
    - format_type: The format in which to receive the data (default is 'json').
    """
    url = f"http://api.worldbank.org/v2/indicator"
    params = {
        'format': format_type
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format_type == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_regions(format_type: str = "json", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all regions available in the World Bank API.
    
    Parameters:
    - format_type: The format in which to receive the data (default is 'json').
    """
    url = f"http://api.worldbank.org/v2/region"
    params = {
        'format': format_type
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format_type == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_income_levels(format_type: str = "json", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all income levels available in the World Bank API.
    
    Parameters:
    - format_type: The format in which to receive the data (default is 'json').
    """
    url = f"http://api.worldbank.org/v2/incomelevel"
    params = {
        'format': format_type
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format_type == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_lending_types(format_type: str = "json", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all lending types available in the World Bank API.
    
    Parameters:
    - format_type: The format in which to receive the data (default is 'json').
    """
    url = f"http://api.worldbank.org/v2/lendingtype"
    params = {
        'format': format_type
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format_type == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}