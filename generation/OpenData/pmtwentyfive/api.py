import requests

def get_device_latest(device_id: str = '08BEAC0A08AE', format: str = 'JSON', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the latest measurement (within 2 hours) of the device.
    """
    url = f"https://pm25.lass-net.org/API-1.0.0/device/{device_id}/latest/"
    params = {'format': format}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_device_history(device_id: str = '08BEAC0A08AE', format: str = 'JSON', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the last 7-day measurement of the device.
    """
    url = f"https://pm25.lass-net.org/API-1.0.0/device/{device_id}/history/"
    params = {'format': format}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_device_date(device_id: str = '08BEAC0A08AE', yyyy_mm_dd: str = '2020-07-01', format: str = 'JSON', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the measurement of the device on the specified date.
    """
    url = f"https://pm25.lass-net.org/API-1.0.0/device/{device_id}/date/{yyyy_mm_dd}/"
    params = {'format': format}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_project_all(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the list of the projects.
    """
    url = "https://pm25.lass-net.org/API-1.0.0/project/all/"
    response = requests.get(url)
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_project_latest(project: str = 'airbox', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the latest measurement (within 2 hours) of the devices in the specified project.
    """
    url = f"https://pm25.lass-net.org/API-1.0.0/project/{project}/latest/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_analysis_adf_emission(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the list of devices that are probably located near emission sources detected by ADF (updated daily).
    """
    url = "https://pm25.lass-net.org/API-1.0.0/analysis/ADF/emission/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_analysis_adf_indoor(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the suspicious indoor devices detected by ADF (updated daily).
    """
    url = "https://pm25.lass-net.org/API-1.0.0/analysis/ADF/indoor/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_analysis_adf_pollution(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the list of devices with suspicious pollution ongoing in their nearby areas detected by ADF (updated hourly).
    """
    url = "https://pm25.lass-net.org/API-1.0.0/analysis/ADF/pollution/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_analysis_adf_ranking(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the ranking scores of all online devices (updated hourly).
    """
    url = "https://pm25.lass-net.org/API-1.0.0/analysis/ADF/ranking/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_analysis_dcf_latest(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the latest version calibration models made by DCF (updated daily).
    """
    url = "https://pm25.lass-net.org/API-1.0.0/analysis/DCF/latest/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_analysis_dcf_nearest(lat: float = 25.04, lon: float = 121.614, sensor: str = 'PMS5003', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the nearest reference site with DCF model to the specified GPS coordinates and sensor type.
    """
    url = f"https://pm25.lass-net.org/API-1.0.0/analysis/DCF/nearest/lat/{lat}/lon/{lon}/"
    params = {'sensor': sensor}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_citation(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the bibtex to cite this project.
    """
    url = "https://pm25.lass-net.org/API-1.0.0/citation/"
    response = requests.get(url)
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_citation_adf(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the bibtex to cite the ADF work.
    """
    url = "https://pm25.lass-net.org/API-1.0.0/citation/ADF/"
    response = requests.get(url)
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}