import requests
from typing import Optional, Dict

def get_game_details(item_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve details of a specific game based on its item ID in the Barter system.
    
    Args:
        item_id (int): The ID of the game in the Barter system.
    
    Returns:
        Dict: The JSON response from the Barter API containing game details.
    """
    url = f"https://barter.vg/i/{item_id}/json"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def get_game_bundles(item_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve information about bundles in which a specific game has been included.
    
    Args:
        item_id (int): The ID of the game in the Barter system.
    
    Returns:
        Dict: The JSON response from the Barter API containing bundle details.
    """
    url = f"https://barter.vg/browse/bundles/json"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
