import requests
from typing import Optional

BASE_URL = "https://the-rosary-api.vercel.app"

def get_today_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/today"
    response = requests.get(url)
    return response.json()

def get_yesterday_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/yesterday"
    response = requests.get(url)
    return response.json()

def get_tomorrow_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/tomorrow"
    response = requests.get(url)
    return response.json()

def get_prayer_by_day(day: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/{day.lower()}"
    response = requests.get(url)
    return response.json()

def get_prayer_by_date(date: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/date/{date}"
    response = requests.get(url)
    return response.json()

def get_random_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/random"
    response = requests.get(url)
    return response.json()

def get_yearly_prayer_list(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/list"
    response = requests.get(url)
    return response.json()

def get_joyful_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/joyful"
    response = requests.get(url)
    return response.json()

def get_glorious_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/glorious"
    response = requests.get(url)
    return response.json()

def get_sorrowful_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/sorrowful"
    response = requests.get(url)
    return response.json()

def get_luminous_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/luminous"
    response = requests.get(url)
    return response.json()

def get_novena_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/novena"
    response = requests.get(url)
    return response.json()

def get_novena_prayer_by_date(date: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/novena/{date}"
    response = requests.get(url)
    return response.json()

def get_54day_novena_prayer(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    url = f"{BASE_URL}/v1/54daynovena"
    response = requests.get(url)
    return response.json()