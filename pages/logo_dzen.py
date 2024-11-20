from data import Url
from locators.logo_locators import LogoLocators
from pages.base_page import BasePage
import allure


class Logo(BasePage):
    @allure.step('Клик на логотип "Яндекс" для открытия нового окна "Яндекс Дзен"')
    def click_logo_yandex(self):
        self.click_element(LogoLocators.LOGO_YANDEX)

    @allure.step('Клик на логотип "Самокат" для перехода на домашнюю страницу')
    def check_logo_scooter_change_url_home_page(self):
        self.click_element(LogoLocators.LOGO_SCOOTER)
        return self.get_url()

    @allure.step('Открытие страницы "Самокат"')
    def open_main_page(self):
        self.open_page(Url.URL_SAMOKAT)

    @allure.step('Проверка открытия страницы "Яндекс Дзен"')
    def check_dzen_logo(self):
        self.find_element(LogoLocators.HEADER_DZEN)
        return self.get_url()