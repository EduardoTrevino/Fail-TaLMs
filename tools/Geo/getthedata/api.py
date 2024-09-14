import requests
from typing import Optional

def bng2latlong(easting: int, northing: int, response_format: Optional[str] = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Convert an OSGB36 easting and northing (British National Grid) to WGS84 latitude and longitude.

    Parameters:
    easting [Required]: int (The easting coordinate)
    northing [Required]: int (The northing coordinate)
    response_format [Optional]: str (Specify the response format, 'json' or 'xml'. Defaults to 'json')

    Returns:
    JSON or XML response with the conversion results or an error message if any.
    """
    url = f"https://api.getthedata.com/bng2latlong/{easting}/{northing}"
    
    if response_format == 'xml':
        url += '/xml'
    
    response = requests.get(url)
    if response_format == 'json':
        try:
            return response.json()
        except Exception as e:
            return {"error": str(e), "response": response.text}
    else:
        return response.text