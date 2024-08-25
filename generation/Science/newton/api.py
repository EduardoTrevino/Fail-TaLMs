import requests

def newton_calculate(operation: str, expression: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Sends a GET request to the newton API to perform a mathematical operation on the provided expression.
    
    Parameters:
    operation [Required]: string - The mathematical operation to perform.
    expression [Required]: string - The URL-encoded mathematical expression.

    Returns:
    A JSON object with the operation, the expression, and the result.
    """
    base_url = "https://newton.now.sh/api/v2"
    url = f"{base_url}/{operation}/{expression}"
    
    response = requests.get(url)
    
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}