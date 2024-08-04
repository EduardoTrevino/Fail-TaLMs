import requests

def get_boards(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the list of all boards and their attributes from 4chan.
    """
    url = "https://a.4cdn.org/boards.json"
    response = requests.get(url)
    try:
        data = response.json()
    except:
        data = response.text
    return data

def get_thread_list(board: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the list of all threads on a board and their attributes from 4chan.
    
    :param board: The board to retrieve threads from.
    """
    url = f"https://a.4cdn.org/{board}/threads.json"
    response = requests.get(url)
    try:
        data = response.json()
    except:
        data = response.text
    return data

def get_thread(board: str, thread_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the full content of a specific thread from 4chan.
    
    :param board: The board the thread is located on.
    :param thread_id: The ID of the thread.
    """
    url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"
    response = requests.get(url)
    try:
        data = response.json()
    except:
        data = response.text
    return data
