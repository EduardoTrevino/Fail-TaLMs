import requests
from typing import Optional


def get_random_quote(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a random quote from Breaking Bad.
    """
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_multiple_quotes(number: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a specified number of quotes from Breaking Bad.
    Parameters:
        number [Optional]: integer [Description: The number of quotes to retrieve.]
    """
    url = f"https://api.breakingbadquotes.xyz/v1/quotes/{number}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}