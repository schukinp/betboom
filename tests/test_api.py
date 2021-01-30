from helper import *


class TestApi:
    def test_register_user(self):
        """Регистрация (можем зарегистрировать пользователя)"""
        username = generate_username()
        request = register_user(username)
        response = request.json()
        assert request.status_code == 201
        assert response['success'] is True
        assert response['result']['user']['login'] == username

    def test_login(self):
        """Авторизация(можем авторизовать пользователя)"""
        username = generate_username()
        register_user(username)
        request = login_as(username)
        response = request.json()
        assert request.status_code == 200
        assert response['success'] is True
        assert response['result']['user']['login'] == username
        assert response['result']['ssid']

    def test_add_contact(self):
        """Добавление контакта (можем добавить контакт пользователя)"""
        username = generate_username()
        phone = generate_phone()
        register_user(username)
        login_request = login_as(username)
        login_response = login_request.json()
        ssid = login_response['result']['ssid']
        add_contact_request = add_contact(ssid, phone)
        add_contact_response = add_contact_request.json()
        assert add_contact_request.status_code == 200
        assert add_contact_response['success'] is True
        assert add_contact_response['result']['user']['contacts'][0]['content'] == phone

    def test_delete_contact(self):
        """Удаление контакта (можем удалить контакт пользователя)"""
        username = generate_username()
        phone = generate_phone()
        register_user(username)
        login_request = login_as(username)
        login_response = login_request.json()
        ssid = login_response['result']['ssid']
        add_contact_request = add_contact(ssid, phone)
        add_contact_response = add_contact_request.json()
        contact_id = add_contact_response['result']['user']['contacts'][0]['id']
        delete_request = delete_contact(ssid, contact_id)
        assert delete_request.status_code == 200
        assert add_contact_response['success'] is True
