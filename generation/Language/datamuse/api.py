import requests
from typing import Optional, List

def words(ml: Optional[str] = None, sl: Optional[str] = None, sp: Optional[str] = None, 
          rel_code: Optional[str] = None, v: Optional[str] = None, topics: Optional[str] = None, 
          lc: Optional[str] = None, rc: Optional[str] = None, max: Optional[int] = 100, 
          md: Optional[str] = None, qe: Optional[str] = None, 
          toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[dict]:
    """
    The /words endpoint returns a list of words and multiword expressions from a given vocabulary 
    matching a set of constraints. 
    
    Parameters:
    - ml (Optional): string. Means like constraint.
    - sl (Optional): string. Sounds like constraint.
    - sp (Optional): string. Spelled like constraint.
    - rel_code (Optional): string. Related word constraints, e.g., 'syn', 'ant'.
    - v (Optional): string. Identifier for the vocabulary to use.
    - topics (Optional): string. Topic hint words.
    - lc (Optional): string. Left context hint word.
    - rc (Optional): string. Right context hint word.
    - max (Optional): int. Maximum number of results to return (default 100).
    - md (Optional): string. Metadata flags, e.g., 'd', 'p'.
    - qe (Optional): string. Query echo.

    Returns a list of word objects.
    """
    url = "https://api.datamuse.com/words"
    params = {k: v for k, v in locals().items() if v is not None and k != 'toolbench_rapidapi_key'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def sug(s: str, max: Optional[int] = 10, v: Optional[str] = None,
        toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> List[dict]:
    """
    The /sug endpoint provides word suggestions given a partially-entered query for autocomplete.

    Parameters:
    - s: string. Prefix hint string entered by user.
    - max (Optional): int. Maximum number of results to return (default is 10).
    - v (Optional): string. Identifier for the vocabulary to use.

    Returns a list of suggested word objects.
    """
    url = "https://api.datamuse.com/sug"
    params = {k: v for k, v in locals().items() if v is not None and k != 'toolbench_rapidapi_key'}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}