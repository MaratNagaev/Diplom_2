# Дипломный проект. Задание 2: API 

## Автотесты для сервиса 'Stellar Burgers'

## Файлы:
- allure_results - директория отчета о тестировании
- tests/test_create_user.py - проверки на создание пользователя
- tests/test_get_user_orders.py - проверки на получение заказов
- tests/test_login.py - проверки логина пользователя
- tests/test_order_create.py - проверки на создание заказа
- tests/test_update_user.py - проверки изменения данных пользователя
- conftest.py - фикстура создания\удаления юзера\заказов
- data.py - файл с предопределенными тестовыми данными, передаваемые в запросах
- generators.py - методы генерации данных для регистрации
- urls.py - эндпоинты и url-адрес сервиса
- requirements.txt - файл с зависимостями

Перед началом работы с репозиторием требуется установить зависимости: 
```
pip install -r requirements.txt
```
Запустить тесты:
```
pytest tests --alluredir=allure_results
```
Просмотреть отчет о тестировании:
```
allure serve allure_results
```