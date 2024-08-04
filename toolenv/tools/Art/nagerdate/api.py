import requests
import json
from typing import Optional, Dict, Union, List

def get_public_holidays(year: int, country_code: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, List]:
    """
    Get the public holidays for a specific year and country.
    
    :param year: The year for which to retrieve public holidays.
    :param country_code: The ISO 3166-1 alpha-2 country code.
    :return: The response from the API.
    """
    url = f"https://date.nager.at/api/v3/publicholidays/{year}/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def get_long_weekends(year: int, country_code: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, List]:
    """
    Get the long weekends for a specific year and country.
    
    :param year: The year for which to retrieve long weekends.
    :param country_code: The ISO 3166-1 alpha-2 country code.
    :return: The response from the API.
    """
    url = f"https://date.nager.at/api/v3/LongWeekend/{year}/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def get_next_public_holidays(country_code: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, List]:
    """
    Returns the upcoming public holidays for the next 365 days for the given country.
    
    :param country_code: The ISO 3166-1 alpha-2 country code.
    :return: The response from the API.
    """
    url = f"https://date.nager.at/api/v3/NextPublicHolidays/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def is_today_public_holiday(country_code: str, offset: int = 0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Union[Dict, List]:
    """
    Checks if today is a public holiday in the given country.
    
    :param country_code: The ISO 3166-1 alpha-2 country code.
    :param offset: UTC timezone offset. Default is 0.
    :return: The response from the API.
    """
    url = f"https://date.nager.at/api/v3/IsTodayPublicHoliday/{country_code}?offset={offset}"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text
