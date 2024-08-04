import requests

def get_all_objects(metadataDate=None, departmentIds=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all valid Object IDs available for access.

    :param metadataDate: datetime, optional, e.g., YYYY-MM-DD
    :param departmentIds: str, optional, integers delimited with the | character
    :return: JSON response from the API
    """
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
    params = {}
    if metadataDate:
        params['metadataDate'] = metadataDate
    if departmentIds:
        params['departmentIds'] = departmentIds
    
    response = requests.get(url, params=params)
    return response.json()

def get_object(objectID, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a record for an object containing all open access data about that object.

    :param objectID: int, required
    :return: JSON response from the API
    """
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectID}"
    response = requests.get(url)
    return response.json()

def get_departments(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a listing of all departments.

    :return: JSON response from the API
    """
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(url)
    return response.json()

def search_objects(q, isHighlight=None, title=None, tags=None, departmentId=None, isOnView=None, artistOrCulture=None, medium=None, hasImages=None, geoLocation=None, dateBegin=None, dateEnd=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for objects in the Met's collection.

    :param q: str, required, search term
    :param isHighlight: bool, optional
    :param title: bool, optional
    :param tags: bool, optional
    :param departmentId: int, optional
    :param isOnView: bool, optional
    :param artistOrCulture: bool, optional
    :param medium: str, optional
    :param hasImages: bool, optional
    :param geoLocation: str, optional
    :param dateBegin: int, optional
    :param dateEnd: int, optional
    :return: JSON response from the API
    """
    url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    params = {'q': q}
    if isHighlight is not None:
        params['isHighlight'] = isHighlight
    if title is not None:
        params['title'] = title
    if tags is not None:
        params['tags'] = tags
    if departmentId is not None:
        params['departmentId'] = departmentId
    if isOnView is not None:
        params['isOnView'] = isOnView
    if artistOrCulture is not None:
        params['artistOrCulture'] = artistOrCulture
    if medium is not None:
        params['medium'] = medium
    if hasImages is not None:
        params['hasImages'] = hasImages
    if geoLocation is not None:
        params['geoLocation'] = geoLocation
    if dateBegin is not None:
        params['dateBegin'] = dateBegin
    if dateEnd is not None:
        params['dateEnd'] = dateEnd
    
    response = requests.get(url, params=params)
    return response.json()
