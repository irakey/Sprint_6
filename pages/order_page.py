from pages.base_page import BasePage
from locators.order_page_locators import OrderButtonLocators, OrderFormLocators1, OrderFormLocators2, OrderPopUpLocators, \
    CookieBar
import allure


class OrderPage(BasePage):

    @allure.step('Переход к форме для заказа с помощью кнопки "Заказать" вверху страницы')
    def check_button_order_top(self):
        self.click_element(OrderButtonLocators.BUTTON_ORDER_TOP)
        return self.find_element(OrderFormLocators1.FIELD_NAME)

    @allure.step('Переход к форме для заказа с помощью кнопки "Заказать" по центру страницы')
    def check_button_to_order_center(self):
        self.scroll_to_element(OrderButtonLocators.BUTTON_ORDER_CENTER)
        self.click_element(OrderButtonLocators.BUTTON_ORDER_CENTER)
        return self.find_element(OrderFormLocators1.FIELD_NAME)

    @allure.step('Заполнение формы для заказа')
    def add_user_data_to_form_order(self, name, last_name, address, metro, phone, rental_day,
                                    comment_for_courier):
        self.click_element(CookieBar.ACCEPT_COOKIE)
        self.add_text_to_element(OrderFormLocators1.FIELD_NAME, name)
        self.add_text_to_element(OrderFormLocators1.FIELD_LAST_NAME, last_name)
        self.add_text_to_element(OrderFormLocators1.FIELD_ADDRESS, address)
        self.click_element(OrderFormLocators1.FIELD_METRO)
        self.click_element(metro)
        self.add_text_to_element(OrderFormLocators1.FIELD_PHONE, phone)
        self.click_element(OrderFormLocators1.BUTTON_NEXT)
        self.click_element(OrderFormLocators2.FIELD_DATA_ORDER)
        self.click_element(OrderFormLocators2.DELIVERY_DATE_TOMORROW)
        self.click_element(OrderFormLocators2.FIELD_RENTAL_PERIOD)
        self.click_element(rental_day)
        self.click_element(OrderFormLocators2.CHECKBOX_BLACK_COLOR)
        self.add_text_to_element(OrderFormLocators2.FIELD_COMMENT_FOR_COURIER, comment_for_courier)
        self.click_element(OrderFormLocators2.BUTTON_TO_ORDER_IN_FORM)
        return self.find_element(OrderPopUpLocators.BUTTON_YES_ORDER)

    @allure.step('Получение поп-апа об успешном оформлении заказа')
    def check_window_successful_order(self):
        self.click_element(OrderPopUpLocators.BUTTON_YES_ORDER)
        return self.get_text_from_element(OrderPopUpLocators.POP_UP_WINDOW_SUCCESSFUL_ORDER)