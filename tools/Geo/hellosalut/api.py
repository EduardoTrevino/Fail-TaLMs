import requests
from typing import Optional

def say_hello(lang: Optional[str] = None, ip: Optional[str] = None, cc: Optional[str] = None, mode: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint to get a greeting in the appropriate language based on provided language code, IP address, country code, or automatic detection mode.
    Parameters:
    lang [Optional]: string - Language code (e.g., 'en', 'ja', 'fr').
    ip [Optional]: string - IP address of the user (e.g., '89.120.120.120').
    cc [Optional]: string - Country code (e.g., 'nl').
    mode [Optional]: string - Automatic mode detection (e.g., 'auto').
    """
    url = "https://hellosalut.stefanbohacek.dev/"
    params = {}

    if lang:
        params['lang'] = lang
    if ip:
        params['ip'] = ip
    if cc:
        params['cc'] = cc
    if mode:
        params['mode'] = mode

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}