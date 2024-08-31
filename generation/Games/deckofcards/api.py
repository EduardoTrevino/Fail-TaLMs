import requests
from typing import Optional

def shuffle_deck(deck_count: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Shuffle a new deck of cards.
    
    Parameters:
    deck_count [Optional]: integer [Default: 1]: Number of decks to use.
    """
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
    params = {'deck_count': deck_count}
    response = requests.get(url, params=params)
    return response.json()

def draw_cards(deck_id: Optional[str] = "new", count: Optional[int] = 2, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Draw cards from a deck.
    
    Parameters:
    deck_id [Optional]: string [Default: "new"]: The deck id to draw cards from.
    count [Optional]: integer [Default: 2]: Number of cards to draw.
    """
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/"
    params = {'count': count}
    response = requests.get(url, params=params)
    return response.json()

def reshuffle_deck(deck_id: str, remaining: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Reshuffle a deck.
    
    Parameters:
    deck_id [Required]: string: The deck id to reshuffle.
    remaining [Optional]: boolean [Default: False]: Only shuffle remaining cards.
    """
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/"
    params = {'remaining': remaining}
    response = requests.get(url, params=params)
    return response.json()

def new_deck(jokers_enabled: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Open a brand new deck of cards.
    
    Parameters:
    jokers_enabled [Optional]: boolean [Default: False]: Include jokers in the deck.
    """
    url = "https://deckofcardsapi.com/api/deck/new/"
    params = {'jokers_enabled': jokers_enabled}
    response = requests.get(url, params=params)
    return response.json()

def partial_deck(cards: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Create a partial deck with specific cards.
    
    Parameters:
    cards [Required]: string: Comma separated card codes for the partial deck.
    """
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
    params = {'cards': cards}
    response = requests.get(url, params=params)
    return response.json()

def add_to_pile(deck_id: str, pile_name: str, cards: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Add cards to a pile.
    
    Parameters:
    deck_id [Required]: string: The deck id.
    pile_name [Required]: string: The name of the pile.
    cards [Required]: string: Comma-separated card codes to add to the pile.
    """
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/add/"
    params = {'cards': cards}
    response = requests.get(url, params=params)
    return response.json()

# def shuffle_pile(deck_id: str, pile_name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Shuffle a pile.
    
#     Parameters:
#     deck_id [Required]: string: The deck id.
#     pile_name [Required]: string: The name of the pile.
#     """
#     url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/shuffle/"
#     response = requests.get(url)
#     return response.json()

# def list_pile(deck_id: str, pile_name: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     List cards in a pile.
    
#     Parameters:
#     deck_id [Required]: string: The deck id.
#     pile_name [Required]: string: The name of the pile.
#     """
#     url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/list/"
#     print(url)
#     response = requests.get(url)

#     print("Response Status Code:", response.status_code)
#     print("Response Text:", response.text)  # Print the raw response text for debugging
    
#     return response.json()

# def draw_from_pile(deck_id: str, pile_name: str, cards: Optional[str] = None, count: Optional[int] = None, draw_type: Optional[str] = "", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
#     """
#     Draw cards from a pile.
    
#     Parameters:
#     deck_id [Required]: string: The deck id.
#     pile_name [Required]: string: The name of the pile.
#     cards [Optional]: string: Comma-separated card codes to draw.
#     count [Optional]: integer: Number of cards to draw.
#     draw_type [Optional]: string: 'bottom' or 'random' for draw type.
#     """
#     path = "draw/"
#     if draw_type in ["bottom", "random"]:
#         path = f"{draw_type}/"
#     url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/{path}"
#     params = {}
#     if cards:
#         params['cards'] = cards
#     if count:
#         params['count'] = count
#     response = requests.get(url, params=params)
#     return response.json()

def return_cards(deck_id: str, cards: Optional[str] = None, pile_name: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Return cards to the main deck or a pile.
    
    Parameters:
    deck_id [Required]: string: The deck id.
    cards [Optional]: string: Comma-separated list of card codes to return.
    pile_name [Optional]: string: The name of the pile to return cards to.
    """
    if pile_name:
        url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/return/"
    else:
        url = f"https://deckofcardsapi.com/api/deck/{deck_id}/return/"
    params = {}
    if cards:
        params['cards'] = cards
    response = requests.get(url, params=params)
    return response.json()