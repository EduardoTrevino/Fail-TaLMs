import requests
from typing import Optional, List

def get_objects(metadata_date: Optional[str] = None, department_ids: Optional[List[int]] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves a list of all valid Object IDs available for access.
    Parameters:
    metadata_date [Optional]: str: Returns any objects with updated data after this date (format: YYYY-MM-DD).
    department_ids [Optional]: List[int]: Returns any objects in the specified departments delimited with the | character.
    """
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
    params = {}
    if metadata_date:
        params['metadataDate'] = metadata_date
    if department_ids:
        params['departmentIds'] = '|'.join(map(str, department_ids))
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_object_details(object_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves detailed information for an object using its unique Object ID.
    Parameters:
    object_id [Required]: int: The unique Object ID for the object.
    """
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_departments(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves a list of all departments.
    """
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_objects(q: str, is_highlight: Optional[bool] = None, title: Optional[bool] = None, tags: Optional[bool] = None, department_id: Optional[int] = None, is_on_view: Optional[bool] = None, artist_or_culture: Optional[bool] = None, medium: Optional[str] = None, has_images: Optional[bool] = None, geo_location: Optional[str] = None, date_begin: Optional[int] = None, date_end: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Searches for objects that match the query within the object's data.
    Parameters:
    q [Required]: str: The search term.
    is_highlight [Optional]: bool: Returns objects that are designated as highlights.
    title [Optional]: bool: Searches specifically against the title field for objects.
    tags [Optional]: bool: Searches specifically against the subject keyword tags field for objects.
    department_id [Optional]: int: Filters objects by department.
    is_on_view [Optional]: bool: Returns objects that are currently on view in the museum.
    artist_or_culture [Optional]: bool: Searches against the artist name or culture field for objects.
    medium [Optional]: str: Filters objects by specified medium or object type.
    has_images [Optional]: bool: Filters objects that have images.
    geo_location [Optional]: str: Filters objects by geographic location.
    date_begin [Optional]: int: Filters objects created after a certain date.
    date_end [Optional]: int: Filters objects created before a certain date.
    """
    url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    params = {'q': q}
    if is_highlight is not None:
        params['isHighlight'] = str(is_highlight)
    if title is not None:
        params['title'] = str(title)
    if tags is not None:
        params['tags'] = str(tags)
    if department_id is not None:
        params['departmentId'] = department_id
    if is_on_view is not None:
        params['isOnView'] = str(is_on_view)
    if artist_or_culture is not None:
        params['artistOrCulture'] = str(artist_or_culture)
    if medium:
        params['medium'] = medium
    if has_images is not None:
        params['hasImages'] = str(has_images)
    if geo_location:
        params['geoLocation'] = geo_location
    if date_begin and date_end:
        params['dateBegin'] = date_begin
        params['dateEnd'] = date_end

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}