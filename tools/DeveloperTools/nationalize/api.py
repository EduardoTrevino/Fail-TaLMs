import requests
from typing import List, Optional, Union

def predict_nationality(name: Union[str, List[str]], toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Estimates the nationality of a person or multiple people based on a name or names.
    
    Parameters:
    name [Required]: string or list of strings [Description: A single name or a list of names for which to predict nationality.]
    """
    url = "https://api.nationalize.io/"
    
    # Prepare the parameters
    if isinstance(name, list):
        name_param = [(f'name[]={n}') for n in name]  # Batch processing
        params = "&".join(name_param)
    else:
        params = f'name={name}'

    full_url = f"{url}?{params}"
    
    # Make the request
    response = requests.get(full_url)
    
    # Return the response as JSON or an error message
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}