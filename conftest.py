import pytest
import string
import random
import uuid
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import MainNoAuthPageLocators, AuthPopUpLocators, RegistrationPopUpLocators, MainAuthPageLocators, \
    ProfilePageLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-desk.education-services.ru")
    yield driver
    driver.quit()

@pytest.fixture
def wait_5(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def new_user_data():
    unique = uuid.uuid4().hex[:8]
    return {"email": f"user_{unique}@yandex.ru", "password": "Qwerty123"}

@pytest.fixture
def invalid_user_data():
    return {"email": "user_yandex.ru", "password": "Qwerty123"}

@pytest.fixture
def random_product():

    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    name = f"Product_{generate_random_string(5)}"

    random_product = {
        "name": name,
        "description": f"Desc_{generate_random_string(15)}",
        "price": random.randint(100, 50000),
        "product_title": ProfilePageLocators.product_title(name)
    }

    return random_product

@pytest.fixture(scope="session")
def registered_user_data():
    unique = uuid.uuid4().hex[:8]
    user_data = {"email": f"user_{unique}@yandex.ru", "password": "Qwerty123"}

    setup_driver = webdriver.Chrome()
    setup_driver.maximize_window()
    setup_driver.get("https://qa-desk.education-services.ru")
    setup_wait = WebDriverWait(setup_driver, 10)
    create_user(setup_driver, setup_wait, user_data["email"], user_data["password"])
    setup_wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
    setup_driver.quit()

    return user_data

def create_user(driver, wait, email, password):
    wait.until(EC.element_to_be_clickable(MainNoAuthPageLocators.BUTTON_ENTER_AND_REG)).click()
    wait.until(EC.visibility_of_element_located(AuthPopUpLocators.BUTTON_NO_ACC)).click()

    wait.until(EC.visibility_of_element_located(RegistrationPopUpLocators.INPUT_EMAIL))

    driver.find_element(*RegistrationPopUpLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*RegistrationPopUpLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*RegistrationPopUpLocators.INPUT_REPEAT_PASSWORD).send_keys(password)
    driver.find_element(*RegistrationPopUpLocators.BUTTON_CREATE_ACCOUNT).click()

def login_user(driver, wait, email, password):
    wait.until(EC.element_to_be_clickable(MainNoAuthPageLocators.BUTTON_ENTER_AND_REG)).click()
    wait.until(EC.visibility_of_element_located(AuthPopUpLocators.INPUT_EMAIL)).send_keys(email)
    driver.find_element(*AuthPopUpLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*AuthPopUpLocators.BUTTON_SUBMIT).click()

def logout_user(driver, wait):
    wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_EXIT)).click()




