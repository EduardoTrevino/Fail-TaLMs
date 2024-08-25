import requests
from typing import Optional, List

def get_global_market_overview(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns current cryptocurrencies market overview metrics.
    """
    url = "https://api.coinpaprika.com/v1/global"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_coins(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns basic information about cryptocurrencies.
    """
    url = "https://api.coinpaprika.com/v1/coins"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_coin_by_id(coin_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns detailed information about a single coin.
    """
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_coin_twitter(coin_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the last 50 tweets from the official Twitter profile for a given coin.
    """
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/twitter"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_coin_events(coin_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns events for a given coin.
    """
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/events"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_exchanges_by_coin_id(coin_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns exchanges where a given coin is traded.
    """
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/exchanges"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_markets_by_coin_id(coin_id: str, quotes: Optional[str] = "USD", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns all available markets for a given coin.
    """
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/markets?quotes={quotes}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ohlc_last_day(coin_id: str, quote: Optional[str] = "usd", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns OHLC for the last full day.
    """
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/ohlcv/latest/?quote={quote}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ohlc_today(coin_id: str, quote: Optional[str] = "usd", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns OHLC for the current day.
    """
    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/ohlcv/today/?quote={quote}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_people(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns list of people related to the cryptocurrency market.
    """
    url = "https://api.coinpaprika.com/v1/people"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_person_by_id(person_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns information about a person with the specified ID.
    """
    url = f"https://api.coinpaprika.com/v1/people/{person_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_tags(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns basic information about cryptocurrencies tags.
    """
    url = "https://api.coinpaprika.com/v1/tags"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_tag_by_id(tag_id: str, additional_fields: Optional[str] = "", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns information about a given cryptocurrency tag.
    """
    url = f"https://api.coinpaprika.com/v1/tags/{tag_id}?additional_fields={additional_fields}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_tickers(quotes: Optional[str] = "USD", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns price data of all active cryptocurrencies.
    """
    url = f"https://api.coinpaprika.com/v1/tickers?quotes={quotes}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ticker_by_id(coin_id: str, quotes: Optional[str] = "USD", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns price data of a single cryptocurrency.
    """
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}?quotes={quotes}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_exchanges(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns basic information about exchanges.
    """
    url = "https://api.coinpaprika.com/v1/exchanges"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_exchange_by_id(exchange_id: str, quotes: Optional[str] = "USD", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns basic information about a given exchange.
    """
    url = f"https://api.coinpaprika.com/v1/exchanges/{exchange_id}?quotes={quotes}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_exchange_markets(exchange_id: str, quotes: Optional[str] = "USD", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns list of all available markets on a given exchange.
    """
    url = f"https://api.coinpaprika.com/v1/exchanges/{exchange_id}/markets?quotes={quotes}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search(query: str, categories: Optional[str] = "currencies,exchanges,icos,people,tags", limit: Optional[int] = 6, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns search results for a given query across multiple categories.
    """
    url = f"https://api.coinpaprika.com/v1/search?q={query}&c={categories}&limit={limit}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def price_converter(base_currency_id: str, quote_currency_id: str, amount: Optional[float] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Converts a set amount of base currency to quote currency.
    """
    url = f"https://api.coinpaprika.com/v1/price-converter?base_currency_id={base_currency_id}&quote_currency_id={quote_currency_id}&amount={amount}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_contracts(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns all available contract platforms.
    """
    url = "https://api.coinpaprika.com/v1/contracts"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_contracts_by_platform(platform_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns all available contracts for a given platform.
    """
    url = f"https://api.coinpaprika.com/v1/contracts/{platform_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def redirect_to_ticker_by_contract(platform_id: str, contract_address: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Redirects to ticker data for a contract with a given address.
    """
    url = f"https://api.coinpaprika.com/v1/contracts/{platform_id}/{contract_address}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_historical_ticks_by_contract(platform_id: str, contract_address: str, start: str, end: Optional[str] = "NOW", limit: Optional[int] = 1000, quote: Optional[str] = "usd", interval: Optional[str] = "5m", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns historical ticks for a contract with a given address.
    """
    url = f"https://api.coinpaprika.com/v1/contracts/{platform_id}/{contract_address}/historical?start={start}&end={end}&limit={limit}&quote={quote}&interval={interval}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}