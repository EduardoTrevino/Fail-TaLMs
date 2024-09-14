import requests
from typing import Optional, List

def generate_avatar(style_name: str, seed: Optional[str] = None, hair: Optional[List[str]] = None, flip: Optional[bool] = False, format: Optional[str] = 'svg', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generates an avatar of a specified style with optional parameters like seed, hair, flip, and format.
    
    :param style_name: str - The style of the avatar, e.g., 'pixel-art', 'lorelei'.
    :param seed: Optional[str] - Seed value for generating a repeatable avatar.
    :param hair: Optional[List[str]] - List of hair styles.
    :param flip: Optional[bool] - Boolean to flip the avatar.
    :param format: Optional[str] - The format of the avatar ('svg', 'png', 'jpg', 'webp', 'avif', 'json').
    """
    url = f"https://api.dicebear.com/9.x/{style_name}/{format}"
    params = {}

    if seed:
        params['seed'] = seed
    if hair:
        params['hair'] = ','.join(hair)
    if flip is not None:
        params['flip'] = str(flip).lower()

    response = requests.get(url, params=params)
    try:
        return response.content if format != 'json' else response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}