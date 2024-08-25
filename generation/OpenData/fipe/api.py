import requests
from typing import Optional

BASE_URL = "https://parallelum.com.br/fipe/api/v1"

def get_brands(vehicle_type: str = "carros", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the brands for the specified vehicle type.

    Parameters:
    vehicle_type [Optional]: str - Type of vehicle ('carros', 'motos', 'caminhoes').

    Returns:
    JSON response with list of vehicle brands.
    """
    url = f"{BASE_URL}/{vehicle_type}/marcas"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_models(brand_code: str, vehicle_type: str = "carros", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the models for a specified brand.

    Parameters:
    brand_code [Required]: str - Code of the brand.
    vehicle_type [Optional]: str - Type of vehicle ('carros', 'motos', 'caminhoes').

    Returns:
    JSON response with list of models and years available for the brand.
    """
    url = f"{BASE_URL}/{vehicle_type}/marcas/{brand_code}/modelos"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_years(brand_code: str, model_code: str, vehicle_type: str = "carros", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the years for a specified model.

    Parameters:
    brand_code [Required]: str - Code of the brand.
    model_code [Required]: str - Code of the model.
    vehicle_type [Optional]: str - Type of vehicle ('carros', 'motos', 'caminhoes').

    Returns:
    JSON response with list of years available for the model.
    """
    url = f"{BASE_URL}/{vehicle_type}/marcas/{brand_code}/modelos/{model_code}/anos"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_value(brand_code: str, model_code: str, year_code: str, vehicle_type: str = "carros", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the current price from FIPE table for a specified vehicle, model and year.

    Parameters:
    brand_code [Required]: str - Code of the brand.
    model_code [Required]: str - Code of the model.
    year_code [Required]: str - Code of the year.
    vehicle_type [Optional]: str - Type of vehicle ('carros', 'motos', 'caminhoes').

    Returns:
    JSON response with price details from FIPE table.
    """
    url = f"{BASE_URL}/{vehicle_type}/marcas/{brand_code}/modelos/{model_code}/anos/{year_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}