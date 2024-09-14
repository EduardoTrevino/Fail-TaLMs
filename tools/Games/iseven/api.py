import requests
from typing import Dict


def iseven(number: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint description: Returns whether a given number is even.
    
    Parameters:
    number [Required]: integer [The number you want to check]
    """
    url = f"https://api.isevenapi.xyz/api/iseven/{number}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}