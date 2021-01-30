import requests
import random
from data import base_url
import uuid


def register_user(username):
    """Зарегистрироваться"""
    url = base_url + 'api/v1/user/registration'
    data = {"user": {"login": username, "password": "123456"}}
    return requests.request('POST', url, json=data)


def login_as(username):
    """Залогиниться"""
    url = base_url + 'api/v1/user/login'
    data = {"user": {"login": username, "password": "123456"}}
    return requests.request('POST', url, json=data)


def generate_phone():
    """Сгенерировать телефон"""
    num = random.randrange(1111111, 9999999)
    return "+7921" + str(num)


def generate_username():
    """Сгенерировать имя пользователя"""
    return str(uuid.uuid4())[: 10]


def add_contact(ssid, phone):
    """Добавить контакт"""
    url = base_url + 'api/v1/user/contact'
    headers = {'ssid': ssid}
    data = {'contact': {"type": "phone", "content": phone}}
    return requests.request('POST', url, headers=headers, json=data)


def delete_contact(ssid, contact_id):
    """Удалить контакт"""
    url = base_url + f'api/v1/user/contact/{contact_id}'
    headers = {'ssid': ssid}
    return requests.request('DELETE', url, headers=headers)
