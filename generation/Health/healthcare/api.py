import requests
from typing import Optional, List


def get_content_object(post_title: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get the JSON object for a specific post by its title.
    Parameters:
     post_title [Required]: string [Description: The title of the post.]
    """
    url = f"https://www.healthcare.gov/{post_title}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_content_collection(content_type: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get a collection of posts by content type.
    Parameters:
     content_type [Required]: string [Description: The type of content such as articles, blog, questions, glossary, etc.]
    """
    url = f"https://www.healthcare.gov/api/{content_type}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_content_index(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get an index of all posts and their metadata.
    """
    url = "https://www.healthcare.gov/api/index.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}