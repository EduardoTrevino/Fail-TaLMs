from api import (
    get_all_cards, get_card_by_id, get_all_sets, get_set_by_code,
    generate_booster_pack, get_all_types, get_all_subtypes,
    get_all_supertypes, get_all_formats, get_cards_by_name,
    get_cards_by_foreign_name
)

def test_get_all_cards():
    response = get_all_cards(page=1, page_size=2)
    assert 'cards' in response, "Cards key not in response"

def test_get_card_by_id():
    response = get_card_by_id("02ea5ddc89d7847abc77a0fbcbf2bc74e6456559")
    assert 'card' in response, "Card key not in response"
    assert response['card']['name'] == 'Archangel Avacyn', "Card name does not match"

def test_get_all_sets():
    response = get_all_sets()
    assert 'sets' in response, "Sets key not in response"

def test_get_set_by_code():
    response = get_set_by_code("KTK")
    assert 'set' in response, "Set key not in response"
    assert response['set']['name'] == 'Khans of Tarkir', "Set name does not match"

def test_generate_booster_pack():
    response = generate_booster_pack("KTK")
    assert 'cards' in response, "Cards key not in response"

def test_get_all_types():
    response = get_all_types()
    assert 'types' in response, "Types key not in response"

def test_get_all_subtypes():
    response = get_all_subtypes()
    assert 'subtypes' in response, "Subtypes key not in response"

def test_get_all_supertypes():
    response = get_all_supertypes()
    assert 'supertypes' in response, "Supertypes key not in response"

def test_get_all_formats():
    response = get_all_formats()
    assert 'formats' in response, "Formats key not in response"

def test_get_cards_by_name():
    response = get_cards_by_name("Archangel Avacyn")
    assert 'cards' in response, "Cards key not in response"

def test_get_cards_by_foreign_name():
    response = get_cards_by_foreign_name(name="Arcángel Avacyn", language="Spanish")
    assert 'cards' in response, "Cards key not in response"