import requests
from typing import Optional

def contains_profanity(text: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> str:
    """
    Checks if the input text contains profanity by calling the 'containsprofanity' endpoint.
    
    Parameters:
    text (str): Input text to be checked for profanity.
    
    Returns:
    str: Returns "true" if profanity is found, otherwise "false".
    """
    url = "https://www.purgomalum.com/service/containsprofanity"
    params = {'text': text}
    response = requests.get(url, params=params)
    return response.text

def filter_text_json(text: str, add: Optional[str] = None, fill_text: Optional[str] = None, 
                     fill_char: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> dict:
    """
    Filters profanity from the input text and returns the result as JSON.
    
    Parameters:
    text (str): Input text to be processed.
    add (Optional[str]): A comma separated list of words to be added to the profanity list.
    fill_text (Optional[str]): Text used to replace profane words.
    fill_char (Optional[str]): Character used to replace profane words.
    
    Returns:
    dict: JSON object with the filtered result.
    """
    url = "https://www.purgomalum.com/service/json"
    params = {'text': text}
    if add:
        params['add'] = add
    if fill_text:
        params['fill_text'] = fill_text
    if fill_char:
        params['fill_char'] = fill_char

    response = requests.get(url, params=params)
    return response.json()

def filter_text_plain(text: str, add: Optional[str] = None, fill_text: Optional[str] = None, 
                      fill_char: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> str:
    """
    Filters profanity from the input text and returns the result as plain text.
    
    Parameters:
    text (str): Input text to be processed.
    add (Optional[str]): A comma separated list of words to be added to the profanity list.
    fill_text (Optional[str]): Text used to replace profane words.
    fill_char (Optional[str]): Character used to replace profane words.
    
    Returns:
    str: Processed input text.
    """
    url = "https://www.purgomalum.com/service/plain"
    params = {'text': text}
    if add:
        params['add'] = add
    if fill_text:
        params['fill_text'] = fill_text
    if fill_char:
        params['fill_char'] = fill_char

    response = requests.get(url, params=params)
    return response.text

def filter_text_xml(text: str, add: Optional[str] = None, fill_text: Optional[str] = None, 
                    fill_char: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> str:
    """
    Filters profanity from the input text and returns the result as XML.
    
    Parameters:
    text (str): Input text to be processed.
    add (Optional[str]): A comma separated list of words to be added to the profanity list.
    fill_text (Optional[str]): Text used to replace profane words.
    fill_char (Optional[str]): Character used to replace profane words.
    
    Returns:
    str: XML string with the filtered result.
    """
    url = "https://www.purgomalum.com/service/xml"
    params = {'text': text}
    if add:
        params['add'] = add
    if fill_text:
        params['fill_text'] = fill_text
    if fill_char:
        params['fill_char'] = fill_char

    response = requests.get(url, params=params)
    return response.text