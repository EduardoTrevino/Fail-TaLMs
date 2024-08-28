import requests
from typing import Optional, List
import json

# Endpoint functions for OpenSenseMap API


def get_boxes(sense_box_id: str, format: Optional[str] = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get information about a single senseBox.
    
    Parameters:
    sense_box_id [Required]: string : the ID of the senseBox you are referring to.
    format [Optional]: string : The format the sensor data is returned in.
    """
    url = f"https://api.opensensemap.org/boxes/{sense_box_id}"
    params = {'format': format}
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_all_boxes(name: Optional[str] = None, limit: Optional[int] = 5, date: Optional[str] = None, phenomenon: Optional[str] = None, 
                  format: Optional[str] = 'json', grouptag: Optional[str] = None, model: Optional[str] = None, classify: Optional[bool] = False, 
                  minimal: Optional[bool] = False, full: Optional[bool] = False, near: Optional[str] = None, max_distance: Optional[int] = 1000,
                  exposure: Optional[str] = None, bbox: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all senseBoxes.
    
    Parameters:
    name [Optional]: string : Search string to find boxes by name, if specified all other parameters are ignored.
    limit [Optional]: number : Limit the search results.
    date [Optional]: RFC3339Date : Dates around which boxes should provide measurements.
    phenomenon [Optional]: string : A sensor phenomenon such as temperature, humidity or UV intensity.
    format [Optional]: string : The format the sensor data is returned in.
    etc...
    """
    url = "https://api.opensensemap.org/boxes"
    params = {
        'name': name,
        'limit': limit,
        'date': date,
        'phenomenon': phenomenon,
        'format': format,
        'grouptag': grouptag,
        'model': model,
        'classify': classify,
        'minimal': minimal,
        'full': full,
        'near': near,
        'maxDistance': max_distance,
        'exposure': exposure,
        'bbox': bbox
    }
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_locations(sense_box_id: str, format: Optional[str] = 'json', from_date: Optional[str] = None, to_date: Optional[str] = None,
                  toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all locations of the specified senseBox.
    
    Parameters:
    sense_box_id [Required]: string : The ID of the senseBox you are referring to.
    format [Optional]: string : The format the data is returned in.
    from_date [Optional]: RFC3339Date : Beginning date of location timestamps.
    to_date [Optional]: RFC3339Date : End date of location timestamps.
    """
    url = f"https://api.opensensemap.org/boxes/{sense_box_id}/locations"
    params = {'format': format, 'from-date': from_date, 'to-date': to_date}
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_idw_statistics(bbox: str, phenomenon: str, from_date: Optional[str] = None, to_date: Optional[str] = None, grid_type: Optional[str] = 'hex',
                       cell_width: Optional[int] = 50, power: Optional[int] = 1, num_timesteps: Optional[int] = 6, num_classes: Optional[int] = 6,
                       exposure: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a Inverse Distance Weighting Interpolation as FeatureCollection.
    
    Parameters:
    bbox [Required]: string : A bounding box containing 4 WGS84 coordinates.
    phenomenon [Required]: string : The name of the phenomenon you want to download the data for.
    from_date [Optional]: RFC3339Date : Beginning date of measurement data.
    to_date [Optional]: RFC3339Date : End date of measurement data.
    etc...
    """
    url = "https://api.opensensemap.org/statistics/idw"
    params = {
        'bbox': bbox,
        'phenomenon': phenomenon,
        'from-date': from_date,
        'to-date': to_date,
        'gridType': grid_type,
        'cellWidth': cell_width,
        'power': power,
        'numTimeSteps': num_timesteps,
        'numClasses': num_classes,
        'exposure': exposure
    }
    
    response = requests.get(url, params=params)
    try:
        return str(json.dumps(response.json()))
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_statistics_descriptive(box_id: str, phenomenon: str, from_date: str, to_date: str, operation: str, window: str,
                               download: Optional[bool] = True, columns: Optional[str] = None, format: Optional[str] = 'csv',
                               bbox: Optional[str] = None, exposure: Optional[str] = None, delimiter: Optional[str] = 'comma',
                               toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Compute basic descriptive statistics over specified time windows.
    
    Parameters:
    box_id [Required]: string : Comma separated list of senseBox IDs.
    phenomenon [Required]: string : The name of the phenomenon you want to download the data for.
    from_date [Required]: RFC3339Date : Beginning date of measurement data.
    to_date [Required]: RFC3339Date : End date of measurement data.
    etc...
    """
    url = "https://api.opensensemap.org/statistics/descriptive"
    params = {
        'boxId': box_id,
        'phenomenon': phenomenon,
        'from-date': from_date,
        'to-date': to_date,
        'operation': operation,
        'window': window,
        'download': download,
        'columns': columns,
        'format': format,
        'bbox': bbox,
        'exposure': exposure,
        'delimiter': delimiter
    }
    
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_latest_measurements_for_sensor(sense_box_id: str, sensor_id: str, from_date: Optional[str] = None, to_date: Optional[str] = None,
                                       format: Optional[str] = 'json', download: Optional[bool] = False, outliers: Optional[str] = None,
                                       outlier_window: Optional[int] = 15, delimiter: Optional[str] = 'comma',
                                       toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the 10000 latest measurements for a sensor.
    
    Parameters:
    sense_box_id [Required]: string : The ID of the senseBox you are referring to.
    sensor_id [Required]: string : The ID of the sensor you are referring to.
    from_date [Optional]: RFC3339Date : Beginning date of measurement data.
    to_date [Optional]: RFC3339Date : End date of measurement data.
    etc...
    """
    url = f"https://api.opensensemap.org/boxes/{sense_box_id}/data/{sensor_id}"
    params = {
        'from-date': from_date,
        'to-date': to_date,
        'format': format,
        'download': download,
        'outliers': outliers,
        'outlier-window': outlier_window,
        'delimiter': delimiter
    }
    
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.content
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_latest_measurements_for_phenomenon(box_id: str, phenomenon: str, from_date: Optional[str] = None, to_date: Optional[str] = None,
                                           format: Optional[str] = 'csv', columns: Optional[str] = 'sensorId,createdAt,value,lat,lon',
                                           download: Optional[bool] = True, delimiter: Optional[str] = 'comma', bbox: Optional[str] = None,
                                           exposure: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get latest measurements for a phenomenon as CSV.
    
    Parameters:
    box_id [Required]: string : Comma separated list of senseBox IDs.
    phenomenon [Required]: string : The name of the phenomenon you want to download the data for.
    from_date [Optional]: RFC3339Date : Beginning date of measurement data.
    to_date [Optional]: RFC3339Date : End date of measurement data.
    etc...
    """
    url = "https://api.opensensemap.org/boxes/data"
    params = {
        'boxId': box_id,
        'from-date': from_date,
        'to-date': to_date,
        'phenomenon': phenomenon,
        'format': format,
        'columns': columns,
        'download': download,
        'delimiter': delimiter,
        'bbox': bbox,
        'exposure': exposure
    }
    
    response = requests.get(url, params=params)
    try:
        return response.json() if format == 'json' else response.content
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_latest_measurements_of_sense_box(sense_box_id: str, count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the latest measurements of all sensors of the specified senseBox.
    
    Parameters:
    senseBoxId [Required]: string : The ID of the senseBox you are referring to.
    count [Optional]: number : Number of measurements to be retrieved for every sensor.
    """
    url = f"https://api.opensensemap.org/boxes/{sense_box_id}/sensors"
    params = {'count': count}
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


# def get_latest_measurements_of_sensor(sense_box_id: str, sensor_id: str, only_value: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Get the latest measurements of a sensor.
    
#     Parameters:
#     senseBoxId [Required]: string : The ID of the senseBox you are referring to.
#     sensorId [Required]: string : The ID of the sensor you are referring to.
#     onlyValue [Optional]: boolean : If true, only returns the measured value.
#     """
#     url = f"https://api.opensensemap.org/boxes/{sense_box_id}/sensors/{sensor_id}"
#     params = {'onlyValue': only_value}
    
#     response = requests.get(url, params=params)
#     try:
#         return response.json()
#     except Exception as e:
#         return {"error": str(e), "response": response.text}


def get_stats(human: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get some statistics about the database.
    
    Parameters:
    human [Optional]: boolean : If true, makes numbers easier human readable.
    """
    url = "https://api.opensensemap.org/stats"
    params = {'human': human}
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def print_routes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Print all routes of this API in human readable format.
    """
    url = "https://api.opensensemap.org/"
    
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}
    
# print(get_idw_statistics("7.6,51.2,7.8,51.4", "Temperatur"))
# print(get_latest_measurements_of_sensor("57000b8745fd40c8196ad04c", "57000b8745fd40c8196ad050"))