import requests
from typing import Optional


def get_exchange_rate_table(table: str, top_count: Optional[int] = None, date: Optional[str] = None,
                            start_date: Optional[str] = None, end_date: Optional[str] = None,
                            toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch a complete table of exchange rates of type {table}.
    
    :param table: table type ('A', 'B', or 'C')
    :param top_count: a number determining the maximum size of the returned data series
    :param date: a specific date in 'YYYY-MM-DD' format
    :param start_date: start date in 'YYYY-MM-DD' for a series of data
    :param end_date: end date in 'YYYY-MM-DD' for a series of data
    :return: JSON response from the API
    """
    base_url = f"http://api.nbp.pl/api/exchangerates/tables/{table}"
    
    if date:
        url = f"{base_url}/{date}/"
    elif start_date and end_date:
        url = f"{base_url}/{start_date}/{end_date}/"
    elif top_count:
        url = f"{base_url}/last/{top_count}/"
    else:
        url = base_url

    params = {'format': 'json'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_currency_exchange_rate(table: str, code: str, top_count: Optional[int] = None, date: Optional[str] = None,
                               start_date: Optional[str] = None, end_date: Optional[str] = None,
                               toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the exchange rate of a specific currency from a table.
    
    :param table: table type ('A', 'B', or 'C')
    :param code: currency code (ISO 4217 standard)
    :param top_count: a number determining the maximum size of the returned data series
    :param date: a specific date in 'YYYY-MM-DD' format
    :param start_date: start date in 'YYYY-MM-DD' for a series of data
    :param end_date: end date in 'YYYY-MM-DD' for a series of data
    :return: JSON response from the API
    """
    base_url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{code}"
    
    if date:
        url = f"{base_url}/{date}/"
    elif start_date and end_date:
        url = f"{base_url}/{start_date}/{end_date}/"
    elif top_count:
        url = f"{base_url}/last/{top_count}/"
    else:
        url = base_url

    params = {'format': 'json'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_gold_price(top_count: Optional[int] = None, date: Optional[str] = None,
                   start_date: Optional[str] = None, end_date: Optional[str] = None,
                   toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the price of gold.
    
    :param top_count: a number determining the maximum size of the returned data series
    :param date: a specific date in 'YYYY-MM-DD' format
    :param start_date: start date in 'YYYY-MM-DD' for a series of data
    :param end_date: end date in 'YYYY-MM-DD' for a series of data
    :return: JSON response from the API
    """
    base_url = "http://api.nbp.pl/api/cenyzlota"
    
    if date:
        url = f"{base_url}/{date}"
    elif start_date and end_date:
        url = f"{base_url}/{start_date}/{end_date}"
    elif top_count:
        url = f"{base_url}/last/{top_count}"
    else:
        url = base_url

    params = {'format': 'json'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}