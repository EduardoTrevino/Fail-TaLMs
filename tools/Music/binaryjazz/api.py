import requests
from typing import Optional

def get_genres(count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetch a number of random music genres.
    Parameters:
    count [Optional]: integer [Description: The number of genres to fetch. Default is 1.]
    """
    url = f"https://binaryjazz.us/wp-json/genrenator/v1/genre/{count}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_stories(count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetch a number of random genre stories.
    Parameters:
    count [Optional]: integer [Description: The number of stories to fetch. Default is 1.]
    """
    url = f"https://binaryjazz.us/wp-json/genrenator/v1/story/{count}/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}