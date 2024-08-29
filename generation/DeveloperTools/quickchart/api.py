import requests
from typing import Optional

def generate_chart(chart_config: str, width: Optional[int] = 500, height: Optional[int] = 300, 
                   device_pixel_ratio: Optional[int] = 2, background_color: Optional[str] = 'transparent', 
                   version: Optional[str] = '2', format: Optional[str] = 'png', 
                   encoding: Optional[str] = 'url', method: Optional[str] = 'GET',
                   toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    This function generates a chart image based on Chart.js configuration using the QuickChart API.
    
    Parameters:
    chart_config [Required]: str - Chart.js configuration object in Javascript or JSON format.
    width [Optional]: int - Width of image in pixels. Defaults to 500.
    height [Optional]: int - Height of image in pixels. Defaults to 300.
    device_pixel_ratio [Optional]: int - Device pixel ratio of output. Defaults to 2.
    background_color [Optional]: str - Background color. Defaults to transparent.
    version [Optional]: str - Chart.js version. Defaults to 2.
    format [Optional]: str - Output format. Defaults to png.
    encoding [Optional]: str - Encoding type, url or base64. Defaults to url.
    method [Optional]: str - HTTP method to use, 'GET' or 'POST'. Defaults to 'GET'.
    """
    url = "https://quickchart.io/chart"

    params = {
        'c': chart_config,
        'w': width,
        'h': height,
        'devicePixelRatio': device_pixel_ratio,
        'bkg': background_color,
        'v': version,
        'format': format,
        'encoding': encoding
    }
    
    try:
        if method.upper() == 'GET':
            response = requests.get(url, params=params)
        elif method.upper() == 'POST':
            json_data = {
                'chart': chart_config,
                'width': width,
                'height': height,
                'devicePixelRatio': device_pixel_ratio,
                'backgroundColor': background_color,
                'version': version,
                'format': format,
                'encoding': encoding
            }
            response = requests.post(url, json=json_data)
        else:
            return {"error": f"Invalid HTTP method: {method}"}

        # Check the response status code
        if response.status_code != 200:
            return {"error": f"HTTP Error: {response.status_code}", "response": response.text}

        # If encoding is 'base64' or 'url', handle the response as binary (image data)
        if encoding in ['url', 'base64']:
            return response.content  # Return the raw image bytes
        else:
            # If other encodings were to be supported
            return response.json()

    except Exception as e:
        return {"error": str(e), "response": response.text}
