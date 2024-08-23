import requests
from typing import Optional, Union

def generate_image(text: str, 
                   format: Optional[str] = 'png', 
                   set: Optional[str] = 'set1', 
                   size: Optional[str] = '200x200', 
                   bgset: Optional[str] = None, 
                   gravatar: Optional[Union[str, bool]] = None, 
                   ignoreext: Optional[bool] = None, 
                   toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Generate a unique image for any text.
    
    Parameters:
    - text [Required]: The text to generate the image from
    - format [Optional]: Format of the image (default: 'png')
    - set [Optional]: Set of images (default: 'set1')
    - size [Optional]: Size of the image (default: '200x200')
    - bgset [Optional]: Background set for the image
    - gravatar [Optional]: Whether to use gravatar, and if email is provided, whether to hash it
    - ignoreext [Optional]: Whether to include the extension in the hash calculation 
    """
    url = f"https://robohash.org/{text}.{format}"
    params = {
        'set': set,
        'size': size,
    }
    if bgset:
        params['bgset'] = bgset
    if gravatar:
        params['gravatar'] = 'hashed' if gravatar == 'hashed' else 'yes'
    if ignoreext:
        params['ignoreext'] = 'false'
    
    response = requests.get(url, params=params)
    try:
        # Return the content of the image
        return response.content
    except Exception as e:
        return {"error": str(e), "response": response.text}