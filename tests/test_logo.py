from pages.logo_dzen import Logo
from data import Url
import allure


@allure.title('Тестирование переходов по клику на логотипы')
class TestLogo:

    @allure.title('Проверка перехода на "Яндекс Дзен" по клику на лого "Яндекс"')
    def test_check_logo_yandex_open_new_window_dzen(self, driver):
        logo = Logo(driver)
        logo.open_main_page()
        logo.click_logo_yandex()
        logo.switch_to_new_window()
        new_url = logo.check_dzen_logo()
        assert Url.URL_DZEN in new_url

    @allure.title('Кликаем на логотип "Самокат" и проверяем переход на страницу "Яндекс Самокат"')
    def test_check_logo_scooter_change_url_home_page(self, driver):
        logo = Logo(driver)
        new_url = logo.check_logo_scooter_change_url_home_page()
        assert new_url == Url.URL_SAMOKAT
