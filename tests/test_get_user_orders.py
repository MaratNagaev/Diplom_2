import allure
from conftest import *


class TestGetOrders:
    @allure.title('Проверка успешного получения заказа для авторизованного пользователя')
    def test_get_orders_authorized_user_successfully(self, create_user_and_order_and_delete):
        header = {'Authorization': create_user_and_order_and_delete[0]}
        response = requests.get(GET_USER_ORDERS, headers=header)
        res = response.json()
        assert response.status_code == 200
        assert res['success'] is True
        assert 'orders' in res.keys()
        assert 'total' in res.keys()

    @allure.title('Проверка на получение зааказа для неавторизованного пользователя')
    def test_get_orders_unauthorized_user_successfully(self):
        response = requests.get(GET_USER_ORDERS, headers=HEADERS)
        assert (response.status_code == 401 and
                response.json() == {'success': False,
                                    'message': 'You should be authorised'})
