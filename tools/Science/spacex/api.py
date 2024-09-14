import requests
from typing import Optional, Dict

def get_all_capsules(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/capsules"
    response = requests.get(url)
    return response.json()

def get_capsule_by_id(capsule_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/capsules/{capsule_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_capsules(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/capsules/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_company_info(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/company"
    response = requests.get(url)
    return response.json()

def get_all_cores(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/cores"
    response = requests.get(url)
    return response.json()

def get_core_by_id(core_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/cores/{core_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_cores(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/cores/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_all_crew(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/crew"
    response = requests.get(url)
    return response.json()

def get_crew_member_by_id(crew_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/crew/{crew_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_crew_members(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/crew/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_all_dragons(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/dragons"
    response = requests.get(url)
    return response.json()

def get_dragon_by_id(dragon_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/dragons/{dragon_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_dragons(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/dragons/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_all_history_events(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/history"
    response = requests.get(url)
    return response.json()

def get_history_event_by_id(event_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/history/{event_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_history_events(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/history/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_all_landing_pads(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/landpads"
    response = requests.get(url)
    return response.json()

def get_landing_pad_by_id(pad_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/landpads/{pad_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_landing_pads(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/landpads/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_all_launches(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    return response.json()

def get_next_launch(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v5/launches/next"
    response = requests.get(url)
    return response.json()

def get_launch_by_id(launch_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def get_all_past_launches(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v5/launches/past"
    response = requests.get(url)
    return response.json()

def query_launches(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v5/launches/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_all_upcoming_launches(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v5/launches/upcoming"
    response = requests.get(url)
    return response.json()

def get_all_launchpads(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/launchpads"
    response = requests.get(url)
    return response.json()

def get_launchpad_by_id(pad_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/launchpads/{pad_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_launchpads(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/launchpads/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_all_payloads(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/payloads"
    response = requests.get(url)
    return response.json()

def get_payload_by_id(payload_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/payloads/{payload_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_payloads(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/payloads/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_roadster_info(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/roadster"
    response = requests.get(url)
    return response.json()

def get_all_rockets(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/rockets"
    response = requests.get(url)
    return response.json()

def get_rocket_by_id(rocket_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_rockets(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/rockets/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()

def get_all_ships(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/ships"
    response = requests.get(url)
    return response.json()

def get_ship_by_id(ship_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"https://api.spacexdata.com/v4/ships/{ship_id}"
    response = requests.get(url)
    if response.status_code == 404:
        return {"error": "Not Found"}
    return response.json()

def query_ships(query: Dict, options: Dict, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = "https://api.spacexdata.com/v4/ships/query"
    response = requests.post(url, json={"query": query, "options": options})
    return response.json()