import requests
from typing import Optional

def coins_list(include_platform: bool = False, status: str = 'active', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: This endpoint allows you to query all the supported coins on CoinGecko with coin id, name and symbol.
    Parameters:
      include_platform [Optional]: boolean [Description: Include platform and token's contract addresses, default: false]
      status [Optional]: string [Description: Filter by status of coins, default: active]
    """
    url = "https://pro-api.coingecko.com/api/v3/coins/list"
    params = {
        'include_platform': include_platform,
        'status': status,
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def top_gainers_losers(vs_currency: str, duration: str = '24h', top_coins: str = '1000', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: This endpoint allows you to query the top 30 coins with large price gain and loss by a specific time duration.
    Parameters:
      vs_currency [Required]: string [Description: Target currency of coins e.g. usd, eur, jpy]
      duration [Optional]: string [Description: Filter result by time range, default: 24h]
      top_coins [Optional]: string [Description: Filter result by market cap ranking or all coins, default: 1000]
    """
    url = "https://pro-api.coingecko.com/api/v3/coins/top_gainers_losers"
    params = {
        'vs_currency': vs_currency,
        'duration': duration,
        'top_coins': top_coins
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def recently_added_coins(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: This endpoint allows you to query the latest 200 coins that recently listed on CoinGecko.
    """
    url = "https://pro-api.coingecko.com/api/v3/coins/list/new"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def coins_markets(vs_currency: str, ids: Optional[str] = None, category: Optional[str] = None, order: str = 'market_cap_desc', per_page: int = 100, page: int = 1, sparkline: bool = False, price_change_percentage: Optional[str] = None, locale: str = 'en', precision: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: This endpoint allows you to query all the supported coins with price, market cap, volume and market related data.
    Parameters:
      vs_currency [Required]: string [Description: Target currency of coins and market data]
      ids [Optional]: string [Description: Coins' ids, comma-separated if querying more than 1 coin.]
      category [Optional]: string [Description: Filter based on coins' category.]
      order [Optional]: string [Description: Sort result by field, default: market_cap_desc]
      per_page [Optional]: number [Description: Total results per page, default: 100]
      page [Optional]: number [Description: Page through results, default: 1]
      sparkline [Optional]: boolean [Description: Include sparkline 7 days data, default: false]
      price_change_percentage [Optional]: string [Description: Include price change percentage timeframe.]
      locale [Optional]: string [Description: Language background, default: en]
      precision [Optional]: string [Description: Decimal place for currency price value]
    """
    url = "https://pro-api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': vs_currency,
        'ids': ids,
        'category': category,
        'order': order,
        'per_page': per_page,
        'page': page,
        'sparkline': sparkline,
        'price_change_percentage': price_change_percentage,
        'locale': locale,
        'precision': precision
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def coin_data_by_id(id: str, localization: bool = True, tickers: bool = True, market_data: bool = True, community_data: bool = True, developer_data: bool = True, sparkline: bool = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: This endpoint allows you to query all the coin data of a coin (name, price, market including exchange tickers) on a specific CoinGecko coin page.
    Parameters:
      id [Required]: string [Description: Coin id]
      localization [Optional]: boolean [Description: Include all the localized languages in the response, default: true]
      tickers [Optional]: boolean [Description: Include tickers data, default: true]
      market_data [Optional]: boolean [Description: Include market data, default: true]
      community_data [Optional]: boolean [Description: Include community data, default: true]
      developer_data [Optional]: boolean [Description: Include developer data, default: true]
      sparkline [Optional]: boolean [Description: Include sparkline 7 days data, default: false]
    """
    url = f"https://pro-api.coingecko.com/api/v3/coins/{id}"
    params = {
        'localization': localization,
        'tickers': tickers,
        'market_data': market_data,
        'community_data': community_data,
        'developer_data': developer_data,
        'sparkline': sparkline
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}