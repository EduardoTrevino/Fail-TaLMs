from api import (
    get_all_characters, get_character_by_id,
    get_all_episodes, get_episode_by_id,
    get_all_locations, get_location_by_id,
    get_all_quotes
)

def test_get_all_characters():
    response = get_all_characters()
    assert isinstance(response, list) and len(response) > 0

def test_get_character_by_id():
    response = get_character_by_id(1)
    assert isinstance(response, dict) and response['id'] == 1

def test_get_all_episodes():
    response = get_all_episodes()
    assert isinstance(response, list) and len(response) > 0

def test_get_episode_by_id():
    response = get_episode_by_id(1)
    assert isinstance(response, dict) and response['id'] == 1

def test_get_all_locations():
    response = get_all_locations()
    assert isinstance(response, list) and len(response) > 0

def test_get_location_by_id():
    response = get_location_by_id(1)
    assert isinstance(response, dict) and response['id'] == 1

def test_get_all_quotes():
    response = get_all_quotes()
    assert isinstance(response, list) and len(response) > 0

if __name__ == "__main__":
    test_get_all_characters()
    test_get_character_by_id()
    test_get_all_episodes()
    test_get_episode_by_id()
    test_get_all_locations()
    test_get_location_by_id()
    test_get_all_quotes()
    print("All tests passed!")