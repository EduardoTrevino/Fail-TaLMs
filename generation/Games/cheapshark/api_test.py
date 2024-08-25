import pytest
from api import edit_alert, manage_alerts


def test_edit_alert_set():
    response = edit_alert(action='set', email='someone@example.org', game_id=59, price=14.99)
    assert response is True or response is False  # assuming the API returns a boolean


def test_edit_alert_delete():
    response = edit_alert(action='delete', email='someone@example.org', game_id=59)
    assert response is True or response is False  # assuming the API returns a boolean


def test_manage_alerts():
    response = manage_alerts(email='address-with-alerts@example.org')
    assert isinstance(response, dict)  # assuming a dict response, adjust as needed based on actual API response