import requests
import xml.etree.ElementTree as ET

def get_anime_details(anime_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> dict:
    """
    Fetch detailed information about an anime using its ID.
    """
    url = f"https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime={anime_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        anime_details = {}
        
        for child in root:
            anime_details[child.tag] = child.text if child.text else {sub.tag: sub.text for sub in child}
        
        return anime_details
    else:
        return {"error": "Failed to fetch data"}

def get_recently_added_anime(nskip: int = 0, nlist: int = 50, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> list:
    """
    Fetch a list of recently added anime.
    """
    url = f"https://cdn.animenewsnetwork.com/encyclopedia/reports.xml?id=155&type=anime&nskip={nskip}&nlist={nlist}"
    response = requests.get(url)
    
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        anime_list = []
        
        for anime in root.findall("anime"):
            anime_info = {
                "id": anime.get("id"),
                "name": anime.get("name"),
                "type": anime.get("type")
            }
            anime_list.append(anime_info)
        
        return anime_list
    else:
        return {"error": "Failed to fetch data"}

def get_anime_details_batch(anime_ids: list, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> dict:
    """
    Fetch detailed information about multiple anime using their IDs.
    """
    ids = "/".join(anime_ids)
    url = f"https://cdn.animenewsnetwork.com/encyclopedia/api.xml?title={ids}"
    response = requests.get(url)
    
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        batch_details = {}
        
        for child in root:
            batch_details[child.tag] = child.text if child.text else {sub.tag: sub.text for sub in child}
        
        return batch_details
    else:
        return {"error": "Failed to fetch data"}
