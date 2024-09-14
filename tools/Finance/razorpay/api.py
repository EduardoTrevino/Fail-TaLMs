import requests

def get_bank_details_by_ifsc(ifsc_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve bank details by providing an IFSC code.

    Parameters:
    ifsc_code [Required]: string. The IFSC code of the bank branch.

    Returns:
    A JSON object containing branch and bank details or an error message if the IFSC code is invalid.
    """
    url = f"https://ifsc.razorpay.com/{ifsc_code}"
    response = requests.get(url)

    if response.status_code == 404:
        return {"error": "Invalid IFSC code"}
    
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}