import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def list_posts(context: str = 'view', page: int = 1, per_page: int = 10, search: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a collection of posts.
    """
    url = "https://example.com/wp-json/wp/v2/posts"
    querystring = {
        'context': context,
        'page': page,
        'per_page': per_page
    }
    if search:
        querystring['search'] = search
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def retrieve_post(id: int, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a specific post record.
    """
    url = f"https://example.com/wp-json/wp/v2/posts/{id}"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def list_comments(post: int, context: str = 'view', page: int = 1, per_page: int = 10, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a collection of comments.
    """
    url = "https://example.com/wp-json/wp/v2/comments"
    querystring = {
        'post': post,
        'context': context,
        'page': page,
        'per_page': per_page
    }
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
