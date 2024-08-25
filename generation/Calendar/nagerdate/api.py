import requests

def public_holidays(year: int, country_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the public holidays for a given year and country.
    
    :param year: The year to retrieve public holidays for.
    :param country_code: The ISO 3166-1 alpha-2 country code.
    """
    url = f"https://date.nager.at/api/v3/publicholidays/{year}/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def country_info(country_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get country info for the given country.
    
    :param country_code: The ISO 3166-1 alpha-2 country code.
    """
    url = f"https://date.nager.at/api/v3/CountryInfo/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def available_countries(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all available countries.
    """
    url = "https://date.nager.at/api/v3/AvailableCountries"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def long_weekends(year: int, country_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get long weekends for a given year and country.
    
    :param year: The year to check for long weekends.
    :param country_code: The ISO 3166-1 alpha-2 country code.
    """
    url = f"https://date.nager.at/api/v3/LongWeekend/{year}/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def is_today_public_holiday(country_code: str, county_code: str = None, offset: int = 0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Check if today is a public holiday.
    
    :param country_code: The ISO 3166-1 alpha-2 country code.
    :param county_code: Optional federal state code.
    :param offset: UTC timezone offset.
    """
    url = f"https://date.nager.at/api/v3/IsTodayPublicHoliday/{country_code}"
    params = {'countyCode': county_code, 'offset': offset}
    response = requests.get(url, params=params)
    
    # Return HTTP status code for specific holiday check responses
    return response.status_code == 200

def next_public_holidays(country_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the upcoming public holidays for the next 365 days for the given country.
    
    :param country_code: The ISO 3166-1 alpha-2 country code.
    """
    url = f"https://date.nager.at/api/v3/NextPublicHolidays/{country_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def next_public_holidays_worldwide(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the upcoming public holidays worldwide for the next 7 days.
    """
    url = "https://date.nager.at/api/v3/NextPublicHolidaysWorldwide"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def version(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the version of the used Nager.Date library.
    """
    url = "https://date.nager.at/api/v3/Version"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}