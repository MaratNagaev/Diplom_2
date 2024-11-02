import allure
from conftest import *


class TestUpdateUser:

    updated_user_data = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }

    @allure.title('Проверка изменения данных авторизованного пользователя')
    def test_update_authorized_user_successfully(self, create_new_user_and_delete):
        response = requests.patch(USER_UPDATE, headers={
            'Authorization': create_new_user_and_delete[1]['accessToken']}, data=self.updated_user_data)
        res = response.json()
        assert response.status_code == 200
        assert res['success'] is True
        assert res['user']['email'] == self.updated_user_data['email']
        assert res['user']['name'] == self.updated_user_data['name']

    @allure.title('Проверка изменения данных неавторизованного пользователя')
    def test_update_unauthorized_user_error(self):
        response = requests.patch(USER_UPDATE, data=self.updated_user_data)
        assert (response.status_code == 401 and
                response.json() == {'success': False,
                                    'message': 'You should be authorised'})
