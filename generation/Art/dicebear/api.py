import requests
from typing import Optional, List

def get_avatar(style_name: str, format: str = 'svg', seed: Optional[str] = None, hair: Optional[List[str]] = None, flip: Optional[bool] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get an avatar based on the specified style and options.
    
    Parameters:
    style_name [Required]: string - The name of the avatar style.
    format [Optional]: string - The format of the avatar (default: svg).
    seed [Optional]: string - Seed for avatar generation.
    hair [Optional]: List[string] - List of hair styles.
    flip [Optional]: bool - Boolean to flip the avatar.
    """
    base_url = f"https://api.dicebear.com/9.x/{style_name}/{format}"
    params = {}

    if seed:
        params['seed'] = seed
    if hair:
        params['hair'] = ','.join(hair)
    if flip is not None:
        params['flip'] = str(flip).lower()  # Convert boolean to string "true" or "false"

    response = requests.get(base_url, params=params)
    
    if 'image' in response.headers.get('content-type', ''):
        return response.content  # If the response is an image
    try:
        return response.json()  # If the response is JSON
    except Exception as e:
        return {"error": str(e), "response": response.text}