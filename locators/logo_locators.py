from selenium.webdriver.common.by import By


class LogoLocators:
    LOGO_YANDEX = By.XPATH, ".//*[@class='Header_LogoYandex__3TSOI']"
    LOGO_SCOOTER = By.XPATH, ".//*[@class='Header_LogoScooter__3lsAR']"
    HEADER_DZEN = By.ID, "dzen-header"
