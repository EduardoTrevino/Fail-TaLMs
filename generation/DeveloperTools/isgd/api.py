import requests
from urllib.parse import urlencode
from typing import Optional


def shorten_url(url: str, format: Optional[str] = 'simple', shorturl: Optional[str] = None, callback: Optional[str] = None, logstats: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Shortens a given URL using the is.gd service.

    Parameters:
    - url: The URL you want to shorten. (Required)
    - format: The format of the response ('web', 'simple', 'xml', 'json'). Defaults to 'simple'.
    - shorturl: Custom shortened URL you would like to use (optional).
    - callback: Used only with format 'json' to specify a callback function (optional).
    - logstats: If 1, enables logging of detailed statistics (optional).

    Returns:
    - The shortened URL or error message.
    """
    base_url = "https://is.gd/create.php?"
    params = {
        'format': format,
        'url': url
    }
    if shorturl:
        params['shorturl'] = shorturl
    if callback and format == 'json':
        params['callback'] = callback
    if logstats == 1:
        params['logstats'] = logstats

    response = requests.get(base_url + urlencode(params))
    try:
        if format in ['simple', 'json', 'xml']:
            return response.text
        else:
            return {"error": "Unsupported format", "response": response.text}
    except Exception as e:
        return {"error": str(e), "response": response.text}