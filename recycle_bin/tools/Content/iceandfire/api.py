import requests

def get_character(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific character from the Ice and Fire universe.

    Parameters:
    - id (int): The unique ID of the character.

    Returns:
    - dict: The response from the API.
    """
    url = f"https://anapioficeandfire.com/api/characters/{id}"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text


def get_house(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a specific house from the Ice and Fire universe.

    Parameters:
    - id (int): The unique ID of the house.

    Returns:
    - dict: The response from the API.
    """
    url = f"https://anapioficeandfire.com/api/houses/{id}"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text
