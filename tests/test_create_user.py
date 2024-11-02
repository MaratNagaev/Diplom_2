import pytest
import allure
from urls import *
from data import *
import requests


class TestCreation:
    @allure.title('Проверка успешного создания уникального пользователя')
    @allure.description('В ответе проверяются код и тело, в том числе '
                        'получение accessToken и refreshToken')
    def test_create_new_account_successfully(self):
        body = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_name()
        }
        response = requests.post(USER_REGISTER, data=body)
        res = response.json()
        assert response.status_code == 200
        assert res['success'] is True
        assert 'accessToken' in res.keys()
        assert 'refreshToken' in res.keys()
        assert res['user']['email'] == body['email']
        assert res['user']['name'] == body['name']
        access_token = res['accessToken']
        requests.delete(USER_DELETE, headers={'Authorization': access_token})

    @allure.title('Проверка на создание пользователя с незаполненным обязательным полем')
    @pytest.mark.parametrize('creds', DataUser.creds_with_empty_fields)
    def test_create_account_with_required_field_is_empty(self, creds):
        response = requests.post(USER_REGISTER, data=creds)
        assert (response.status_code == 403 and
                response.json() == {'success': False, 'message': 'Email, password and name are required fields'})

    @allure.title('Проверка на создание пользователя, который уже зарегистрировано.')
    @allure.description('В тесте используется email уже зарегистрированного аккаунта. Если новый аккаунт '
                        'все же создается, то удаляется из базы после теста.')
    def test_create_user_is_already_registered(self):
        body = {
            'email': DataUser.email,
            'password': create_random_password(),
            'name': create_random_name()
        }
        response = requests.post(USER_REGISTER, data=body)
        assert (response.status_code == 403 and
                response.json() == {'success': False, 'message': 'User already exists'})
