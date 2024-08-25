import requests

def get_iss_location(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Returns the current location of the International Space Station (ISS).
    This API takes no inputs and returns the current latitude and longitude of the space station with a unix timestamp.
    """
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_people_in_space(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Returns the current number of people in space, along with their names and spacecraft if available.
    This API takes no inputs.
    """
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}