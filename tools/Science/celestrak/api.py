import requests
from typing import Optional

BASE_URL = "https://celestrak.org/NORAD/elements/gp.php"

def query_by_catnr(catnr: str, format: Optional[str] = 'TLE', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Query the Celestrak GP Data using the Catalog Number (CATNR).

    Parameters:
    - catnr (str): Catalog number. Allows return of data for a single catalog number.
    - format (Optional[str]): Format of data. Defaults to 'TLE'. Options: 'TLE', '3LE', '2LE', 'XML', 'KVN', 'JSON', 'JSON-PRETTY', 'CSV'.
    """
    url = BASE_URL
    params = {
        'CATNR': catnr,
        'FORMAT': format
    }
    response = requests.get(url, params=params)
    try:
        return response.text if format in ['TLE', '3LE', '2LE', 'KVN', 'XML'] else response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def query_by_intdes(intdes: str, format: Optional[str] = 'TLE', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Query the Celestrak GP Data using International Designator (INTDES).

    Parameters:
    - intdes (str): International Designator (yyyy-nnn). Allows return of data for all objects associated with a particular launch.
    - format (Optional[str]): Format of data. Defaults to 'TLE'. Options: 'TLE', '3LE', '2LE', 'XML', 'KVN', 'JSON', 'JSON-PRETTY', 'CSV'.
    """
    url = BASE_URL
    params = {
        'INTDES': intdes,
        'FORMAT': format
    }
    response = requests.get(url, params=params)
    try:
        return response.text if format in ['TLE', '3LE', '2LE', 'KVN', 'XML'] else response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def query_by_group(group: str, format: Optional[str] = 'TLE', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Query the Celestrak GP Data using Groups of Satellites.

    Parameters:
    - group (str): Groups of satellites provided on the CelesTrak Current Data page.
    - format (Optional[str]): Format of data. Defaults to 'TLE'. Options: 'TLE', '3LE', '2LE', 'XML', 'KVN', 'JSON', 'JSON-PRETTY', 'CSV'.
    """
    url = BASE_URL
    params = {
        'GROUP': group,
        'FORMAT': format
    }
    response = requests.get(url, params=params)
    try:
        return response.text if format in ['TLE', '3LE', '2LE', 'KVN', 'XML'] else response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def query_by_name(name: str, format: Optional[str] = 'TLE', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Query the Celestrak GP Data using Satellite Name.

    Parameters:
    - name (str): Satellite Name. Allows searching for satellites by parts of their name.
    - format (Optional[str]): Format of data. Defaults to 'TLE'. Options: 'TLE', '3LE', '2LE', 'XML', 'KVN', 'JSON', 'JSON-PRETTY', 'CSV'.
    """
    url = BASE_URL
    params = {
        'NAME': name,
        'FORMAT': format
    }
    response = requests.get(url, params=params)
    try:
        return response.text if format in ['TLE', '3LE', '2LE', 'KVN', 'XML'] else response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def query_by_special(special: str, format: Optional[str] = 'TLE', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Query the Celestrak GP Data using Special datasets.

    Parameters:
    - special (str): Special data sets for the GEO Protected Zone (GPZ) or GPZ Plus.
    - format (Optional[str]): Format of data. Defaults to 'TLE'. Options: 'TLE', '3LE', '2LE', 'XML', 'KVN', 'JSON', 'JSON-PRETTY', 'CSV'.
    """
    url = BASE_URL
    params = {
        'SPECIAL': special,
        'FORMAT': format
    }
    response = requests.get(url, params=params)
    try:
        return response.text
        # return response.text if format in ['TLE', '3LE', '2LE', 'KVN', 'XML'] else response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}