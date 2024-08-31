import requests
from typing import Optional, List

def grand_exchange_info(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the runedate of when the Grand Exchange Database was last updated.
    """
    url = "https://secure.runescape.com/m=itemdb_rs/api/info.json"
    response = requests.get(url)
    return response.json()

def grand_exchange_category(category: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the number of items determined by the first letter for a given category.
    """
    url = f"https://services.runescape.com/m=itemdb_rs/api/catalogue/category.json?category={category}"
    response = requests.get(url)
    return response.json()

def grand_exchange_items(category: int, alpha: str, page: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns items given the category, starting letter, and page number.
    """
    url = f"https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category={category}&alpha={alpha}&page={page}"
    response = requests.get(url)
    return response.json()

def grand_exchange_detail(item_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns detailed information on a tradeable item in the Grand Exchange by ItemID.
    """
    url = f"https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={item_id}"
    response = requests.get(url)
    return response.json()

def grand_exchange_graph(item_id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Shows the prices each day of a given item for the previous 180 days.
    """
    url = f"https://services.runescape.com/m=itemdb_rs/api/graph/{item_id}.json"
    response = requests.get(url)
    return response.json()

def hiscores_ranking(table: int, category: int, size: int = 50, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns up to the top 50 players in a given skill or activity.
    """
    url = f"https://secure.runescape.com/m=hiscore/ranking.json?table={table}&category={category}&size={size}"
    response = requests.get(url)
    return response.json()