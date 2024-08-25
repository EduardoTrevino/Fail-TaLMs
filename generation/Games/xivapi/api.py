import requests
from typing import Optional, List


def search(string: str, indexes: Optional[str] = None,
           string_algo: Optional[str] = "wildcard", page: Optional[int] = None,
           sort_field: Optional[str] = None, sort_order: Optional[str] = "asc",
           limit: Optional[int] = 100, filters: Optional[str] = None, 
           toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    General search endpoint for FFXIV game content.
    """
    url = "https://xivapi.com/search"
    params = {
        "string": string,
        "indexes": indexes,
        "string_algo": string_algo,
        "page": page,
        "sort_field": sort_field,
        "sort_order": sort_order,
        "limit": limit,
        "filters": filters,
        "private_key": toolbench_rapidapi_key
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.json()


def get_content(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the list of available content.
    """
    url = "https://xivapi.com/content"
    params = {"private_key": toolbench_rapidapi_key}
    response = requests.get(url, params=params)
    return response.json()


def get_item(item_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific item by ID.
    """
    url = f"https://xivapi.com/item/{item_id}"
    params = {"private_key": toolbench_rapidapi_key}
    response = requests.get(url, params=params)
    return response.json()


def list_servers(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of servers.
    """
    url = "https://xivapi.com/servers"
    params = {"private_key": toolbench_rapidapi_key}
    response = requests.get(url, params=params)
    return response.json()


def list_servers_data_centers(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of servers grouped by data centers.
    """
    url = "https://xivapi.com/servers/dc"
    params = {"private_key": toolbench_rapidapi_key}
    response = requests.get(url, params=params)
    return response.json()


def character_search(name: str, server: Optional[str] = None, page: Optional[int] = 1,
                     toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for a character by name.
    """
    url = "https://xivapi.com/character/search"
    params = {
        "name": name,
        "server": server,
        "page": page,
        "private_key": toolbench_rapidapi_key
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.json()


def get_character(lodestone_id: int, extended: Optional[int] = 0,
                  data: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get detailed data about a character by Lodestone ID.
    """
    url = f"https://xivapi.com/character/{lodestone_id}"
    params = {
        "extended": extended,
        "data": data,
        "private_key": toolbench_rapidapi_key
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.json()


def freecompany_search(name: str, server: Optional[str] = None, page: Optional[int] = 1,
                       toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for a Free Company by name.
    """
    url = "https://xivapi.com/freecompany/search"
    params = {
        "name": name,
        "server": server,
        "page": page,
        "private_key": toolbench_rapidapi_key
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.json()


def get_freecompany(lodestone_id: int, extended: Optional[int] = 0,
                    data: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get detailed data about a Free Company by Lodestone ID.
    """
    url = f"https://xivapi.com/freecompany/{lodestone_id}"
    params = {
        "extended": extended,
        "data": data,
        "private_key": toolbench_rapidapi_key
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.json()


def linkshell_search(name: str, server: Optional[str] = None, page: Optional[int] = 1,
                     toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for a Linkshell by name.
    """
    url = "https://xivapi.com/linkshell/search"
    params = {
        "name": name,
        "server": server,
        "page": page,
        "private_key": toolbench_rapidapi_key
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.json()


def linkshell_crossworld_search(name: str, page: Optional[int] = 1,
                               toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for a cross-world Linkshell by name.
    """
    url = "https://xivapi.com/linkshell/crossworld/search"
    params = {
        "name": name,
        "page": page,
        "private_key": toolbench_rapidapi_key
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.json()