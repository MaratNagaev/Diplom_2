import allure
from conftest import *


class TestCreateOrder:
    @allure.title('Проверка на создание заказа авторизированного пользователя с указанными ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientsData.burger_1, IngredientsData.burger_2])
    def test_create_order_authorized_user_successfully(self, create_new_user_and_delete, burger_ingredients):
        header = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        body = {'ingredients': [burger_ingredients]}
        response = requests.post(ORDER_CREATE, data=body, headers=header)
        res = response.json()
        assert response.status_code == 200
        assert res['success'] is True
        assert 'name' in res.keys()
        assert 'number' in res['order'].keys()

    @allure.title('Проверка на создание заказа НЕавторизированного пользователя с указанными ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientsData.burger_1, IngredientsData.burger_2])
    def test_create_order_unauthorized_user_successfully(self, burger_ingredients):
        body = {'ingredients': [burger_ingredients]}
        response = requests.post(ORDER_CREATE, data=body)
        assert (response.status_code == 200 and
                response.json()["success"] is True)

    @allure.title('Проверка на создание заказа авторизированным пользователем с неуказанными ингредиентами')
    def test_create_order_authorized_user_with_empty_ingredients_error(self, create_new_user_and_delete):
        header = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        body = {'ingredients': []}
        response = requests.post(ORDER_CREATE, data=body, headers=header)
        assert (response.status_code == 400 and
                response.json() == {'success': False,
                                    'message': 'Ingredient ids must be provided'})

    @allure.title('Проверка на создание заказа НЕавторизированным пользователем с неуказанными ингредиентами')
    def test_create_order_unauthorized_user_with_empty_ingredients_error(self):
        body = {'ingredients': []}
        response = requests.post(ORDER_CREATE, data=body, headers=HEADERS)
        assert (response.status_code == 400 and
                response.json() == {'success': False,
                                    'message': 'Ingredient ids must be provided'})

    @allure.title('Проверка на создание заказа с неверным хешем ингредиентов')
    @allure.description('В запрос передается невалиднй хеш ингредиента.')
    def test_create_order_invalid_ingredients_authorized_user_error(self, create_new_user_and_delete):
        header = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        body = {'ingredients': [IngredientsData.invalid_hash_ingredient]}
        response = requests.post(ORDER_CREATE, data=body, headers=header)
        assert response.status_code == 500
