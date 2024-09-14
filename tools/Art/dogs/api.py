import requests
from typing import Optional, List

def list_all_breeds(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for listing all breeds.
    """
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def random_image(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for retrieving a random image from all breeds.
    """
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def random_images(num: Optional[int] = 3, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for retrieving multiple random images from all breeds.
    Parameters:
    num [Optional]: The number of images to retrieve.
    """
    url = f"https://dog.ceo/api/breeds/image/random/{num}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def images_by_breed(breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for getting all images of a specific breed.
    Parameters:
    breed [Required]: The breed of dog images to retrieve.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def random_image_by_breed(breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for retrieving a random image of a specific breed.
    Parameters:
    breed [Required]: The breed of the dog image to retrieve.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def random_images_by_breed(breed: str, num: Optional[int] = 3, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for retrieving multiple random images of a specific breed.
    Parameters:
    breed [Required]: The breed of dog images to retrieve.
    num [Optional]: The number of images to retrieve.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images/random/{num}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def list_sub_breeds(breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for listing all sub-breeds of a specific breed.
    Parameters:
    breed [Required]: The breed to list sub-breeds of.
    """
    url = f"https://dog.ceo/api/breed/{breed}/list"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def images_by_sub_breed(breed: str, sub_breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for retrieving all images of a specific sub-breed.
    Parameters:
    breed [Required]: The breed of the dog to retrieve images of.
    sub_breed [Required]: The sub-breed to retrieve images of.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def random_image_by_sub_breed(breed: str, sub_breed: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for retrieving a random image of a specific sub-breed.
    Parameters:
    breed [Required]: The breed of the dog image to retrieve.
    sub_breed [Required]: The sub-breed of the dog image to retrieve.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def random_images_by_sub_breed(breed: str, sub_breed: str, num: Optional[int] = 3, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint for retrieving multiple random images of a specific sub-breed.
    Parameters:
    breed [Required]: The breed of dog images to retrieve.
    sub_breed [Required]: The sub-breed to retrieve images of.
    num [Optional]: The number of images to retrieve.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random/{num}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}