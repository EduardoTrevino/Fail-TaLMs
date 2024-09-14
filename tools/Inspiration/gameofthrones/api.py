import requests
from typing import Optional

def get_random_quote(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch a random quote from the Game of Thrones API.
    """
    url = "https://api.gameofthronesquotes.xyz/v1/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_random_quotes(number: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch multiple random quotes from the Game of Thrones API.
    
    Parameters:
    number [Optional]: Number of random quotes to return. Defaults to 1.
    """
    url = f"https://api.gameofthronesquotes.xyz/v1/random/{number}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_quotes_by_character(character_slug: str, number: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch quotes for a specific character.
    
    Parameters:
    character_slug [Required]: Slug of the character.
    number [Optional]: Number of quotes to return. If None, all quotes are returned.
    """
    url = f"https://api.gameofthronesquotes.xyz/v1/author/{character_slug}"
    if number is not None:
        url += f"/{number}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_houses(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the list of houses from the Game of Thrones API.
    """
    url = "https://api.gameofthronesquotes.xyz/v1/houses"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_house_details(house_slug: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch details of a specific house.
    
    Parameters:
    house_slug [Required]: Slug of the house.
    """
    url = f"https://api.gameofthronesquotes.xyz/v1/house/{house_slug}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_characters(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the list of characters with their quotes from the Game of Thrones API.
    """
    url = "https://api.gameofthronesquotes.xyz/v1/characters"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_character_details(character_slug: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch details of a specific character.
    
    Parameters:
    character_slug [Required]: Slug of the character.
    """
    url = f"https://api.gameofthronesquotes.xyz/v1/character/{character_slug}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}