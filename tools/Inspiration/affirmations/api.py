import requests

def get_random_affirmation(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch a random affirmation.
    """
    url = "https://www.affirmations.dev/"
    headers = {
        'X-RapidAPI-Key': toolbench_rapidapi_key
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}