from conftest import *
import allure


class TestLogin:

    @allure.title('Проверка успешной авторизации существующего пользовате')
    @allure.description('В ответе проверяются код и тело, в том числе получение accessToken и refreshToken')
    def test_login_existing_account_successfully(self, create_new_user_and_delete):
        body = create_new_user_and_delete[0]
        response = requests.post(USER_LOGIN, data=body)
        res = response.json()
        assert response.status_code == 200
        assert res['success'] is True
        assert 'accessToken' in res.keys()
        assert 'refreshToken' in res.keys()
        assert res['user']['email'] == create_new_user_and_delete[0]['email']
        assert res['user']['name'] == create_new_user_and_delete[0]['name']

    @allure.title('Проверка на авторизацию с неверным логином и паролем')
    @pytest.mark.parametrize('body', [{
                'email': create_random_email(),
                'password': DataUser.password,
            },
            {
                'email': DataUser.email,
                'password': create_random_password(),
            }])
    def test_login_with_wrong_login_or_password_error(self, body):
        response = requests.post(USER_LOGIN, data=body)
        assert (response.status_code == 401 and
                response.json() == {"success": False,
                                    "message": "email or password are incorrect"})

