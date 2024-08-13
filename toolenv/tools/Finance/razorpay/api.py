import requests
from typing import Optional

def ifsc(ifsc: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve details of a bank branch using the IFSC code.
    """
    url = f"https://ifsc.razorpay.com/{ifsc}"
    response = requests.get(url)
    
    try:
        observation = response.json()
    except:
        observation = response.text
    
    return observation