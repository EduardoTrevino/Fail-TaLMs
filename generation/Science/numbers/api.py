import requests
from typing import Optional

def get_number_fact(number: str = "random", type: str = "trivia", fragment: Optional[bool] = False, notfound: Optional[str] = "default", min_val: Optional[int] = None, max_val: Optional[int] = None, json: Optional[bool] = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a fact about a number from the Numbers API.

    Parameters:
    number [Optional]: String [An integer, 'random', or day of year 'month/day'. Default is 'random'.]
    type [Optional]: String ['trivia', 'math', 'date', or 'year'. Default is 'trivia'.]
    fragment [Optional]: Boolean [If true, returns the fact as a sentence fragment.]
    notfound [Optional]: String ['default', 'floor', 'ceil'.]
    min_val [Optional]: Integer [The minimum value for random facts]
    max_val [Optional]: Integer [The maximum value for random facts]
    json [Optional]: Boolean [If true, returns the fact in JSON format. Default is True.]
    """
    url = f"http://numbersapi.com/{number}/{type}"

    params = {}
    if fragment:
        params['fragment'] = 'true'
    params['notfound'] = notfound
    if min_val is not None:
        params['min'] = min_val
    if max_val is not None:
        params['max'] = max_val
    if json:
        params['json'] = 'true'
    
    response = requests.get(url, params=params)
    try:
        return response.json() if json else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_batch_number_facts(numbers: str = "1..3", json: Optional[bool] = True, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get facts for multiple numbers in one request.

    Parameters:
    numbers [Optional]: String [A comma separated list of numbers or number ranges. Default is '1..3'.]
    json [Optional]: Boolean [If true, returns the facts in JSON format. Default is True.]
    """
    url = f"http://numbersapi.com/{numbers}"
    params = {}
    if json:
        params['json'] = 'true'
    
    response = requests.get(url, params=params)
    try:
        return response.json() if json else response.text
    except Exception as e:
        return {"error": str(e), "response": response.text}