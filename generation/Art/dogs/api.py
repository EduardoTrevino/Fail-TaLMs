import requests
from typing import Optional

def list_all_breeds(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Lists all dog breeds with optional sub-breeds.
    """
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}
    
def random_image_from_all_dogs(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetches a single random image from all dog breeds collection.
    """
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def multiple_random_images(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', count: Optional[int] = 3):
    """
    Endpoint description: Fetches multiple random images from all dog breeds collection.
    """
    url = f"https://dog.ceo/api/breeds/image/random/{count}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def images_by_breed(breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetches all images from a specified breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def random_image_by_breed(breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetches a single random image from a specified breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def multiple_random_images_by_breed(breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', count: Optional[int] = 3):
    """
    Endpoint description: Fetches multiple random images from a specified breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images/random/{count}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_all_sub_breeds(breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Lists all sub-breeds from a specified breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/list"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def images_by_sub_breed(breed: str, sub_breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetches all images from a specified sub-breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}
    
def random_image_by_sub_breed(breed: str, sub_breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetches a single random image from a specified sub-breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def multiple_random_images_by_sub_breed(breed: str, sub_breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', count: Optional[int] = 3):
    """
    Endpoint description: Fetches multiple random images from a specified sub-breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random/{count}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}