import requests
from typing import Optional


def get_robohash_image(text: str, fmt: Optional[str] = 'png', size: Optional[str] = None, 
                       set: Optional[str] = None, bgset: Optional[str] = None, gravatar: Optional[str] = None, 
                       ignoreext: Optional[bool] = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Generate a unique image from any text. Customize the image by using different sets, backgrounds, sizes, etc.
    
    Parameters:
    text [Required]: Text input for generating the image.
    fmt [Optional]: Output format of the image (e.g., 'png', 'jpg', 'bmp'). Defaults to 'png'.
    size [Optional]: Size of the generated image (e.g., '200x200').
    set [Optional]: The set to generate the image from (e.g., 'set1', 'set2', 'set3', 'set4', 'set5').
    bgset [Optional]: The background set to use (e.g., 'bg1', 'bg2').
    gravatar [Optional]: Set to 'yes' to use a gravatar image if available.
    ignoreext [Optional]: Boolean to determine whether to ignore the extension in the hash. Defaults to True.
    """
    base_url = f"https://robohash.org/{text}"
    
    params = {
        'ignoreext': str(ignoreext).lower()
    }
    
    if size:
        params['size'] = size
    if set:
        params['set'] = set
    if bgset:
        params['bgset'] = bgset
    if gravatar:
        params['gravatar'] = gravatar
    
    response = requests.get(f"{base_url}.{fmt}", params=params)
    
    if response.status_code != 200:
        return {"error": "Failed to retrieve image", "status_code": response.status_code}
    
    return response.content