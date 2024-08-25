import requests
from typing import Optional


def get_languages(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Gets the languages targeted by the FilterLists.
    Parameters: None
    """
    url = "https://api.filterlists.com/v1/languages"
    headers = {
        "toolbench-rapidapi-key": toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_licenses(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Gets the licenses applied to the FilterLists.
    Parameters: None
    """
    url = "https://api.filterlists.com/v1/licenses"
    headers = {
        "toolbench-rapidapi-key": toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_lists(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Gets the FilterLists.
    Parameters: None
    """
    url = "https://api.filterlists.com/v1/lists"
    headers = {
        "toolbench-rapidapi-key": toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_list_details(list_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Gets the details of the specified FilterList.
    Parameters:
     list_id [Required]: integer [Description: The identifier of the FilterList.]
    """
    url = f"https://api.filterlists.com/v1/lists/{list_id}"
    headers = {
        "toolbench-rapidapi-key": toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_maintainers(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Gets the maintainers of the FilterLists.
    Parameters: None
    """
    url = "https://api.filterlists.com/v1/maintainers"
    headers = {
        "toolbench-rapidapi-key": toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_software(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Gets the software that subscribes to the FilterLists.
    Parameters: None
    """
    url = "https://api.filterlists.com/v1/software"
    headers = {
        "toolbench-rapidapi-key": toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_syntaxes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Gets the syntaxes of the FilterLists.
    Parameters: None
    """
    url = "https://api.filterlists.com/v1/syntaxes"
    headers = {
        "toolbench-rapidapi-key": toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_tags(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Gets the tags of the FilterLists.
    Parameters: None
    """
    url = "https://api.filterlists.com/v1/tags"
    headers = {
        "toolbench-rapidapi-key": toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}