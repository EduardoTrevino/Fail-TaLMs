import requests
from typing import Optional


def get_random_quotes(orderby: str = "rand", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve quotes from the Quotes on Design API randomly.
    Parameters:
    orderby [Optional]: string [Description: The order in which to sort the quotes. Default is 'rand' for random.]
    """
    url = "https://quotesondesign.com/wp-json/wp/v2/posts/"
    params = {
        'orderby': orderby
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}