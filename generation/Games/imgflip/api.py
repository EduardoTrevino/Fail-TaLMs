import requests
from typing import Optional, List, Dict


def get_memes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieves an array of popular memes that may be captioned with this API.
    Parameters: None
    """
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def caption_image(template_id: str, username: str, password: str, text0: Optional[str] = "", text1: Optional[str] = "", font: Optional[str] = "impact", max_font_size: Optional[int] = 50, boxes: Optional[List[Dict[str, str]]] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Add a caption to an Imgflip meme template.
    Parameters:
     template_id [Required]: string, the ID of the template to use.
     username [Required]: string, imgflip account username.
     password [Required]: string, imgflip account password.
     text0 [Optional]: string, top text for the meme.
     text1 [Optional]: string, bottom text for the meme.
     font [Optional]: string, font family to use for the text. Defaults to "impact".
     max_font_size [Optional]: integer, maximum font size in pixels. Defaults to 50.
     boxes [Optional]: list of dicts, each dict representing a text box with properties like 'text', 'x', 'y', 'width', 'height', 'color', 'outline_color'.
    """
    url = "https://api.imgflip.com/caption_image"
    data = {
        'template_id': template_id,
        'username': username,
        'password': password,
        'text0': text0,
        'text1': text1,
        'font': font,
        'max_font_size': max_font_size
    }

    if boxes:
        data['boxes'] = boxes

    response = requests.post(url, data=data)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}