import requests
from typing import Optional


def get_product_by_barcode(barcode: str, fields: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get product details by barcode.
    
    Parameters:
    barcode [Required]: string [Description: The barcode number of the product]
    fields [Optional]: string [Description: Fields to be returned in the response]
    """
    base_url = "https://world.openfoodfacts.org/api/v2/product"
    url = f"{base_url}/{barcode}.json"
    params = {}
    if fields:
        params['fields'] = fields

    headers = {
        'User-Agent': 'OpenFoodFactsApp/1.0 (myapp@example.com)'
    }

    response = requests.get(url, params=params, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_products(nutrition_grades_tags: Optional[str] = None, categories_tags_en: Optional[str] = None, fields: Optional[str] = None, sort_by: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search products by various criteria.
    
    Parameters:
    nutrition_grades_tags [Optional]: string [Description: Filter products by nutrition grades]
    categories_tags_en [Optional]: string [Description: Filter products by category]
    fields [Optional]: string [Description: Fields to be returned in the response]
    sort_by [Optional]: string [Description: Field to sort the response]
    """
    url = "https://world.openfoodfacts.org/api/v2/search"
    params = {}
    if nutrition_grades_tags:
        params['nutrition_grades_tags'] = nutrition_grades_tags
    if categories_tags_en:
        params['categories_tags_en'] = categories_tags_en
    if fields:
        params['fields'] = fields
    if sort_by:
        params['sort_by'] = sort_by

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}