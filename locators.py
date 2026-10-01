from selenium.webdriver.common.by import By

class MainNoAuthPageLocators:
    BUTTON_ENTER_AND_REG = (By.XPATH, './/button[text()="Вход и регистрация"]')
    BUTTON_CREATE_POST = (By.XPATH, './/button[text()="Разместить объявление"]')

class MainAuthPageLocators:
    BUTTON_AVATAR = (By.XPATH, './/button[@class="circleSmall"]')
    BUTTON_EXIT = (By.XPATH, './/button[text()="Выйти"]')
    TEXT_PROFILE_TEXT = (By.XPATH, ".//h3[@class='profileText name']")
    BUTTON_CREATE_POST_BUTTON = (By.XPATH, './/button[text()="Разместить объявление"]')

class AuthPopUpLocators:
    BUTTON_NO_ACC = (By.XPATH, './/button[text()="Нет аккаунта"]')
    INPUT_EMAIL = (By.XPATH, './/input[@name="email"]')
    INPUT_PASSWORD = (By.XPATH, './/input[@name="password"]')
    BUTTON_SUBMIT = (By.XPATH, './/button[text()="Войти"]')
    TEXT_NO_AUTH_TEXT = (By.XPATH, './/h1[contains(normalize-space(.), "Чтобы разместить объявление, авторизуйтесь")]')

class RegistrationPopUpLocators:
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    INPUT_REPEAT_PASSWORD = (By.NAME, "submitPassword")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, './/button[text()="Создать аккаунт"]')
    TEXT_ERROR = (By.XPATH, './/span[text() = "Ошибка"]')

    INPUT_EMAIL_ERROR = (By.XPATH, './/input[@name="email"]/parent::div[contains(@class, "inputError")]'    )
    INPUT_PASSWORD_ERROR = (By.XPATH, './/input[@name="password"]/parent::div[contains(@class, "inputError")]')
    INPUT_REPEAT_PASSWORD_ERROR = (By.XPATH, './/input[@name="submitPassword"]/parent::div[contains(@class, "inputError")]')

class CreatePostPageLocators:
    INPUT_PRODUCT_NAME = (By.XPATH, './/input[@name="name"]')
    TEXTAREA_PRODUCT_DESCRIPTION = (By.XPATH, './/textarea[@name="description"]')
    INPUT_PRICE = (By.XPATH, './/input[@name="price"]')
    DROPDOWN_CATEGORY = (By.XPATH, '(.//button[contains(@class, "dropDownMenu_arrowDown") and contains(@class, "dropDownMenu_noDefault")])[1]')
    SPAN_CATEGORY = (By.XPATH, './/span[contains(@class, "dropDownMenu_textColor") and text()="Книги"]')
    DROPDOWN_CITY = (By.XPATH, '(.//button[contains(@class, "dropDownMenu_arrowDown") and contains(@class, "dropDownMenu_noDefault")])[2]')
    SPAN_CITY = (By.XPATH, './/span[contains(@class, "dropDownMenu_textColor") and text()="Санкт-Петербург"]')
    RADIOBUTTON_CONDITION = (By.XPATH, './/div[contains(@class, "radioUnput")]/label[text()="Б/У"]')
    BUTTON_PUBLISH = (By.XPATH, './/button[text()="Опубликовать"]')

class ProfilePageLocators:
    MY_POSTS_BLOCK = (By.XPATH, './/h1[@class="h1" and text()="Мои объявления"]')

    @staticmethod
    def product_title(name):
        return (By.XPATH, f'.//h2[@class="h2" and text()="{name}"]')


