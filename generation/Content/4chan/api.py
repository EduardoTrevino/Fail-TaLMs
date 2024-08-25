import requests

def get_boards(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches the list of all boards and their attributes.
    """
    url = "https://a.4cdn.org/boards.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_threads(board: str = 'po', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches a summarized list of all threads on a board including thread numbers,
    their modification time, and reply count.
    
    Parameters:
    board [Optional]: string [Description: The board name. Default is 'po'.]
    """
    url = f"https://a.4cdn.org/{board}/threads.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_catalog(board: str = 'po', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches a JSON representation of a board catalog including all OPs and their preview replies.

    Parameters:
    board [Optional]: string [Description: The board name. Default is 'po'.]
    """
    url = f"https://a.4cdn.org/{board}/catalog.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_archive(board: str = 'po', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches a list of all closed threads in a board archive. Archived threads no longer receive posts.

    Parameters:
    board [Optional]: string [Description: The board name. Default is 'po'.]
    """
    url = f"https://a.4cdn.org/{board}/archive.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_thread(board: str = 'po', thread_id: int = 570368, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches a full list of posts in a single thread.

    Parameters:
    board [Optional]: string [Description: The board name. Default is 'po'.]
    thread_id [Optional]: integer [Description: The OP ID of the thread. Default is 570368.]
    """
    url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_page(board: str = 'po', page_number: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches a list of threads and their preview replies from a specified index page.

    Parameters:
    board [Optional]: string [Description: The board name. Default is 'po'.]
    page_number [Optional]: integer [Description: The index page number. Default is 1.]
    """
    url = f"https://a.4cdn.org/{board}/{page_number}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}