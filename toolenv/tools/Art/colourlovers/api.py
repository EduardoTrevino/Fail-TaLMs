import requests
import json
from typing import Optional, Dict, List

def top_colors(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', lover: Optional[str] = None, hueRange: Optional[str] = None, briRange: Optional[str] = None,
               keywords: Optional[str] = None, keywordExact: Optional[int] = None, orderCol: Optional[str] = None,
               sortBy: Optional[str] = None, numResults: Optional[int] = 20, resultOffset: Optional[int] = 0,
               format: Optional[str] = "json", jsonCallback: Optional[str] = None):
    """
    Fetch top colors based on specific parameters
    """
    url = "http://www.colourlovers.com/api/colors/top"
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
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_patterns(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', lover: Optional[str] = None, hueOption: Optional[str] = None, hex: Optional[str] = None,
                 hex_logic: Optional[str] = "AND", keywords: Optional[str] = None, keywordExact: Optional[int] = None,
                 orderCol: Optional[str] = None, sortBy: Optional[str] = None, numResults: Optional[int] = 20,
                 resultOffset: Optional[int] = 0, format: Optional[str] = "json", jsonCallback: Optional[str] = None):
    """
    Fetch top patterns based on specific parameters
    """
    url = "http://www.colourlovers.com/api/patterns/top"
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
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
