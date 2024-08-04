import requests

def list_all_breeds(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    List all breeds.
    """
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    return response.json()

def random_image(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Display a single random image from all dogs collection.
    """
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    return response.json()

def multiple_random_images(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', count=3):
    """
    Display multiple random images from all dogs collection.
    """
    url = f"https://dog.ceo/api/breeds/image/random/{count}"
    response = requests.get(url)
    return response.json()

def breed_images(breed, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns an array of all the images from a breed, e.g. hound.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images"
    response = requests.get(url)
    return response.json()

def random_image_from_breed(breed, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a random dog image from a breed, e.g. hound.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    return response.json()

def multiple_images_from_breed(breed, count=3, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Return multiple random dog images from a breed, e.g. hound.
    """
    url = f"https://dog.ceo/api/breed/{breed}/images/random/{count}"
    response = requests.get(url)
    return response.json()

def list_all_sub_breeds(breed, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns an array of all the sub-breeds from a breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/list"
    response = requests.get(url)
    return response.json()

def sub_breed_images(breed, sub_breed, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns an array of all the images from the sub-breed.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images"
    response = requests.get(url)
    return response.json()

def random_image_from_sub_breed(breed, sub_breed, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a random dog image from a sub-breed, e.g. hound-afghan.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random"
    response = requests.get(url)
    return response.json()

def multiple_images_from_sub_breed(breed, sub_breed, count=3, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Return multiple random dog images from a sub-breed, e.g. Afghan Hound.
    """
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random/{count}"
    response = requests.get(url)
    return response.json()
