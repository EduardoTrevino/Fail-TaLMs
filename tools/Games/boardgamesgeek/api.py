import requests
from typing import Optional


def get_thing_items(ids: str, type: Optional[str] = None, versions: Optional[int] = None, videos: Optional[int] = None,
                    stats: Optional[int] = None, page: Optional[int] = 1, pagesize: Optional[int] = 100,
                    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about specified 'thing' items such as boardgames or other types from BGG.
    
    Parameters:
    ids (str): Comma-separated list of thing IDs to retrieve.
    type (Optional[str]): Filter results by THINGTYPEs like boardgame, expansion, accessory etc. Multiple types can be comma-separated.
    versions (Optional[int]): Include version info. 
    videos (Optional[int]): Include videos. 
    stats (Optional[int]): Include ranking and rating stats. 
    page (Optional[int]): Page number for paginated results.
    pagesize (Optional[int]): Page size for paginated results.
    """
    
    url = "https://boardgamegeek.com/xmlapi2/thing"
    params = {
        'id': ids,
        'type': type,
        'versions': versions,
        'videos': videos,
        'stats': stats,
        'page': page,
        'pagesize': pagesize
    }
    response = requests.get(url, params=params)
    return response.content


def get_family_items(ids: str, type: Optional[str] = None, 
                     toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about specified 'family' items from BGG.

    Parameters:
    ids (str): Comma-separated list of family IDs to retrieve.
    type (Optional[str]): Filter results by FAMILYTYPEs like boardgamefamily.
    """

    url = "https://boardgamegeek.com/xmlapi2/family"
    params = {
        'id': ids,
        'type': type
    }
    response = requests.get(url, params=params)
    return response.content


def get_forum_list(id: int, type: str, 
                   toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve forum list for a specific type/id from BGG.

    Parameters:
    id (int): The ID of the entry you want the forum list for.
    type (str): The type of entry (either thing or family).
    """

    url = "https://boardgamegeek.com/xmlapi2/forumlist"
    params = {
        'id': id,
        'type': type
    }
    response = requests.get(url, params=params)
    return response.content


def get_forum(id: int, page: Optional[int] = 1, 
              toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve threads for a specific forum from BGG.

    Parameters:
    id (int): The ID of the forum.
    page (Optional[int]): The page of the thread list to return.
    """

    url = "https://boardgamegeek.com/xmlapi2/forum"
    params = {
        'id': id,
        'page': page
    }
    response = requests.get(url, params=params)
    return response.content


def get_thread(id: int, minarticleid: Optional[int] = None, minarticledate: Optional[str] = None,
               count: Optional[int] = None, username: Optional[str] = None,
               toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a specific forum thread by ID.

    Parameters:
    id (int): The ID of the thread to retrieve.
    minarticleid (Optional[int]): Minimum article ID to filter articles.
    minarticledate (Optional[str]): Minimum date (YYYY-MM-DD) to filter articles.
    count (Optional[int]): Limit the number of articles returned.
    """

    url = "https://boardgamegeek.com/xmlapi2/thread"
    params = {
        'id': id,
        'minarticleid': minarticleid,
        'minarticledate': minarticledate,
        'count': count
    }
    response = requests.get(url, params=params)
    return response.content


def get_user_info(name: str, buddies: Optional[int] = None, guilds: Optional[int] = None,
                  hot: Optional[int] = None, top: Optional[int] = None, domain: Optional[str] = 'boardgame',
                  page: Optional[int] = 1, 
                  toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a user by username from BGG.

    Parameters:
    name (str): The username to retrieve info for.
    buddies (Optional[int]): Include buddies.
    guilds (Optional[int]): Include guilds.
    hot (Optional[int]): Include user's hot 10 list.
    top (Optional[int]): Include user's top 10 list.
    domain (Optional[str]): The domain for hot and top lists.
    """

    url = "https://boardgamegeek.com/xmlapi2/user"
    params = {
        'name': name,
        'buddies': buddies,
        'guilds': guilds,
        'hot': hot,
        'top': top,
        'domain': domain,
        'page': page
    }
    response = requests.get(url, params=params)
    return response.content


def get_guild_info(id: int, members: Optional[int] = None, sort: Optional[str] = 'username',
                   page: Optional[int] = 1, 
                   toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about a guild by ID.

    Parameters:
    id (int): The ID of the guild.
    members (Optional[int]): Include member roster.
    sort (Optional[str]): How to sort the members list (e.g. username, date).
    page (Optional[int]): Page of members list to return.
    """

    url = "https://boardgamegeek.com/xmlapi2/guild"
    params = {
        'id': id,
        'members': members,
        'sort': sort,
        'page': page
    }
    response = requests.get(url, params=params)
    return response.content


def get_plays(username: Optional[str] = None, id: Optional[int] = None, type: Optional[str] = 'thing',
              mindate: Optional[str] = None, maxdate: Optional[str] = None, subtype: Optional[str] = 'boardgame',
              page: Optional[int] = 1, 
              toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve play information logged by a user or for an item.

    Parameters:
    username (Optional[str]): Username to retrieve play information for.
    id (Optional[int]): Item ID to retrieve play information for.
    type (Optional[str]): Type of the item (thing, family).
    """

    url = "https://boardgamegeek.com/xmlapi2/plays"
    params = {
        'username': username,
        'id': id,
        'type': type,
        'mindate': mindate,
        'maxdate': maxdate,
        'subtype': subtype,
        'page': page
    }
    response = requests.get(url, params=params)
    return response.content


def get_collection(username: str, version: Optional[int] = None, subtype: Optional[str] = 'boardgame', 
                   excludesubtype: Optional[str] = None, id: Optional[str] = None, brief: Optional[int] = None,
                   stats: Optional[int] = None, own: Optional[int] = None, rated: Optional[int] = None,
                   played: Optional[int] = None, comment: Optional[int] = None, trade: Optional[int] = None,
                   want: Optional[int] = None, wishlist: Optional[int] = None, wishlistpriority: Optional[int] = None,
                   preordered: Optional[int] = None, wanttoplay: Optional[int] = None, 
                   wanttobuy: Optional[int] = None, prevowned: Optional[int] = None, hasparts: Optional[int] = None,
                   wantparts: Optional[int] = None, minrating: Optional[int] = None, rating: Optional[int] = None,
                   minbggrating: Optional[int] = None, bggrating: Optional[int] = None, minplays: Optional[int] = None,
                   maxplays: Optional[int] = None, showprivate: Optional[int] = None, collid: Optional[int] = None,
                   modifiedsince: Optional[str] = None,
                   toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve details about a user's collection.

    Parameters:
    username (str): The username to request the collection for.
    """

    url = "https://boardgamegeek.com/xmlapi2/collection"
    params = {
        'username': username,
        'version': version,
        'subtype': subtype,
        'excludesubtype': excludesubtype,
        'id': id,
        'brief': brief,
        'stats': stats,
        'own': own,
        'rated': rated,
        'played': played,
        'comment': comment,
        'trade': trade,
        'want': want,
        'wishlist': wishlist,
        'wishlistpriority': wishlistpriority,
        'preordered': preordered,
        'wanttoplay': wanttoplay,
        'wanttobuy': wanttobuy,
        'prevowned': prevowned,
        'hasparts': hasparts,
        'wantparts': wantparts,
        'minrating': minrating,
        'rating': rating,
        'minbggrating': minbggrating,
        'bggrating': bggrating,
        'minplays': minplays,
        'maxplays': maxplays,
        'showprivate': showprivate,
        'collid': collid,
        'modifiedsince': modifiedsince
    }
    response = requests.get(url, params=params)
    return response.content


def get_hot_items(type: str, 
                  toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the list of most active items on BGG.

    Parameters:
    type (str): The type of hot list to retrieve (e.g. boardgame, rpg).
    """

    url = "https://boardgamegeek.com/xmlapi2/hot"
    params = {
        'type': type
    }
    response = requests.get(url, params=params)
    return response.content


def search_items(query: str, type: Optional[str] = None, exact: Optional[int] = None,
                 toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Search for items by name from the BGG database.

    Parameters:
    query (str): The search query.
    type (Optional[str]): The type of items to return.
    """

    url = "https://boardgamegeek.com/xmlapi2/search"
    params = {
        'query': query,
        'type': type,
        'exact': exact
    }
    response = requests.get(url, params=params)
    return response.content