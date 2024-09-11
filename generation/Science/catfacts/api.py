import requests
from typing import Optional

def get_cat_facts(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve daily cat facts.
    """
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}