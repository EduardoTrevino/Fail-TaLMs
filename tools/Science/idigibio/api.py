import requests
from typing import Optional, List, Dict, Any

def view_basic_access(uuid: str, view_type: Optional[str] = 'records', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Returns iDigBio record format from legacy API.
    Parameters:
    uuid [Required]: string [Description: The unique identifier for the record.]
    view_type [Optional]: string [Description: The type of object to view. Default is 'records'.]
    """
    url = f"https://search.idigbio.org/v2/view/{view_type}/{uuid}"
    headers = {'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_records(rq: Optional[Dict] = None, sort: Optional[str] = None, fields: Optional[List[str]] = None, 
                   fields_exclude: Optional[List[str]] = None, limit: Optional[int] = 10, offset: Optional[int] = 0,
                   no_attribution: Optional[bool] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Searches for record objects.
    Parameters:
    rq [Optional]: dict [Description: Search Query in iDigBio Query Format.]
    sort [Optional]: string [Description: Field to sort on.]
    fields [Optional]: List of string [Description: List of fields to return.]
    fields_exclude [Optional]: List of string [Description: List of fields to exclude.]
    limit [Optional]: integer [Description: Max results.]
    offset [Optional]: integer [Description: Skip results.]
    no_attribution [Optional]: boolean [Description: Disable the attribution block.]
    """
    url = "https://search.idigbio.org/v2/search/records/"
    params = {
        'rq': rq, 
        'sort': sort, 
        'fields': fields, 
        'fields_exclude': fields_exclude, 
        'limit': limit, 
        'offset': offset, 
        'no_attribution': no_attribution
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None}, headers={'Content-Type': 'application/json'})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_media(mq: Optional[Dict] = None, rq: Optional[Dict] = None, sort: Optional[str] = None, fields: Optional[List[str]] = None, 
                 fields_exclude: Optional[List[str]] = None, limit: Optional[int] = 10, offset: Optional[int] = 0,
                 no_attribution: Optional[bool] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Searches for mediarecord objects.
    Parameters:
    mq [Optional]: dict [Description: Media Query in iDigBio Query Format.]
    rq [Optional]: dict [Description: Record Query in iDigBio Query Format.]
    sort [Optional]: string [Description: Field to sort on.]
    fields [Optional]: List of string [Description: List of fields to return.]
    fields_exclude [Optional]: List of string [Description: List of fields to exclude.]
    limit [Optional]: integer [Description: Max results.]
    offset [Optional]: integer [Description: Skip results.]
    no_attribution [Optional]: boolean [Description: Disable the attribution block.]
    """
    url = "https://search.idigbio.org/v2/search/media/"
    params = {
        'mq': mq, 
        'rq': rq, 
        'sort': sort, 
        'fields': fields, 
        'fields_exclude': fields_exclude, 
        'limit': limit, 
        'offset': offset, 
        'no_attribution': no_attribution
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None}, headers={'Content-Type': 'application/json'})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_recordsets(rsq: Optional[Dict] = None, sort: Optional[str] = None, fields: Optional[List[str]] = None, 
                      fields_exclude: Optional[List[str]] = None, limit: Optional[int] = 10, offset: Optional[int] = 0,
                      toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Searches for recordset objects.
    Parameters:
    rsq [Optional]: dict [Description: Recordset Query in iDigBio Query Format.]
    sort [Optional]: string [Description: Field to sort on.]
    fields [Optional]: List of string [Description: List of fields to return.]
    fields_exclude [Optional]: List of string [Description: List of fields to exclude.]
    limit [Optional]: integer [Description: Max results.]
    offset [Optional]: integer [Description: Skip results.]
    """
    url = "https://search.idigbio.org/v2/search/recordsets/"
    params = {
        'rsq': rsq, 
        'sort': sort, 
        'fields': fields, 
        'fields_exclude': fields_exclude, 
        'limit': limit, 
        'offset': offset
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None}, headers={'Content-Type': 'application/json'})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def create_map(rq: Optional[Dict] = None, style: Optional[Dict] = None, map_type: Optional[str] = 'geohash',
               toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Creates a map with iDigBio data.
    Parameters:
    rq [Optional]: dict [Description: Record Query in iDigBio Query Format.]
    style [Optional]: dict [Description: JSON dictionary describing map style.]
    map_type [Optional]: string [Description: 'geohash' or 'points'. Default is 'geohash'.]
    """
    url = "https://search.idigbio.org/v2/mapping/"
    data = {
        'rq': rq, 
        'style': style, 
        'type': map_type
    }
    response = requests.post(url, json={k: v for k, v in data.items() if v is not None}, headers={'Content-Type': 'application/json'})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}