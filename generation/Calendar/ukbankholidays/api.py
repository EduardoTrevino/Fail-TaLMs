import requests
from typing import Optional

def uk_bank_holidays_json(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Serves bank holidays data in JSON format for UK, including regions like England and Wales, Scotland, and Northern Ireland.
    Parameters:
        None
    """
    url = "https://www.gov.uk/bank-holidays.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}