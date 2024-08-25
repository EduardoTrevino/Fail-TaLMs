import requests
from typing import Optional


def get_current_intensity(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data for the current half hour.
    """
    url = "https://api.carbonintensity.org.uk/intensity"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_by_date(date: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data for a specific date.
    :param date: Date in YYYY-MM-DD format.
    """
    url = f"https://api.carbonintensity.org.uk/intensity/date/{date}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_by_date_period(date: str, period: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data for a specific date and half hour settlement period.
    :param date: Date in YYYY-MM-DD format.
    :param period: Half hour settlement period between 1-48.
    """
    url = f"https://api.carbonintensity.org.uk/intensity/date/{date}/{period}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_factors(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity factors for each fuel type.
    """
    url = "https://api.carbonintensity.org.uk/intensity/factors"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_specific_period(from_time: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data for a specific half-hour period.
    :param from_time: Datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    """
    url = f"https://api.carbonintensity.org.uk/intensity/{from_time}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_24h_forward(from_time: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data 24hrs forward from a specific datetime.
    :param from_time: Start datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    """
    url = f"https://api.carbonintensity.org.uk/intensity/{from_time}/fw24h"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_48h_forward(from_time: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data 48hrs forward from a specific datetime.
    :param from_time: Start datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    """
    url = f"https://api.carbonintensity.org.uk/intensity/{from_time}/fw48h"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_24h_past(from_time: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data 24hrs in the past from a specific datetime.
    :param from_time: Start datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    """
    url = f"https://api.carbonintensity.org.uk/intensity/{from_time}/pt24h"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_between(from_time: str, to_time: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data between specified datetimes.
    :param from_time: Start datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    :param to_time: End datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    """
    url = f"https://api.carbonintensity.org.uk/intensity/{from_time}/{to_time}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_intensity_statistics(from_time: str, to_time: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity statistics (average, max, min) between specified datetimes.
    :param from_time: Start datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    :param to_time: End datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    """
    url = f"https://api.carbonintensity.org.uk/intensity/stats/{from_time}/{to_time}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_generation_mix_current(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get generation mix for the current half hour.
    """
    url = "https://api.carbonintensity.org.uk/generation"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_generation_mix_24h_past(from_time: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get generation mix for the past 24 hours.
    :param from_time: Datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    """
    url = f"https://api.carbonintensity.org.uk/generation/{from_time}/pt24h"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_generation_mix_between(from_time: str, to_time: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get generation mix between specified datetimes.
    :param from_time: Start datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    :param to_time: End datetime in ISO8601 format YYYY-MM-DDThh:mmZ.
    """
    url = f"https://api.carbonintensity.org.uk/generation/{from_time}/{to_time}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_regional_intensity(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data for current half hour for GB regions.
    """
    url = "https://api.carbonintensity.org.uk/regional"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_regional_intensity_postcode(postcode: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data for current half hour for specified postcode.
    :param postcode: Outward postcode i.e. RG41 or SW1 or TF8.
    """
    url = f"https://api.carbonintensity.org.uk/regional/postcode/{postcode}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_regional_intensity_regionid(regionid: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Carbon Intensity data for current half hour for specified region.
    :param regionid: Region ID of GB region.
    """
    url = f"https://api.carbonintensity.org.uk/regional/regionid/{regionid}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}