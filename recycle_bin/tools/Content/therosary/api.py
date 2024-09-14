import requests
from typing import Optional

def today(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Will return today's rosary prayer.
    """
    url = "https://the-rosary-api.vercel.app/v1/today"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def joyful(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Will return joyful rosary prayer.
    """
    url = "https://the-rosary-api.vercel.app/v1/joyful"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
