import requests
from typing import Optional


def get_favicon(domain: str, sz: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the favicon for a specified domain. Optionally, specify the size of the favicon image.

    Parameters:
    - domain [Required]: string - The domain to retrieve the favicon from.
    - sz [Optional]: integer - A size hint for the favicon (e.g., 128, 256). Defaults to None, which returns the default size (usually 16x16).
    """
    url = "https://www.google.com/s2/favicons"
    params = {
        'domain': domain
    }
    if sz:
        params['sz'] = sz

    response = requests.get(url, params=params)
    try:
        # Returns the content directly (typically PNG binary data)
        return response.content
    except Exception as e:
        return {"error": str(e), "response": response.text}