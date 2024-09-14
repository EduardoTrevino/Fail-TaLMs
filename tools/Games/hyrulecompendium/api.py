import requests
from typing import Optional


def get_entry(entry: str, game: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves a specific entry given its name or ID. 
    Parameters:
    entry [Required]: string - The name or ID of the entry.
    game [Optional]: string - The game version to query; defaults to 'botw'.
    """
    url = f"https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{entry}"
    params = {'game': game} if game else {}
    response = requests.get(url, params=params)
    return response.json()


def get_all_entries(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all compendium entries.
    """
    url = "https://botw-compendium.herokuapp.com/api/v3/compendium/all"
    response = requests.get(url)
    return response.json()


def get_category_entries(category: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all entries in a given category.
    Parameters:
    category [Required]: string - The category to retrieve entries from.
    """
    url = f"https://botw-compendium.herokuapp.com/api/v3/compendium/category/{category}"
    response = requests.get(url)
    return response.json()


def get_master_mode_entry(entry: str, game: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves data on a master mode exclusive entry given its name or ID.
    Parameters:
    entry [Required]: string - The name or ID of the master mode exclusive entry.
    game [Optional]: string - The game version to query; defaults to 'botw'.
    """
    url = f"https://botw-compendium.herokuapp.com/api/v3/compendium/master_mode/entry/{entry}"
    params = {'game': game} if game else {}
    response = requests.get(url, params=params)
    return response.json()


def get_all_master_mode_entries(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all master mode exclusive entries.
    """
    url = "https://botw-compendium.herokuapp.com/api/v3/compendium/master_mode/all"
    response = requests.get(url)
    return response.json()


def get_region(region: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves information on a single region given its name.
    Parameters:
    region [Required]: string - The name of the region.
    """
    url = f"https://botw-compendium.herokuapp.com/api/v3/regions/{region}"
    response = requests.get(url)
    return response.json()


def get_all_regions(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all regions.
    """
    url = "https://botw-compendium.herokuapp.com/api/v3/regions/all"
    response = requests.get(url)
    return response.json()