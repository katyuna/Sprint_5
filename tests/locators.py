from selenium.webdriver.common.by import By

class MainNoAuthPageLocators:
    BUTTON_ENTER_AND_REG = (By.XPATH, './/button[text()="Вход и регистрация"]')

class MainAuthPageLocators:
    BUTTON_AVATAR = (By.XPATH, './/button[@class="circleSmall"]')
    BUTTON_EXIT = (By.XPATH, './/button[text()="Выйти"]')

class AuthPopUpLocators:
    BUTTON_NO_ACC = (By.XPATH, './/button[text()="Нет аккаунта"]')

class RegistrationPopUpLocators:
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    INPUT_REPEAT_PASSWORD = (By.NAME, "submitPassword")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, './/button[text()="Создать аккаунт"]')

