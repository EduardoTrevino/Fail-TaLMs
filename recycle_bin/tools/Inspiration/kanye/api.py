import requests
from typing import Optional, Dict, Union, List

def quote(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a random Kanye West quote
    """
    url = "https://api.kanye.rest/"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation