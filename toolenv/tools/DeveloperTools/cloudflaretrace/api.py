import requests
import json
from datetime import datetime
import os

from typing import Optional, Dict, Union, List

def trace(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get IP address, timestamp, user agent, country code, and more from Cloudflare.
    """
    url = "https://one.one.one.one/cdn-cgi/trace"

    response = requests.get(url)
    try:
        observation = response.text
        # Parsing the response to return it as a dictionary
        observation_dict = dict(line.split('=') for line in observation.splitlines())
    except:
        observation_dict = {"error": "Failed to parse response"}

    return observation_dict


def trace_alt(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Alternative endpoint to get IP address, timestamp, user agent, country code, and more data from Cloudflare.
    """
    url = "https://1.0.0.1/cdn-cgi/trace"

    response = requests.get(url)
    try:
        observation = response.text
        # Parsing the response to return it as a dictionary
        observation_dict = dict(line.split('=') for line in observation.splitlines())
    except:
        observation_dict = {"error": "Failed to parse response"}

    return observation_dict
