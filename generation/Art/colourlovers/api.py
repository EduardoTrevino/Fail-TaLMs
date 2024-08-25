import requests
from typing import Optional, List, Dict

BASE_URL = "http://www.colourlovers.com/api"

def request_colorlovers_api(method: str, endpoint: str, params: Dict = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Helper function to request Colourlovers API.
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json() if 'json' in params.get("format", "xml") else response.text

def colors(lover: Optional[str] = None, hueRange: Optional[str] = None, briRange: Optional[str] = None,
           keywords: Optional[str] = None, keywordExact: int = 0, orderCol: Optional[str] = None,
           sortBy: str = "ASC", numResults: int = 20, resultOffset: int = 0, format: str = "json", 
           jsonCallback: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    params = {
        "lover": lover,
        "hueRange": hueRange,
        "briRange": briRange,
        "keywords": keywords,
        "keywordExact": keywordExact,
        "orderCol": orderCol,
        "sortBy": sortBy,
        "numResults": numResults,
        "resultOffset": resultOffset,
        "format": format,
        "jsonCallback": jsonCallback
    }
    return request_colorlovers_api(method="GET", endpoint="/colors", params=params)

def color(hex_value: str, format: str = "json", jsonCallback: Optional[str] = None, 
          toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    params = {
        "format": format,
        "jsonCallback": jsonCallback
    }
    return request_colorlovers_api(method="GET", endpoint=f"/color/{hex_value}", params=params)

def palettes(lover: Optional[str] = None, hueOption: Optional[str] = None, hex: Optional[str] = None,
             hex_logic: str = "AND", keywords: Optional[str] = None, keywordExact: int = 0, orderCol: Optional[str] = None, 
             sortBy: str = "ASC", numResults: int = 20, resultOffset: int = 0, format: str = "json",
             jsonCallback: Optional[str] = None, showPaletteWidths: int = 0, 
             toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    params = {
        "lover": lover,
        "hueOption": hueOption,
        "hex": hex,
        "hex_logic": hex_logic,
        "keywords": keywords,
        "keywordExact": keywordExact,
        "orderCol": orderCol,
        "sortBy": sortBy,
        "numResults": numResults,
        "resultOffset": resultOffset,
        "format": format,
        "jsonCallback": jsonCallback,
        "showPaletteWidths": showPaletteWidths
    }
    return request_colorlovers_api(method="GET", endpoint="/palettes", params=params)

def palette(palette_id: int, format: str = "json", jsonCallback: Optional[str] = None, 
            showPaletteWidths: int = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    params = {
        "format": format,
        "jsonCallback": jsonCallback,
        "showPaletteWidths": showPaletteWidths
    }
    return request_colorlovers_api(method="GET", endpoint=f"/palette/{palette_id}", params=params)

def patterns(lover: Optional[str] = None, hueOption: Optional[str] = None, hex: Optional[str] = None,
             hex_logic: str = "AND", keywords: Optional[str] = None, keywordExact: int = 0, orderCol: Optional[str] = None,
             sortBy: str = "ASC", numResults: int = 20, resultOffset: int = 0, format: str = "json",
             jsonCallback: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    params = {
        "lover": lover,
        "hueOption": hueOption,
        "hex": hex,
        "hex_logic": hex_logic,
        "keywords": keywords,
        "keywordExact": keywordExact,
        "orderCol": orderCol,
        "sortBy": sortBy,
        "numResults": numResults,
        "resultOffset": resultOffset,
        "format": format,
        "jsonCallback": jsonCallback
    }
    return request_colorlovers_api(method="GET", endpoint="/patterns", params=params)

def pattern(pattern_id: int, format: str = "json", jsonCallback: Optional[str] = None, 
            toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    params = {
        "format": format,
        "jsonCallback": jsonCallback
    }
    return request_colorlovers_api(method="GET", endpoint=f"/pattern/{pattern_id}", params=params)

def lovers(orderCol: Optional[str] = None, sortBy: str = "ASC", numResults: int = 20, 
           resultOffset: int = 0, format: str = "json", jsonCallback: Optional[str] = None,
           toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    params = {
        "orderCol": orderCol,
        "sortBy": sortBy,
        "numResults": numResults,
        "resultOffset": resultOffset,
        "format": format,
        "jsonCallback": jsonCallback
    }
    return request_colorlovers_api(method="GET", endpoint="/lovers", params=params)

def lover(username: str, comments: int = 0, format: str = "json", jsonCallback: Optional[str] = None, 
          toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    params = {
        "comments": comments,
        "format": format,
        "jsonCallback": jsonCallback
    }
    return request_colorlovers_api(method="GET", endpoint=f"/lover/{username}", params=params)

def stats(resource: str, format: str = "json", jsonCallback: Optional[str] = None,
          toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    # Ensure resource is valid
    if resource not in ['colors', 'palettes', 'patterns', 'lovers']:
        raise ValueError("Invalid resource type. Must be 'colors', 'palettes', 'patterns', or 'lovers'.")
    
    params = {
        "format": format,
        "jsonCallback": jsonCallback
    }
    return request_colorlovers_api(method="GET", endpoint=f"/stats/{resource}", params=params)