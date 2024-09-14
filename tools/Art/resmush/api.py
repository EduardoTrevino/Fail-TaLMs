import requests
import mimetypes
from typing import Optional

def compress_image_get_method(img_url: str, qlty: Optional[int] = 92, exif: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Compresses an image specified by a URL using the GET method.
    Parameters:
     - img_url [Required]: string [Description: The URL of the image to be compressed]
     - qlty [Optional]: integer [Description: The quality level for JPG compression (0-100), default is 92]
     - exif [Optional]: boolean [Description: Retain the EXIF data (default is false)]
    """
    url = "https://api.resmush.it/ws.php"
    params = {
        'img': img_url,
        'qlty': qlty,
        'exif': 'true' if exif else 'false'
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def compress_image_post_method(file_path: str, qlty: Optional[int] = 92, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Compresses an image by sending the file using the POST method.
    Parameters:
     - file_path [Required]: string [Description: The local file path of the image to be compressed]
     - qlty [Optional]: integer [Description: The quality level for JPG compression (0-100), default is 92]
    """
    url = f"http://api.resmush.it/?qlty={qlty}"
    mime_type = 'image/jpeg'  # Default mime type
    output = None
    try:
        mime_type = mimetypes.guess_type(file_path)[0] or mime_type
        output = ('files', (file_path, open(file_path, 'rb'), mime_type))
    except FileNotFoundError:
        return {"error": "File not found", "response": None}

    data = {'files': output}

    response = requests.post(url, files=data)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}