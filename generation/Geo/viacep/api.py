import requests
from typing import Optional


def query_cep(cep: str, return_format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve information for a given ZIP code in Brazil.
    Parameters:
    cep [Required]: string [Description: ZIP code in the format of 8 digits.]
    return_format [Optional]: string [Description: Format of the return data (json or xml). Default is 'json'.]
    """
    if len(cep) != 8 or not cep.isdigit():
        return {"error": "Invalid ZIP code format. Must be 8 digits."}

    url = f"https://viacep.com.br/ws/{cep}/{return_format}/"
    response = requests.get(url)
    try:
        return response.json() if return_format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_address(state: str, city: str, street: str, return_format: str = 'json', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Search for a ZIP code based on the address details.
    Parameters:
    state [Required]: string [Description: Two-letter state code in Brazil.]
    city [Required]: string [Description: Name of the city. Must have at least 3 characters.]
    street [Required]: string [Description: Name of the street. Must have at least 3 characters.]
    return_format [Optional]: string [Description: Format of the return data (json or xml). Default is 'json'.]
    """
    if len(city) < 3 or len(street) < 3:
        return {"error": "City and street names must be at least 3 characters long."}

    url = f"https://viacep.com.br/ws/{state}/{city}/{street}/{return_format}/"
    response = requests.get(url)
    try:
        return response.json() if return_format == 'json' else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}