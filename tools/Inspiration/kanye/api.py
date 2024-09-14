import requests

def get_random_kanye_quote(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetches a random Kanye West quote.
    Documentation: A free REST API for random Kanye West quotes (Kanye as a Service).
    """
    url = "https://api.kanye.rest/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}