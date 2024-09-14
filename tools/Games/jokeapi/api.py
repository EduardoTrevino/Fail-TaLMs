import requests
from typing import Optional, List

def get_joke(category: str = "Any", blacklist_flags: Optional[List[str]] = None, lang: str = "en", joke_type: Optional[str] = None,
             contains: Optional[str] = None, id_range: Optional[str] = None, amount: int = 1, 
             format: str = "json", safe_mode: bool = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetches jokes from JokeAPI based on given parameters.
    
    :param category: The joke category to fetch (e.g., "Programming"). Default is "Any".
    :param blacklist_flags: List of flags to filter out jokes (e.g., ["nsfw", "religious"]).
    :param lang: Language of the joke (e.g., "en" for English). Default is "en".
    :param joke_type: Type of joke ("single" or "twopart").
    :param contains: Search for a joke containing this string.
    :param id_range: ID range or specific ID(s) to retrieve joke(s).
    :param amount: How many jokes to fetch. Maximum is 10. Default is 1.
    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param safe_mode: Whether to fetch only safe jokes.
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: A response containing joke(s).
    """
    url = f"https://v2.jokeapi.dev/joke/{category}"
    params = {
        'blacklistFlags': ','.join(blacklist_flags) if blacklist_flags else None,
        'lang': lang,
        'type': joke_type,
        'contains': contains,
        'idRange': id_range,
        'amount': amount,
        'format': format,
    }
    if safe_mode:
        params['safe-mode'] = ''
    
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.json()

def get_joke_info(format: str = "json", lang: str = "en", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves information about the JokeAPI.

    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param lang: Language code for system messages (e.g., "en" for English). Default is "en".
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: Information about the JokeAPI.
    """
    url = "https://v2.jokeapi.dev/info"
    params = {
        'format': format,
        'lang': lang,
    }
    
    response = requests.get(url, params=params)
    return response.json()

def get_joke_categories(format: str = "json", lang: str = "en", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves all available joke categories.

    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param lang: Language code for system messages (e.g., "en" for English). Default is "en".
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: List of available joke categories.
    """
    url = "https://v2.jokeapi.dev/categories"
    params = {
        'format': format,
        'lang': lang,
    }
    
    response = requests.get(url, params=params)
    return response.json()

def get_language_code(language: str, format: str = "json", lang: str = "en", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves ISO 639-1 language code for the specified language.
    
    :param language: The language name to search for.
    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param lang: Language code for system messages (e.g., "en" for English). Default is "en".
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: The ISO 639-1 language code.
    """
    url = f"https://v2.jokeapi.dev/langcode/{language}"
    params = {
        'format': format,
        'lang': lang,
    }
    
    response = requests.get(url, params=params)
    return response.json()

def get_supported_languages(format: str = "json", lang: str = "en", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves supported languages for jokes and system messages.

    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param lang: Language code for system messages (e.g., "en" for English). Default is "en".
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: Information about supported languages.
    """
    url = "https://v2.jokeapi.dev/languages"
    params = {
        'format': format,
        'lang': lang,
    }
    
    response = requests.get(url, params=params)
    return response.json()

def get_flags(format: str = "json", lang: str = "en", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves available blacklist flags.
    
    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param lang: Language code for system messages (e.g., "en" for English). Default is "en".
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: List of available blacklist flags.
    """
    url = "https://v2.jokeapi.dev/flags"
    params = {
        'format': format,
        'lang': lang,
    }
    
    response = requests.get(url, params=params)
    return response.json()

def get_formats(format: str = "json", lang: str = "en", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves available response formats.
    
    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param lang: Language code for system messages (e.g., "en" for English). Default is "en".
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: List of available response formats.
    """
    url = "https://v2.jokeapi.dev/formats"
    params = {
        'format': format,
        'lang': lang,
    }
    
    response = requests.get(url, params=params)
    return response.json()

def ping_jokeapi(format: str = "json", lang: str = "en", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Pings JokeAPI to test connectivity.

    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param lang: Language code for system messages (e.g., "en" for English). Default is "en".
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: A response message indicating the API is reachable.
    """
    url = "https://v2.jokeapi.dev/ping"
    params = {
        'format': format,
        'lang': lang,
    }

    response = requests.get(url, params=params)
    return response.json()

def get_endpoints_info(format: str = "json", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieves information about all available endpoints.
    
    :param format: Response format ("json", "xml", "yaml", "txt"). Default is "json".
    :param toolbench_rapidapi_key: API key for accessing JokeAPI.
    :return: List of available endpoints with their usage and descriptions.
    """
    url = "https://v2.jokeapi.dev/endpoints"
    params = {
        'format': format,
    }
    
    response = requests.get(url, params=params)
    return response.json()