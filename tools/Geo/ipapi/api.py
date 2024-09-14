import requests

def get_ip_location(ip: str, format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get complete location information for a specific IP address.
    
    Parameters:
    ip (str): The IP address to retrieve location for.
    format (str): The format of the response. Default is 'json'. Other formats include 'jsonp', 'xml', 'csv', and 'yaml'.
    
    Returns:
    dict or str: The response from the API in the specified format.
    """
    url = f"https://ipapi.co/{ip}/{format}/"
    response = requests.get(url)
    if format == 'json':
        return response.json()
    else:
        return response.text

def get_ip_location_field(ip: str, field: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a specific location field for a specific IP address.
    
    Parameters:
    ip (str): The IP address to retrieve the location field for.
    field (str): The specific field to retrieve.
    
    Returns:
    str: The value of the requested field.
    """
    url = f"https://ipapi.co/{ip}/{field}/"
    response = requests.get(url)
    return response.text

def get_client_ip_location(format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get complete location information for the client's IP address.
    
    Parameters:
    format (str): The format of the response. Default is 'json'. Other formats include 'jsonp', 'xml', 'csv', and 'yaml'.
    
    Returns:
    dict or str: The response from the API in the specified format.
    """
    url = f"https://ipapi.co/{format}/"
    response = requests.get(url)
    if format == 'json':
        return response.json()
    else:
        return response.text

def get_client_ip_location_field(field: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a specific location field for the client's IP address.
    
    Parameters:
    field (str): The specific field to retrieve.
    
    Returns:
    str: The value of the requested field.
    """
    url = f"https://ipapi.co/{field}/"
    response = requests.get(url)
    return response.text