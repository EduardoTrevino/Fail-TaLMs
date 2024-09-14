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

def get_tag_by_id(tag_id: str, additional_fields: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns information about a given cryptocurrency tag.
    - name
    - description
    - type of tag: technical or functional
    - number of coins with the tag
    - number of ICOs with the tag
    
    Parameters:
    - tag_id: str - The ID of the tag to retrieve information for.
    - additional_fields: Optional[str] - The additional fields to include in the response (supported: "coins", "icos").
    
    Returns:
    - JSON response from the API or an error message.
    """
    
    # Validate the additional_fields parameter
    if additional_fields is None:
        url = f"https://api.coinpaprika.com/v1/tags/{tag_id}"
    elif additional_fields in ["coins", "icos"]:
        url = f"https://api.coinpaprika.com/v1/tags/{tag_id}?additional_fields={additional_fields}"
    else:
        return {"error": f"Invalid additional_fields value: {additional_fields}. Supported values are 'coins', 'icos'."}
    
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

def get_ticker_by_id(coin_id: str, quotes: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns price data of a single cryptocurrency.

    Parameters:
    - coin_id: str - The ID of the cryptocurrency to retrieve data for (e.g., "btc-bitcoin").
    - quotes: Optional[str] - Comma-separated list of fiat currencies or other cryptocurrency symbols for price data 
      (e.g., "USD,EUR,BTC"). Up to 3 quotes at once. Allowed values include "BTC", "ETH", "USD", "EUR", "PLN", etc.

    Returns:
    - JSON response from the API or an error message.
    """

    # Construct the base URL
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    
   # Append the quotes parameter only if it's provided
    if quotes:
        # Validate quotes by splitting and checking each value
        allowed_quotes = sorted(["BTC", "ETH", "USD", "EUR", "PLN", "KRW", "GBP", "CAD", "JPY", "RUB", "TRY", "NZD", "AUD", 
                                 "CHF", "UAH", "HKD", "SGD", "NGN", "PHP", "MXN", "BRL", "THB", "CLP", "CNY", "CZK", "DKK", 
                                 "HUF", "IDR", "ILS", "INR", "MYR", "NOK", "PKR", "SEK", "TWD", "ZAR", "VND", "BOB", "COP", 
                                 "PEN", "ARS", "ISK"])

        invalid_quotes = [q for q in quotes.split(",") if q not in allowed_quotes]
        
        if invalid_quotes:
            allowed_quotes_str = ", ".join(allowed_quotes)
            return {"error": f"Invalid quote(s) provided: {', '.join(invalid_quotes)}. "
                             f"Allowed values are: {allowed_quotes_str}."}
        
        url += f"?quotes={quotes}"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 404:
            return {"error": f"Coin with ID '{coin_id}' not found."}
        elif response.status_code == 429:
            return {"error": "Too many requests. Please try again later."}
        elif response.status_code != 200:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}

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

def get_exchange_by_id(exchange_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns basic information about a given exchange.
    """
    url = f"https://api.coinpaprika.com/v1/exchanges/{exchange_id}"
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

def search(query: str, categories: Optional[str] = None, limit: Optional[int] = 6, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns search results for a given query across multiple categories.
    
    Parameters:
    - query: str - The search query (e.g., "btc").
    - categories: Optional[str] - Comma-separated list of categories to search (supported: "currencies", "exchanges", "icos", "people", "tags").
    - limit: Optional[int] - The maximum number of results per category (default: 6, max: 250).
    
    Returns:
    - JSON response from the API or an error message.
    """

    # Supported categories
    supported_categories = {"currencies", "exchanges", "icos", "people", "tags"}

    if categories is None:
        # No categories provided, only search by the query
        url = f"https://api.coinpaprika.com/v1/search?q={query}&limit={limit}"
    else:
        # Split and validate categories
        category_list = categories.split(",")
        for category in category_list:
            if category not in supported_categories:
                return {"error": f"Invalid category: {category}. Supported categories are 'currencies', 'exchanges', 'icos', 'people', 'tags'."}
        categories = ",".join(category_list)
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