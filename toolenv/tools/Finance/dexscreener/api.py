import requests
import json
from typing import Optional, List

def pairs(chainId: str, pairAddresses: List[str], toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get one or multiple pairs by chain and pair address.
    """
    url = f"https://api.dexscreener.com/latest/dex/pairs/{chainId}/" + ",".join(pairAddresses)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def tokens(tokenAddresses: List[str], toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get one or multiple pairs by token address.
    """
    url = f"https://api.dexscreener.com/latest/dex/tokens/" + ",".join(tokenAddresses)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(q: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for pairs matching query.
    """
    url = f"https://api.dexscreener.com/latest/dex/search/?q={q}"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
