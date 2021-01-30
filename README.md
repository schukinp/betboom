# Bet Boom

На проекте используется: 
* selenium wrapper [selene](https://github.com/yashaka/selene) для UI тестов
* библиотека requests для API тестов


# Предусловия

* [Python 3.6](https://www.python.org/)
* Браузер [Chrome](https://www.google.com/chrome/)


# Установка
* Разверните и запустите локально проект Без или С Docker из [репозитория](https://gitlab.com/kenshi2150/test-auto-test)
* Установите зависимости из текущего репозитория`pip install -r requirements.txt`

# Запуск тестов

```
$ pytest tests/
```

# Результат запуска тестов 
```============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /Users/apple/PycharmProjects/betboom/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/apple/PycharmProjects/betboom/tests
plugins: Faker-5.8.0
collecting ... collected 5 items

test_api.py::TestApi::test_register_user 
test_api.py::TestApi::test_login 
test_api.py::TestApi::test_add_contact 
test_api.py::TestApi::test_delete_contact 
test_ui.py::TestUsername::test_username_is_correct PASSED                          [ 20%]PASSED                                  [ 40%]PASSED                            [ 60%]PASSED                         [ 80%]

============================== 5 passed in 2.64s ===============================

Process finished with exit code 0
PASSED                [100%]```