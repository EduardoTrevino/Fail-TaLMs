import requests
from typing import Optional

def get_database(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches the entire election polls database from the DAWUM API, which includes comprehensive information 
    on various polls including parliament, institute, clients, survey results of parties, and more.

    :param toolbench_rapidapi_key: API key for accessing DAWUM API
    :return: JSON response with database information
    """
    url = "https://api.dawum.de/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_last_update(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches the last update date of the DAWUM election polls database to check for the most recent data.

    :param toolbench_rapidapi_key: API key for accessing DAWUM API
    :return: Text response with last update datetime
    """
    url = "https://api.dawum.de/last_update.txt"
    response = requests.get(url)
    try:
        return response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}