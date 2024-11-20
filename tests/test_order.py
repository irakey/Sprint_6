import pytest
from data import Url, AuthData
from pages.order_page import OrderPage
from locators.order_page_locators import OrderFormLocators1, OrderFormLocators2
import allure


@allure.title('Оформление заказа')
class TestOrderPage:
    @allure.title('Переход к форме для заказа с помощью кнопки "Заказать" вверху страницы')
    def test_check_button_to_order_top(self, driver):
        driver.get(Url.URL_SAMOKAT)
        order_page = OrderPage(driver)
        element = order_page.check_button_order_top()
        assert element is not None

    @allure.title('Переход к форме для заказа с помощью кнопки "Заказать" по центру страницы')
    def test_check_button_to_order_center(self, driver):
        driver.get(Url.URL_SAMOKAT)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_center()
        assert element is not None

    @allure.title('Оформление заказа с разными тестовыми данными')
    @pytest.mark.parametrize(
        "name, last_name, address, metro, phone, rental_day, comment_for_courier",
        [
            (AuthData.name_1, AuthData.last_name_1, AuthData.address_1, OrderFormLocators1.METRO_TECHNOPARK,
             AuthData.phone_1, OrderFormLocators2.RENT_1_DAY,
             AuthData.comment_empty),
            (AuthData.name_2, AuthData.last_name_2, AuthData.address_2, OrderFormLocators1.METRO_AVTOZADOSKAYA,
             AuthData.phone_2, OrderFormLocators2.RENT_2_DAYS,
             AuthData.comment_for_courier_1)
        ],
        ids=['Оформление заказа с данными первого пользователя', 'Оформление заказа с данными второго пользователя']
    )
    def test_order_with_different_user_data(self, driver, name, last_name, address, metro, phone, rental_day, comment_for_courier):
        driver.get(Url.URL_SAMOKAT)
        order_page = OrderPage(driver)
        order_page.check_button_order_top()
        order_page.add_user_data_to_form_order(name, last_name, address, metro, phone, rental_day,
                                               comment_for_courier)
        success_screen_text = order_page.check_window_successful_order()
        assert 'Заказ оформлен' in success_screen_text

