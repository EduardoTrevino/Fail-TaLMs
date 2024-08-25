import requests
from typing import Optional, Dict, Union

# Default API key
toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

def retrieve_metadata(url: str, adblock: Optional[bool] = True, animations: Optional[bool] = False, audio: Optional[bool] = False, colors: Optional[bool] = True) -> Dict:
    """
    Retrieve metadata from any link using the Microlink API.
    
    :param url: The URL to retrieve metadata for.
    :param adblock: Allows/disallows third-party ad requests (default is True).
    :param animations: Enables/disables CSS animations (default is False).
    :param audio: Enables audio source detection (default is False).
    :param colors: Colorize output (default is True).
    :return: JSON response with metadata.
    """
    endpoint = "https://api.microlink.io"
    params = {
        'url': url,
        'adblock': adblock,
        'animations': animations,
        'audio': audio,
        'colors': colors
    }
    response = requests.get(endpoint, params=params)
    return response.json()


def take_screenshot(url: str, screenshot: bool = True) -> Dict:
    """
    Take a screenshot of the target website.
    
    :param url: The URL of the website to screenshot.
    :param screenshot: Boolean to take a screenshot (default is True).
    :return: JSON response with screenshot data.
    """
    endpoint = "https://api.microlink.io"
    params = {
        'url': url,
        'screenshot': screenshot
    }
    response = requests.get(endpoint, params=params)
    return response.json()


def filter_data(url: str, filter: str) -> Dict:
    """
    Filter specific data fields from the response payload.
    
    :param url: The URL to process.
    :param filter: Comma-separated list of data fields to include.
    :return: Filtered JSON response.
    """
    endpoint = "https://api.microlink.io"
    params = {
        'url': url,
        'filter': filter
    }
    response = requests.get(endpoint, params=params)
    return response.json()


def execute_custom_query(url: str, additional_params: Dict[str, Union[str, bool]]) -> Dict:
    """
    Execute a custom query with additional parameters.
    
    :param url: The target URL.
    :param additional_params: Dictionary of additional query parameters.
    :return: JSON response based on the custom query.
    """
    endpoint = "https://api.microlink.io"
    params = {'url': url}
    params.update(additional_params)
    response = requests.get(endpoint, params=params)
    return response.json()