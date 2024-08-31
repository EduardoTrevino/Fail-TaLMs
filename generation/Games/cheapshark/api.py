import requests
from typing import Optional, List, Dict, Union

def edit_alert(action: str, email: str, game_id: int, price: Optional[float] = None, toolbench_rapidapi_key: str = '') -> bool:
    """
    Set or delete a price alert.

    Parameters:
    - action (str): The action to take on the price alert ('set' or 'delete').
    - email (str): A valid email address.
    - game_id (int): An existing game ID.
    - price (Optional[float]): The price to wait for, required when setting an alert.
    - toolbench_rapidapi_key (str): Not used.

    Returns:
    - bool: True if the action was successful, otherwise False.
    """
    url = "https://www.cheapshark.com/api/1.0/alerts"
    params = {
        'action': action,
        'email': email,
        'gameID': game_id
    }
    if action == 'set' and price is not None:
        params['price'] = price

    response = requests.get(url, params=params)
    return response.text.lower() == 'true'


def manage_alerts(email: str, toolbench_rapidapi_key: str = '') -> str:
    """
    Send an email containing a link to manage your alerts.

    Parameters:
    - email (str): A valid email address with existing alerts.
    - toolbench_rapidapi_key (str): Not used.

    Returns:
    - str: A response indicating the result of the action.
    """
    url = "https://www.cheapshark.com/api/1.0/alerts"
    params = {
        'action': 'manage',
        'email': email
    }

    response = requests.get(url, params=params)
    return response.text


def get_alerts(key: str, toolbench_rapidapi_key: str = '') -> Union[List[Dict[str, str]], str]:
    """
    Retrieve all existing alerts.

    Parameters:
    - key (str): The key parameter from your manage link (received via email).
    - toolbench_rapidapi_key (str): Not used.

    Returns:
    - List[Dict[str, str]]: A list of alerts if the key is valid.
    - str: An error message if the key is invalid.
    """
    url = "https://www.cheapshark.com/api/1.0/alerts"
    params = {
        'action': 'get',
        'key': key
    }

    response = requests.get(url, params=params)
    try:
        return response.json()
    except ValueError:
        return response.text
