import requests
from typing import Optional

BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"

def decode_vin(vin: str, modelyear: Optional[int] = None, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Decode a VIN (Vehicle Identification Number) to get detailed vehicle information.
    """
    url = f"{BASE_URL}/DecodeVin/{vin}"
    params = {'format': format}
    if modelyear:
        params['modelyear'] = modelyear
    response = requests.get(url, params=params)
    return response.json()

def decode_vin_values(vin: str, modelyear: Optional[int] = None, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Decode a VIN and provide data in a flat format.
    """
    url = f"{BASE_URL}/DecodeVinValues/{vin}"
    params = {'format': format}
    if modelyear:
        params['modelyear'] = modelyear
    response = requests.get(url, params=params)
    return response.json()

def decode_vin_extended(vin: str, modelyear: Optional[int] = None, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Decode a VIN with extended data information.
    """
    url = f"{BASE_URL}/DecodeVinExtended/{vin}"
    params = {'format': format}
    if modelyear:
        params['modelyear'] = modelyear
    response = requests.get(url, params=params)
    return response.json()

def decode_vin_values_extended(vin: str, modelyear: Optional[int] = None, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Decode a VIN in a flat format with extended data information.
    """
    url = f"{BASE_URL}/DecodeVinValuesExtended/{vin}"
    params = {'format': format}
    if modelyear:
        params['modelyear'] = modelyear
    response = requests.get(url, params=params)
    return response.json()

def decode_wmi(wmi: str, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Decode the World Manufacturer Identifier (WMI).
    """
    url = f"{BASE_URL}/DecodeWMI/{wmi}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_wmis_for_manufacturer(manufacturer: str, vehicle_type: Optional[str] = None, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the World Manufacturer Identifier (WMI) for a specified manufacturer.
    """
    url = f"{BASE_URL}/GetWMIsForManufacturer/{manufacturer}"
    params = {'format': format}
    if vehicle_type:
        params['vehicleType'] = vehicle_type
    response = requests.get(url, params=params)
    return response.json()

def get_all_makes(format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all the Makes available.
    """
    url = f"{BASE_URL}/GetAllMakes"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_parts(type: int, from_date: Optional[str] = None, to_date: Optional[str] = None, manufacturer: Optional[str] = None, format: str = 'json', page: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of ORGs with letter date in the given range of the dates and with specified Type of ORG.
    """
    url = f"{BASE_URL}/GetParts"
    params = {
        'type': type,
        'format': format,
        'page': page
    }
    if from_date:
        params['fromDate'] = from_date
    if to_date:
        params['toDate'] = to_date
    if manufacturer:
        params['manufacturer'] = manufacturer
    response = requests.get(url, params=params)
    return response.json()

def get_all_manufacturers(manufacturer_type: Optional[str] = None, page: int = 1, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all the Manufacturers available, optionally filtered by Manufacturer Type.
    """
    url = f"{BASE_URL}/GetAllManufacturers"
    params = {
        'page': page,
        'format': format
    }
    if manufacturer_type:
        params['ManufacturerType'] = manufacturer_type
    response = requests.get(url, params=params)
    return response.json()

def get_manufacturer_details(manufacturer: str, page: Optional[int] = None, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the details for a specific manufacturer.
    """
    url = f"{BASE_URL}/GetManufacturerDetails/{manufacturer}"
    params = {'format': format}
    if page:
        params['page'] = page
    response = requests.get(url, params=params)
    return response.json()

def get_make_for_manufacturer(manufacturer: str, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all the Makes for a specified manufacturer.
    """
    url = f"{BASE_URL}/GetMakeForManufacturer/{manufacturer}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_makes_for_manufacturer_and_year(manufacturer: str, year: int, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all the Makes for a specified manufacturer and year.
    """
    url = f"{BASE_URL}/GetMakesForManufacturerAndYear/{manufacturer}"
    params = {'year': year, 'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_makes_for_vehicle_type(vehicle_type: str, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all the Makes for a specified vehicle type.
    """
    url = f"{BASE_URL}/GetMakesForVehicleType/{vehicle_type}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_vehicle_types_for_make(make: str, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all the Vehicle Types for a specified Make.
    """
    url = f"{BASE_URL}/GetVehicleTypesForMake/{make}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_vehicle_types_for_make_id(make_id: int, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all the Vehicle Types for a specified Make ID.
    """
    url = f"{BASE_URL}/GetVehicleTypesForMakeId/{make_id}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_equipment_plant_codes(year: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get assigned Equipment Plant Codes by Year.
    """
    url = f"{BASE_URL}/GetEquipmentPlantCodes/{year}"
    params = {'format': 'json'}
    response = requests.get(url, params=params)
    return response.json()

def get_models_for_make(make: str, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the Models for a specified Make.
    """
    url = f"{BASE_URL}/GetModelsForMake/{make}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_models_for_make_id(make_id: int, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the Models for a specified Make ID.
    """
    url = f"{BASE_URL}/GetModelsForMakeId/{make_id}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_models_for_make_year(make: str, modelyear: Optional[int] = None, vehicletype: Optional[str] = None, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the Models for a specified Make by Year and Vehicle Type.
    """
    url = f"{BASE_URL}/GetModelsForMakeYear/make/{make}"
    if modelyear:
        url += f"/modelyear/{modelyear}"
    if vehicletype:
        url += f"/vehicletype/{vehicletype}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_vehicle_variable_list(format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all the vehicle-related variables.
    """
    url = f"{BASE_URL}/GetVehicleVariableList"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def get_vehicle_variable_values_list(variable: str, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all the accepted values for a given vehicle variable.
    """
    url = f"{BASE_URL}/GetVehicleVariableValuesList/{variable}"
    params = {'format': format}
    response = requests.get(url, params=params)
    return response.json()

def decode_vin_values_batch(vins: str, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Decode multiple VINs in batch, separated by semicolon and model year.
    """
    url = f"{BASE_URL}/DecodeVINValuesBatch/"
    headers = {'Content-Type': 'application/json'}
    params = {'format': format}
    data = vins  # Send string of VINs
    response = requests.post(url, headers=headers, params=params, data=data)
    return response.json()

def get_canadian_vehicle_specifications(year: int, make: str, model: Optional[str] = None, units: Optional[str] = 'Metric', format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Canadian vehicle specifications.
    """
    url = f"{BASE_URL}/GetCanadianVehicleSpecifications/"
    params = {
        'year': year,
        'make': make,
        'units': units,
        'format': format
    }
    if model:
        params['model'] = model
    response = requests.get(url, params=params)
    return response.json()