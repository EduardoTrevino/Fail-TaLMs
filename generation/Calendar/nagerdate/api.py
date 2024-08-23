import requests
from typing import Optional, List


def get_country_info(country_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get country info for the given country.
    Parameters:
        country_code (str): Country code (ISO 3166-1 alpha-2)
        toolbench_rapidapi_key (str): API key
    """
    url = f"https://date.nager.at/api/v3/CountryInfo/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_available_countries(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all available countries.
    Parameters:
        toolbench_rapidapi_key (str): API key
    """
    url = "https://date.nager.at/api/v3/AvailableCountries"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_long_weekends(year: int, country_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get long weekends for a given country.
    Parameters:
        year (int): Year to query.
        country_code (str): Country code (ISO 3166-1 alpha-2)
        toolbench_rapidapi_key (str): API key
    """
    url = f"https://date.nager.at/api/v3/LongWeekend/{year}/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_public_holidays(year: int, country_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get public holidays for a given year and country.
    Parameters:
        year (int): Year to query.
        country_code (str): Country code (ISO 3166-1 alpha-2)
        toolbench_rapidapi_key (str): API key
    """
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def is_today_public_holiday(country_code: str, county_code: Optional[str] = None, offset: Optional[int] = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Check if today is a public holiday.
    Parameters:
        country_code (str): Country code (ISO 3166-1 alpha-2)
        county_code (Optional[str]): Federal State Code.
        offset (Optional[int]): UTC timezone offset. Default 0.
        toolbench_rapidapi_key (str): API key
    """
    url = f"https://date.nager.at/api/v3/IsTodayPublicHoliday/{country_code}"
    params = {}
    if county_code:
        params["countyCode"] = county_code
    if offset:
        params["offset"] = offset

    response = requests.get(url, params=params)
    return {"status_code": response.status_code}


def get_next_public_holidays(country_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the upcoming public holidays for the next 365 days for the given country.
    Parameters:
        country_code (str): Country code (ISO 3166-1 alpha-2)
        toolbench_rapidapi_key (str): API key
    """
    url = f"https://date.nager.at/api/v3/NextPublicHolidays/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_next_public_holidays_worldwide(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the upcoming public holidays for the next 7 days worldwide.
    Parameters:
        toolbench_rapidapi_key (str): API key
    """
    url = "https://date.nager.at/api/v3/NextPublicHolidaysWorldwide"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_version(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the version of the used Nager.Date library.
    Parameters:
        toolbench_rapidapi_key (str): API key
    """
    url = "https://date.nager.at/api/v3/Version"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}