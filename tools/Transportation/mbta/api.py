import requests
from typing import Optional, Dict


BASE_URL = "https://api-v3.mbta.com"


def get_alerts(
    filter_activity: Optional[str] = None,
    filter_route_type: Optional[str] = None,
    filter_direction_id: Optional[str] = None,
    filter_route: Optional[str] = None,
    filter_stop: Optional[str] = None,
    filter_trip: Optional[str] = None,
    filter_facility: Optional[str] = None,
    filter_id: Optional[str] = None,
    filter_banner: Optional[str] = None,
    filter_datetime: Optional[str] = None,
    filter_lifecycle: Optional[str] = None,
    filter_severity: Optional[str] = None,
    page_offset: Optional[int] = None,
    page_limit: Optional[int] = None,
    sort: Optional[str] = None,
    fields_alert: Optional[str] = None,
    include: Optional[str] = None,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict:
    url = f"{BASE_URL}/alerts"
    params = {
        "filter[activity]": filter_activity,
        "filter[route_type]": filter_route_type,
        "filter[direction_id]": filter_direction_id,
        "filter[route]": filter_route,
        "filter[stop]": filter_stop,
        "filter[trip]": filter_trip,
        "filter[facility]": filter_facility,
        "filter[id]": filter_id,
        "filter[banner]": filter_banner,
        "filter[datetime]": filter_datetime,
        "filter[lifecycle]": filter_lifecycle,
        "filter[severity]": filter_severity,
        "page[offset]": page_offset,
        "page[limit]": page_limit,
        "sort": sort,
        "fields[alert]": fields_alert,
        "include": include
    }
    
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return str(response.json())
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_alert_detail(alert_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get details of a specific alert by ID.
    """
    url = f"{BASE_URL}/alerts/{alert_id}"
    
    response = requests.get(url)
    try:
        return str(response.json())
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_facilities(
    filter_type: Optional[str] = None,
    filter_stop: Optional[str] = None,
    page_offset: Optional[int] = None,
    page_limit: Optional[int] = None,
    sort: Optional[str] = None,
    fields_facility: Optional[str] = None,
    include: Optional[str] = None,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict:
    url = f"{BASE_URL}/facilities"
    params = {
        "filter[type]": filter_type,
        "filter[stop]": filter_stop,
        "page[offset]": page_offset,
        "page[limit]": page_limit,
        "sort": sort,
        "fields[facility]": fields_facility,
        "include": include
    }
    
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return str(response.json())
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_facility_detail(facility_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get details of a specific facility by ID.
    """
    url = f"{BASE_URL}/facilities/{facility_id}"
    
    response = requests.get(url)
    try:
        return str(response.json())
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_lines(
    filter_id: Optional[str] = None,
    page_offset: Optional[int] = None,
    page_limit: Optional[int] = None,
    sort: Optional[str] = None,
    fields_line: Optional[str] = None,
    include: Optional[str] = None,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict:
    url = f"{BASE_URL}/lines"
    params = {
        "filter[id]": filter_id,
        "page[offset]": page_offset,
        "page[limit]": page_limit,
        "sort": sort,
        "fields[line]": fields_line,
        "include": include
    }
    
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return str(response.json())
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_line_detail(line_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get details of a specific line by ID.
    """
    url = f"{BASE_URL}/lines/{line_id}"
    
    response = requests.get(url)
    try:
        return str(response.json())
    except Exception as e:
        return {"error": str(e), "response": response.text}

# Additional functions for other endpoints can be added here following the same structure