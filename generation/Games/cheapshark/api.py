import requests
from typing import Optional


def edit_alert(action: str, email: str, game_id: Optional[int] = None, price: Optional[float] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Set or delete a price alert for a specific game and price.
    Parameters:
    action [Required]: string (The action to take on the price alert, "set" or "delete")
    email [Required]: string (Any valid email address)
    game_id [Optional]: integer (An existing gameID, required for "set" and "delete")
    price [Optional]: decimal (The price to wait for, only required when using "set" value for action parameter)
    """
    url = "https://www.cheapshark.com/api/1.0/alerts"
    params = {
        'action': action,
        'email': email
    }
    if action == 'set':
        if game_id is not None and price is not None:
            params['gameID'] = game_id
            params['price'] = price
        else:
            raise ValueError("game_id and price are required when action is 'set'")
    elif action == 'delete':
        if game_id is not None:
            params['gameID'] = game_id
        else:
            raise ValueError("game_id is required when action is 'delete'")
    
    response = requests.get(url, params=params)
    return response.json()


def manage_alerts(email: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Send an email containing a link to manage your alerts.
    Parameters:
    email [Required]: string (Any valid email address with existing alerts)
    """
    url = "https://www.cheapshark.com/api/1.0/alerts"
    params = {
        'action': 'manage',
        'email': email
    }
    
    response = requests.get(url, params=params)
    return response.json()