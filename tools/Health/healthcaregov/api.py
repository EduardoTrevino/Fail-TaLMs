import requests
from typing import Optional


def get_content_object(post_title: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a specific content post object by post title.
    Parameters:
    post_title [Required]: string [The title of the post]
    """
    url = f"https://www.healthcare.gov/{post_title}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_content_collection(content_type: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a list of post objects by content type.
    Parameters:
    content_type [Required]: string [The type of content like 'articles', 'blog', 'questions', etc.]
    """
    url = f"https://www.healthcare.gov/api/{content_type}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_content_index(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve a site-wide index of all posts and their metadata.
    Parameters:
    None
    """
    url = "https://www.healthcare.gov/api/index.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}