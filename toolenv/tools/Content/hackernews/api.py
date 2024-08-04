import requests
import json

def get_story_by_id(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch a Hacker News story by its ID.
    
    :param id: The ID of the story.
    :return: The response from the API.
    """
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

def get_comment_by_id(id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch a Hacker News comment by its ID.
    
    :param id: The ID of the comment.
    :return: The response from the API.
    """
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"
    response = requests.get(url)
    try:
        return response.json()
    except:
        return response.text

# Example usage:
# story = get_story_by_id(8863)
# comment = get_comment_by_id(2921983)
