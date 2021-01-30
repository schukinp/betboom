import pytest
from pages.home_page import HomePage
from data import base_url
from helper import register_user, generate_username, login_as


@pytest.mark.usefixtures('set_browser')
class TestUsername:
    def test_username_is_correct(self):
        """Проверить что имя в span.username отображается правильно"""
        username = generate_username()
        register_user(username)
        login_request = login_as(username)
        login_response = login_request.json()
        ssid = login_response['result']['ssid']
        HomePage().open_url(base_url + f'session/{ssid}')
        HomePage().check_username_is(username)
