import requests
from typing import Optional

def get_all_giveaways(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch all ongoing giveaways.
    """
    url = "https://gamerpower.com/api/giveaways"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_giveaway_by_id(giveaway_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch a specific giveaway by its unique ID.
    """
    url = f"https://gamerpower.com/api/giveaway?id={giveaway_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_giveaways_by_platform(platform: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch giveaways filtered by platform.
    """
    url = f"https://gamerpower.com/api/giveaways?platform={platform}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_giveaways_by_type(giveaway_type: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch giveaways filtered by type.
    """
    url = f"https://gamerpower.com/api/giveaways?type={giveaway_type}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_giveaways_sorted(sort_by: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch giveaways sorted by a specified criteria (date, value, popularity).
    """
    url = f"https://gamerpower.com/api/giveaways?sort-by={sort_by}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_total_worth(platform: Optional[str] = None, giveaway_type: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch the total worth of live giveaways and worth estimation in US dollars. Can filter by platform and type.
    """
    url = "https://gamerpower.com/api/worth"
    if platform or giveaway_type:
        url += "?"
        if platform:
            url += f"platform={platform}"
        if giveaway_type:
            if platform:
                url += "&"
            url += f"type={giveaway_type}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}