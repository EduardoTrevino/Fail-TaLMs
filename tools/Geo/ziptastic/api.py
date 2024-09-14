import requests


def get_location_by_zip(zipcode: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches the country, state, and city for the given ZIP code.
    
    Parameters:
    zipcode: str - The ZIP code to query.
    toolbench_rapidapi_key: str - Your API key for authentication.
    
    Returns:
    dict - The location information including country, state, and city.
    """
    url = f"http://ZiptasticAPI.com/{zipcode}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}