import requests

def compress_image(img: str, qlty: int = 92, exif: bool = False, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Compress an image using resmush.it API
    """
    url = f"https://api.resmush.it/ws.php?img={img}&qlty={qlty}&exif={str(exif).lower()}"
    
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def check_error(img: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Check the error log of the compressed image using resmush.it API
    """
    url = f"https://api.resmush.it/ws.php?img={img}"
    
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text
