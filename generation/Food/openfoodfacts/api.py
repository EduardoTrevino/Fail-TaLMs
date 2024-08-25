import requests
from typing import Optional

def get_product_by_barcode(barcode: str, fields: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get product details by barcode.
    
    Parameters:
    - barcode: str [Required] - The barcode of the product.
    - fields: str [Optional] - Specific fields to retrieve (comma-separated).
    """
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
    params = {}
    if fields:
        params['fields'] = fields

    headers = {
        "User-Agent": f"OpenFoodFactsClient/1.0 ({toolbench_rapidapi_key})"
    }
    
    response = requests.get(url, params=params, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def search_products(categories: Optional[str] = None, nutrition_grades: Optional[str] = None, fields: Optional[str] = None, sort_by: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for products with specific criteria.

    Parameters:
    - categories: str [Optional] - Categories to filter by.
    - nutrition_grades: str [Optional] - Nutrition grade to filter by.
    - fields: str [Optional] - Specific fields to retrieve (comma-separated).
    - sort_by: str [Optional] - Field name to sort by.
    """
    url = "https://world.openfoodfacts.org/api/v2/search"
    params = {}
    if categories:
        params['categories_tags_en'] = categories
    if nutrition_grades:
        params['nutrition_grades_tags'] = nutrition_grades
    if fields:
        params['fields'] = fields
    if sort_by:
        params['sort_by'] = sort_by

    headers = {
        "User-Agent": f"OpenFoodFactsClient/1.0 ({toolbench_rapidapi_key})"
    }
    
    response = requests.get(url, params=params, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}