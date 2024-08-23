import requests
from typing import Optional, Dict, Any, Tuple

TOOLBENCH_RAPIDAPI_KEY = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

def resmush_get(img: str, qlty: Optional[int] = 92, exif: Optional[bool] = False, toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY) -> Dict[str, Any]:
    """
    Compress an image using GET method.
    
    Parameters:
    img (str): URL of the image to be compressed.
    qlty (int, optional): Quality level for JPG compression (0-100), default is 92.
    exif (bool, optional): Whether to retain EXIF data, default is False.
    """
    url = "http://api.resmush.it/ws.php"
    params = {
        'img': img,
        'qlty': qlty
    }
    if exif:
        params['exif'] = 'true'

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def resmush_post(file_path: str, qlty: Optional[int] = 92, toolbench_rapidapi_key: str = TOOLBENCH_RAPIDAPI_KEY) -> Dict[str, Any]:
    """
    Compress an image using POST method by sending the file directly.
    
    Parameters:
    file_path (str): Path to the image file to be compressed.
    qlty (int, optional): Quality level for JPG compression (0-100), default is 92.
    """
    url = f"http://api.resmush.it/?qlty={qlty}"
    with open(file_path, 'rb') as file:
        files = {'files': (file_path, file)}
        response = requests.post(url, files=files)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}