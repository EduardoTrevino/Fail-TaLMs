import requests
from typing import Optional


def getcapabilities(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of available API functions and list of their parameters.
    """
    url = "https://api.ctext.org/getcapabilities"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def getcharacter(char: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns basic data about a character.
    :param char: Character to describe.
    """
    url = "https://api.ctext.org/getcharacter"
    params = {
        'char': char
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def getdictionaryheadwords(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a complete list of headwords for distinct word senses, names, and places having entries in the CTP dictionary.
    """
    url = "https://api.ctext.org/getdictionaryheadwords"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def getdynasties(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of identifiers, labels, and dates for dynasties used in the Chinese Text Project.
    """
    url = "https://api.ctext.org/getdynasties"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def getlink(urn: str, redirect: Optional[int] = 0, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a http://ctext.org URL corresponding to a URN.
    :param urn: URN specifying the text to return a link to.
    :param redirect: If set to 1, do not return a JSON response, but instead return an HTTP 30x response.
    :param search: Link to human-readable search results for the phrase within the specified URN.
    """
    url = "https://api.ctext.org/getlink"
    params = {
        'urn': urn,
        'redirect': redirect,
        'search': search
    }
    response = requests.get(url, params=params)
    if redirect == 1:
        return response.url
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def getstats(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Machine-readable interface to data available at http://ctext.org/system-statistics
    """
    url = "https://api.ctext.org/getstats"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def getstatus(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the status of the current client-server relationship.
    """
    url = "https://api.ctext.org/getstatus"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def gettext(urn: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the textual content of a chapter of text.
    :param urn: URN specifying the text to return.
    """
    url = "https://api.ctext.org/gettext"
    params = {
        'urn': urn
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def gettextinfo(urn: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns metadata about a textual object.
    :param urn: URN specifying the text to describe.
    """
    url = "https://api.ctext.org/gettextinfo"
    params = {
        'urn': urn
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def gettexttitles(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a complete list of top-level textual items in the textual database and Wiki.
    """
    url = "https://api.ctext.org/gettexttitles"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def readlink(url: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a URN corresponding to a http://ctext.org URL.
    :param url: URL specifying a text on http://ctext.org.
    """
    api_url = "https://api.ctext.org/readlink"
    params = {
        'url': url
    }
    response = requests.get(api_url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def searchtexts(title: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of items in the textual database and Wiki matching specified parameters.
    :param title: Part or all of the text title.
    """
    url = "https://api.ctext.org/searchtexts"
    params = {
        'title': title
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}