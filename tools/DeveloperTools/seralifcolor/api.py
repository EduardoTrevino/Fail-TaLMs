import requests
from typing import Optional


def get_color_info(color: str = 'aquamarine', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the requested color, its complementary, and its grayscale in different formats and the black or white text corresponding to each color according to its brightness.
    
    Parameters:
    color [Required]: string (e.g., keyword, HEX, RGB, RGBA, HSL, or HSLA formats)
    
    Returns:
    JSON object containing the details of the requested color.
    """
    url = f"https://color.serialif.com/{color}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}