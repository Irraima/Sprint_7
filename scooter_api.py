import allure
import requests
import urls


class CreateACourierApi:
    @staticmethod
    @allure.step("Отправляем запрос на создание курьера")
    def create_a_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATING_A_COURIER_ENDPOINT, json=body)


class AuthACourierApi:
    @staticmethod
    @allure.step("Авторизуем курьера")
    def auth_a_courier(login_pass):
        return requests.post(
            urls.BASE_URL + urls.COURIER_LOGIN_ENDPOINT, json=login_pass
        )

    @staticmethod
    @allure.step("Удаляем курьера")
    def delete_a_courier(id):
        return requests.delete(urls.BASE_URL + urls.DELETE_A_COURIER_ENDPOINT, json=id)


class CreateAnOrderApi:
    @staticmethod
    @allure.step("Создаём заказ")
    def create_an_order(payload):
        return requests.post(urls.BASE_URL + urls.CREATING_AN_ORDER_ENDPOINT, json=payload)


class ReceivingAnOrderList:
    @staticmethod
    @allure.step("Отправляем запрос на получение списка заказов")
    def receiving_an_orders_list():
        return requests.get(urls.BASE_URL + urls.RECEIVING_AN_ORDERS_LIST_ENDPOINT)
