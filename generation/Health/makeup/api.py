import requests
from typing import Optional, List

def search_makeup_products(
    brand: Optional[str] = None,
    product_type: Optional[str] = None,
    product_category: Optional[str] = None,
    product_tags: Optional[str] = None,
    price_greater_than: Optional[float] = None,
    price_less_than: Optional[float] = None,
    rating_greater_than: Optional[float] = None,
    rating_less_than: Optional[float] = None,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
):
    """
    Search makeup products with the given parameters.

    Parameters:
    - brand: string (optional)
    - product_type: string (optional)
    - product_category: string (optional)
    - product_tags: string, list separated by commas (optional)
    - price_greater_than: number (optional)
    - price_less_than: number (optional)
    - rating_greater_than: number (optional)
    - rating_less_than: number (optional)
    """
    url = "http://makeup-api.herokuapp.com/api/v1/products.json"
    params = {}

    if brand:
        params['brand'] = brand
    if product_type:
        params['product_type'] = product_type
    if product_category:
        params['product_category'] = product_category
    if product_tags:
        params['product_tags'] = product_tags
    if price_greater_than is not None:
        params['price_greater_than'] = price_greater_than
    if price_less_than is not None:
        params['price_less_than'] = price_less_than
    if rating_greater_than is not None:
        params['rating_greater_than'] = rating_greater_than
    if rating_less_than is not None:
        params['rating_less_than'] = rating_less_than
    
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}