import requests
from typing import Optional
import json


def get_bank_holidays(division: Optional[str] = 'england-and-wales', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve bank holidays for different regions in the UK.

    Parameters:
    division [Optional]: string [Description: The division for which to fetch the bank holidays. Default is 'england-and-wales'.]
    """
    url = "https://www.gov.uk/bank-holidays.json"
    
    response = requests.get(url)
    
    try:
        data = response.json()
        # print(data['england-and-wales'])
        if division in data:
            return data[division]
            return json.dumps(data[division])
            # print(data[division])
            # return json.dumps(data[division])# ['events']
            # return data['divisions'][division]
        else:
            return {"error": "Division not found"}
    except Exception as e:
        return {"error": str(e), "response": response.text}
    

print(get_bank_holidays())