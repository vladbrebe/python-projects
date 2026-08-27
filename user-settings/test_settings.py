import pytest

from settings import add_setting, delete_setting, update_setting, view_settings


def make_settings():
    """A fresh settings dictionary for each test to work on."""
    return {"brightness": "high", "zoom": "out", "contrast": "small"}


def test_add_new_setting():
    settings = make_settings()
    message = add_setting(settings, ("Volume", "LOUD"))
    assert message == "Setting 'volume' added with value 'loud' successfully!"
    assert settings["volume"] == "loud"


def test_add_lower_cases_the_key_and_value():
    settings = make_settings()
    add_setting(settings, ("VOLUME", "Loud"))
    assert "VOLUME" not in settings
    assert settings["volume"] == "loud"


def test_view_empty_settings():
    assert view_settings({}) == "No settings available."