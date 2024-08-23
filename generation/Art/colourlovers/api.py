import requests
from typing import Optional, List


def colors(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', lover: Optional[str] = None, hueRange: Optional[str] = None, briRange: Optional[str] = None, keywords: Optional[str] = None, keywordExact: Optional[int] = 0, orderCol: Optional[str] = None, sortBy: Optional[str] = "ASC", numResults: Optional[int] = 20, resultOffset: Optional[int] = 0, format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch multiple colors based on provided parameters."""
    url = "http://www.colourlovers.com/api/colors"
    params = {
        'lover': lover,
        'hueRange': hueRange,
        'briRange': briRange,
        'keywords': keywords,
        'keywordExact': keywordExact,
        'orderCol': orderCol,
        'sortBy': sortBy,
        'numResults': numResults,
        'resultOffset': resultOffset,
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def colors_new(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **kwargs):
    """Fetch new colors based on provided parameters."""
    kwargs.update({'orderCol': 'dateCreated'})
    return colors(**kwargs)


def colors_top(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **kwargs):
    """Fetch top colors based on provided parameters."""
    kwargs.update({'orderCol': 'score'})
    return colors(**kwargs)


def colors_random(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch a random color."""
    url = "http://www.colourlovers.com/api/colors/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def color(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', hex_value: str = "6B4106", format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch details of a specific color using hex value."""
    url = f"http://www.colourlovers.com/api/color/{hex_value}"
    params = {
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def palettes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', lover: Optional[str] = None, hueOption: Optional[str] = None, hex: Optional[str] = None, hex_logic: Optional[str] = "AND", keywords: Optional[str] = None, keywordExact: Optional[int] = 0, orderCol: Optional[str] = None, sortBy: Optional[str] = "ASC", numResults: Optional[int] = 20, resultOffset: Optional[int] = 0, format: Optional[str] = "xml", jsonCallback: Optional[str] = None, showPaletteWidths: Optional[int] = 0):
    """Fetch multiple palettes based on provided parameters."""
    url = "http://www.colourlovers.com/api/palettes"
    params = {
        'lover': lover,
        'hueOption': hueOption,
        'hex': hex,
        'hex_logic': hex_logic,
        'keywords': keywords,
        'keywordExact': keywordExact,
        'orderCol': orderCol,
        'sortBy': sortBy,
        'numResults': numResults,
        'resultOffset': resultOffset,
        'format': format,
        'jsonCallback': jsonCallback,
        'showPaletteWidths': showPaletteWidths
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def palettes_new(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **kwargs):
    """Fetch new palettes based on provided parameters."""
    kwargs.update({'orderCol': 'dateCreated'})
    return palettes(**kwargs)


def palettes_top(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **kwargs):
    """Fetch top palettes based on provided parameters."""
    kwargs.update({'orderCol': 'score'})
    return palettes(**kwargs)


def palettes_random(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch a random palette."""
    url = "http://www.colourlovers.com/api/palettes/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def palette(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', palette_id: int = 113451, format: Optional[str] = "xml", jsonCallback: Optional[str] = None, showPaletteWidths: Optional[int] = 0):
    """Fetch details of a specific palette using palette ID."""
    url = f"http://www.colourlovers.com/api/palette/{palette_id}"
    params = {
        'format': format,
        'jsonCallback': jsonCallback,
        'showPaletteWidths': showPaletteWidths
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def patterns(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', lover: Optional[str] = None, hueOption: Optional[str] = None, hex: Optional[str] = None, hex_logic: Optional[str] = "AND", keywords: Optional[str] = None, keywordExact: Optional[int] = 0, orderCol: Optional[str] = None, sortBy: Optional[str] = "ASC", numResults: Optional[int] = 20, resultOffset: Optional[int] = 0, format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch multiple patterns based on provided parameters."""
    url = "http://www.colourlovers.com/api/patterns"
    params = {
        'lover': lover,
        'hueOption': hueOption,
        'hex': hex,
        'hex_logic': hex_logic,
        'keywords': keywords,
        'keywordExact': keywordExact,
        'orderCol': orderCol,
        'sortBy': sortBy,
        'numResults': numResults,
        'resultOffset': resultOffset,
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def patterns_new(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **kwargs):
    """Fetch new patterns based on provided parameters."""
    kwargs.update({'orderCol': 'dateCreated'})
    return patterns(**kwargs)


def patterns_top(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **kwargs):
    """Fetch top patterns based on provided parameters."""
    kwargs.update({'orderCol': 'score'})
    return patterns(**kwargs)


def patterns_random(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch a random pattern."""
    url = "http://www.colourlovers.com/api/patterns/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def pattern(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', pattern_id: int = 1451, format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch details of a specific pattern using pattern ID."""
    url = f"http://www.colourlovers.com/api/pattern/{pattern_id}"
    params = {
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def lovers(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', orderCol: Optional[str] = None, sortBy: Optional[str] = "ASC", numResults: Optional[int] = 20, resultOffset: Optional[int] = 0, format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch multiple lovers based on provided parameters."""
    url = "http://www.colourlovers.com/api/lovers"
    params = {
        'orderCol': orderCol,
        'sortBy': sortBy,
        'numResults': numResults,
        'resultOffset': resultOffset,
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def lovers_new(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **kwargs):
    """Fetch new lovers based on provided parameters."""
    kwargs.update({'orderCol': 'dateCreated'})
    return lovers(**kwargs)


def lovers_top(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', **kwargs):
    """Fetch top lovers based on provided parameters."""
    kwargs.update({'orderCol': 'score'})
    return lovers(**kwargs)


def lover(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', username: str = "COLOURlover", comments: Optional[int] = 0, format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch details of a specific lover using username."""
    url = f"http://www.colourlovers.com/api/lover/{username}"
    params = {
        'comments': comments,
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def stats_colors(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch total number of colors."""
    url = "http://www.colourlovers.com/api/stats/colors"
    params = {
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def stats_palettes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch total number of palettes."""
    url = "http://www.colourlovers.com/api/stats/palettes"
    params = {
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def stats_patterns(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch total number of patterns."""
    url = "http://www.colourlovers.com/api/stats/patterns"
    params = {
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def stats_lovers(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', format: Optional[str] = "xml", jsonCallback: Optional[str] = None):
    """Fetch total number of lovers."""
    url = "http://www.colourlovers.com/api/stats/lovers"
    params = {
        'format': format,
        'jsonCallback': jsonCallback
    }
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}