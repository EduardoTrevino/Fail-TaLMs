import requests
from typing import Optional

def get_content_object(post_title: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves a specific content object by its post title.
    Parameters:
    - post_title: str - The title of the post without trailing slashes.
    """
    url = f"https://www.healthcare.gov/{post_title}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_content_collection(content_type: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves a specific content collection by its content type.
    Parameters:
    - content_type: str - The type of the content (e.g., articles, blog, glossary).
    """
    url = f"https://www.healthcare.gov/api/{content_type}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_content_index(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves the site-wide index of all posts and their metadata.
    """
    url = "https://www.healthcare.gov/api/index.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}