import requests

def randomaffirmation(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate a random affirmation.
    """
    url = "https://www.affirmations.dev/"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation