import requests
from typing import Optional

def get_global_stats(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve global crypto statistics.
    """
    url = "https://api.coinlore.net/api/global/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_all_tickers(start: Optional[int] = 0, limit: Optional[int] = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve tick data for multiple crypto coins, sorted by market cap.
    """
    url = f"https://api.coinlore.net/api/tickers/?start={start}&limit={limit}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ticker(coin_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve tick data for specific coin.
    """
    url = f"https://api.coinlore.net/api/ticker/?id={coin_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_markets_for_coin(coin_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve top 50 exchanges and markets for specific coin.
    """
    url = f"https://api.coinlore.net/api/coin/markets/?id={coin_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_all_exchanges(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all exchanges listed on the platform.
    """
    url = "https://api.coinlore.net/api/exchanges/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_exchange(exchange_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get specific exchange using ID, returns exchange info and top 100 pairs.
    """
    url = f"https://api.coinlore.net/api/exchange/?id={exchange_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_social_stats(coin_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get social stats for a specific coin.
    """
    url = f"https://api.coinlore.net/api/coin/social_stats/?id={coin_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}