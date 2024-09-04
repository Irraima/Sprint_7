import allure
from scooter_api import ReceivingAnOrderList


class TestReceivingOrderList:
    @allure.step("Проверка запроса списка заказов")
    @allure.description(
        "Создаём запрос на получение списка заказов, проверяем код и тело ответа"
    )
    def test_receiving_orders_list(self):
        receiving_an_orders_list = ReceivingAnOrderList.receiving_an_orders_list()
        orders = receiving_an_orders_list.json()["orders"]
        assert receiving_an_orders_list.status_code == 200 and orders is not None
