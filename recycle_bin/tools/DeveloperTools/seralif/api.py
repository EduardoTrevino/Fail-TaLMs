import requests
from typing import Optional, Dict

def get_color_by_keyword(keyword: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve color information by keyword.
    """
    url = f"https://color.serialif.com/keyword={keyword}"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_color_by_hex(hex_value: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve color information by HEX value.
    """
    url = f"https://color.serialif.com/hex={hex_value}"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_contrasted_text(hex_value: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the ideal text color (black or white) for the provided color to ensure readability.
    """
    url = f"https://color.serialif.com/hex={hex_value}&contrasted_text"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
