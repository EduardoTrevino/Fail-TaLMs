import requests
from typing import Optional, Dict, Union, List

def auctions_data_list(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all online auctions aggregated data including total trading volumes and winning bids.
    """
    url = "https://whiskyhunter.api.com/auctions_data/"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def auctions_info_list(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all online auctions' main information such as auction name, date, and status.
    """
    url = "https://whiskyhunter.api.com/auctions_info"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def distillery_data_read(slug: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List data for a specific distillery including trading volumes and winning bids.
    """
    url = f"https://whiskyhunter.api.com/distillery_data/{slug}/"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
