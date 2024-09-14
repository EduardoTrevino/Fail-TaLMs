import requests
from typing import Optional

def unshorten_url(short_url: str, authorization_token: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> dict:
    """
    Unshorten a given short URL using the Unshorten.me API.

    Parameters:
    short_url (str): The shortened URL you want to unshorten.
    authorization_token (str, optional): The authorization token found on your Unshorten.me profile page.
    toolbench_rapidapi_key (str): Public rapidapi key.

    Returns:
    dict: Response from the API containing the unshortened URL and success status.
    """
    url = f"https://unshorten.me/api/v2/unshorten?url={short_url}"
    headers = {}
    
    if authorization_token:
        headers['Authorization'] = f"Token {authorization_token}"
    
    response = requests.get(url, headers=headers)
    
    try:
        return response.json()  # Convert response text to JSON
    except Exception as e:
        return {"error": str(e), "response_code": response.status_code, "response_text": response.text}
