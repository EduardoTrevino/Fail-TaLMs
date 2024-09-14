import requests
from typing import Optional, Dict, Any

def list_posts(
    context: Optional[str] = 'view',
    page: Optional[int] = 1,
    per_page: Optional[int] = 10,
    search: Optional[str] = None,
    author: Optional[int] = None,
    categories: Optional[int] = None,
    tags: Optional[int] = None,
    orderby: Optional[str] = 'date',
    order: Optional[str] = 'desc',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve a collection of posts.
    """
    url = "https://example.com/wp-json/wp/v2/posts"
    params = {
        'context': context,
        'page': page,
        'per_page': per_page,
        'search': search,
        'author': author,
        'categories': categories,
        'tags': tags,
        'orderby': orderby,
        'order': order
    }
    response = requests.get(url, params=params)
    return response.json()

def create_post(
    title: str,
    content: str,
    status: Optional[str] = 'draft',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Create a new post.
    """
    url = "https://example.com/wp-json/wp/v2/posts"
    headers = {'Authorization': f'Bearer {toolbench_rapidapi_key}'}
    data = {
        'title': title,
        'content': content,
        'status': status
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def list_categories(
    context: Optional[str] = 'view',
    page: Optional[int] = 1,
    per_page: Optional[int] = 10,
    orderby: Optional[str] = 'name',
    order: Optional[str] = 'asc',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve a collection of categories.
    """
    url = "https://example.com/wp-json/wp/v2/categories"
    params = {
        'context': context,
        'page': page,
        'per_page': per_page,
        'orderby': orderby,
        'order': order
    }
    response = requests.get(url, params=params)
    return response.json()

def retrieve_category(
    category_id: int,
    context: Optional[str] = 'view',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve a specific category.
    """
    url = f"https://example.com/wp-json/wp/v2/categories/{category_id}"
    params = {'context': context}
    response = requests.get(url, params=params)
    return response.json()

def list_tags(
    context: Optional[str] = 'view',
    page: Optional[int] = 1,
    per_page: Optional[int] = 10,
    orderby: Optional[str] = 'name',
    order: Optional[str] = 'asc',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve a collection of tags.
    """
    url = "https://example.com/wp-json/wp/v2/tags"
    params = {
        'context': context,
        'page': page,
        'per_page': per_page,
        'orderby': orderby,
        'order': order
    }
    response = requests.get(url, params=params)
    return response.json()

def list_users(
    context: Optional[str] = 'view',
    page: Optional[int] = 1,
    per_page: Optional[int] = 10,
    orderby: Optional[str] = 'name',
    order: Optional[str] = 'asc',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve a collection of users.
    """
    url = "https://example.com/wp-json/wp/v2/users"
    params = {
        'context': context,
        'page': page,
        'per_page': per_page,
        'orderby': orderby,
        'order': order
    }
    response = requests.get(url, params=params)
    return response.json()

def retrieve_user(
    user_id: int,
    context: Optional[str] = 'view',
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve a specific user.
    """
    url = f"https://example.com/wp-json/wp/v2/users/{user_id}"
    params = {'context': context}
    response = requests.get(url, params=params)
    return response.json()