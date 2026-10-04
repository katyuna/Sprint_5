import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainAuthPageLocators, MainNoAuthPageLocators
from helpers import create_driver, get_wait, generate_user_data, create_user, logout_user

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture
def registered_user_data(driver):
    user_data = generate_user_data()
    wait = get_wait(driver)

    create_user(driver, wait, user_data["email"], user_data["password"])
    wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
    logout_user(driver, wait)
    wait.until(EC.visibility_of_element_located(MainNoAuthPageLocators.BUTTON_ENTER_AND_REG))

    return user_data
