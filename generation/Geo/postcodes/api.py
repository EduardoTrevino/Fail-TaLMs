import requests
from typing import List, Optional

def lookup_postcode(postcode: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(url)
    return response.json()

def bulk_lookup_postcodes(postcodes: List[str], toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.postcodes.io/postcodes"
    data = {"postcodes": postcodes}
    response = requests.post(url, json=data)
    return response.json()

def nearest_postcodes(lon: float, lat: float, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.postcodes.io/postcodes"
    params = {"lon": lon, "lat": lat, "limit": limit}
    response = requests.get(url, params=params)
    return response.json()

def validate_postcode(postcode: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/postcodes/{postcode}/validate"
    response = requests.get(url)
    return response.json()

def nearest_postcodes_for_postcode(postcode: str, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/postcodes/{postcode}/nearest"
    params = {"limit": limit}
    response = requests.get(url, params=params)
    return response.json()

def autocomplete_postcode(postcode: str, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/postcodes/{postcode}/autocomplete"
    params = {"limit": limit}
    response = requests.get(url, params=params)
    return response.json()

def query_postcodes(query: str, limit: Optional[int] = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/postcodes"
    params = {"q": query, "limit": limit}
    response = requests.get(url, params=params)
    return response.json()

def lookup_random_postcode(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.postcodes.io/random/postcodes"
    response = requests.get(url)
    return response.json()

def lookup_terminated_postcode(postcode: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/terminated_postcodes/{postcode}"
    response = requests.get(url)
    return response.json()

def lookup_outward_code(outcode: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/outcodes/{outcode}"
    response = requests.get(url)
    return response.json()

def nearest_outcode_for_outcode(outcode: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/outcodes/{outcode}/nearest"
    response = requests.get(url)
    return response.json()

def nearest_outcode(lon: float, lat: float, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/outcodes"
    params = {"lon": lon, "lat": lat}
    response = requests.get(url, params=params)
    return response.json()

def lookup_scottish_postcode(postcode: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/scotland/postcodes/{postcode}"
    response = requests.get(url)
    return response.json()

def lookup_place(code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/places/{code}"
    response = requests.get(url)
    return response.json()

def query_places(query: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.postcodes.io/places"
    params = {"q": query}
    response = requests.get(url, params=params)
    return response.json()

def lookup_random_place(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.postcodes.io/random/places"
    response = requests.get(url)
    return response.json()