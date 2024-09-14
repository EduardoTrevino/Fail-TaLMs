import requests
from typing import Optional


def latestjobs(count: Optional[int] = 50, geo: Optional[str] = None, industry: Optional[str] = None, tag: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the latest remote job listings.
    """
    url = "https://jobicy.com/api/v2/remote-jobs"
    params = {
        "count": count,
    }
    if geo:
        params["geo"] = geo
    if industry:
        params["industry"] = industry
    if tag:
        params["tag"] = tag

    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation