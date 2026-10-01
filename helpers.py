import random
import string
import uuid
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainNoAuthPageLocators, AuthPopUpLocators, RegistrationPopUpLocators, MainAuthPageLocators
from urls import MAIN_PAGE_URL

WAIT_TIMEOUT = 10
DEFAULT_PASSWORD = "Qwerty123"

def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(MAIN_PAGE_URL)
    return driver

def get_wait(driver, timeout=WAIT_TIMEOUT):
    return WebDriverWait(driver, timeout)

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_user_data():
    unique = uuid.uuid4().hex[:8]
    return {"email": f"user_{unique}@yandex.ru", "password": DEFAULT_PASSWORD}

def generate_invalid_user_data():
    unique = uuid.uuid4().hex[:8]
    return {"email": f"user_{unique}_yandex.ru", "password": DEFAULT_PASSWORD}

def generate_product_data():
    return {
        "name": f"Product_{generate_random_string(5)}",
        "description": f"Desc_{generate_random_string(15)}",
        "price": random.randint(100, 50000)
    }

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
