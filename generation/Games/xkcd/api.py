import requests
from typing import Optional, Dict

def get_current_comic(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get the current comic.
    
    Returns: 
        A dictionary containing the current comic's metadata.
    """
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_comic_by_number(number: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get a comic by its number.
    
    Parameters:
        number (int): The comic number to fetch.
        
    Returns:
        A dictionary containing the specified comic's metadata.
    """
    url = f"https://xkcd.com/{number}/info.0.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}