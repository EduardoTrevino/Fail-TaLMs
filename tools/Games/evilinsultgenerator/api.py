import requests
from typing import Optional


def generate_insult(lang: Optional[str] = 'en', type: Optional[str] = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: This endpoint serves to generate insults from the API.
    
    Optional Parameters:
    - lang: The language of the insult you want. Defaults to English ('en') if not provided.
    - type: The response type. It supports 'text', 'XML', and 'JSON'. Defaults to 'json' if not provided.
    """
    url = "https://evilinsult.com/generate_insult.php"
    params = {
        'lang': lang,
        'type': type
    }
    response = requests.get(url, params=params)
    try:
        if type == 'json':
            return response.json()
        else:
            return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}