import requests
from typing import Optional

def get_word_definition(word: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> dict:
    """
    Retrieves the definition of the specified English word from the FreeDictionary API.
    
    Parameters:
    - word (str): The word to get the definition for.
    
    Returns:
    - dict: The API response containing the word definition.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}