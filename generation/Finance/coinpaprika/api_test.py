from api import *
import pytest

toolbench_rapidapi_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

def test_get_global_market_overview():
    response = get_global_market_overview(toolbench_rapidapi_key)
    assert 'market_cap_usd' in response

def test_list_coins():
    response = list_coins(toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_coin_by_id():
    coin_id = "btc-bitcoin"
    response = get_coin_by_id(coin_id, toolbench_rapidapi_key)
    assert response['id'] == coin_id

def test_get_coin_twitter():
    coin_id = "btc-bitcoin"
    response = get_coin_twitter(coin_id, toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_coin_events():
    coin_id = "btc-bitcoin"
    response = get_coin_events(coin_id, toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_exchanges_by_coin_id():
    coin_id = "btc-bitcoin"
    response = get_exchanges_by_coin_id(coin_id, toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_markets_by_coin_id():
    coin_id = "btc-bitcoin"
    response = get_markets_by_coin_id(coin_id, toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_ohlc_last_day():
    coin_id = "btc-bitcoin"
    response = get_ohlc_last_day(coin_id, toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_ohlc_today():
    coin_id = "btc-bitcoin"
    response = get_ohlc_today(coin_id, toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_list_people():
    response = list_people(toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_person_by_id():
    person_id = "vitalik-buterin"
    response = get_person_by_id(person_id, toolbench_rapidapi_key)
    assert response['id'] == person_id

def test_list_tags():
    response = list_tags(toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_tag_by_id():
    tag_id = "blockchain-service"
    response = get_tag_by_id(tag_id, toolbench_rapidapi_key)
    assert response['id'] == tag_id

def test_get_tickers():
    response = get_tickers(toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_ticker_by_id():
    coin_id = "btc-bitcoin"
    response = get_ticker_by_id(coin_id, toolbench_rapidapi_key)
    assert response['id'] == coin_id

def test_list_exchanges():
    response = list_exchanges(toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_exchange_by_id():
    exchange_id = "binance"
    response = get_exchange_by_id(exchange_id, toolbench_rapidapi_key)
    assert response['id'] == exchange_id

def test_list_exchange_markets():
    exchange_id = "binance"
    response = list_exchange_markets(exchange_id, toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_search():
    query = "bitcoin"
    response = search(query, toolbench_rapidapi_key)
    assert 'currencies' in response

def test_price_converter():
    response = price_converter("btc-bitcoin", "eth-ethereum", 1, toolbench_rapidapi_key)
    assert response['base_currency_id'] == "btc-bitcoin"

def test_list_contracts():
    response = list_contracts(toolbench_rapidapi_key)
    assert isinstance(response, list)

def test_get_contracts_by_platform():
    platform_id = "eth-ethereum"
    response = get_contracts_by_platform(platform_id, toolbench_rapidapi_key)
    assert isinstance(response, list)