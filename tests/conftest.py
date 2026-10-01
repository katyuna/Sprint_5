import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainAuthPageLocators
from helpers import create_driver, get_wait, generate_user_data, create_user

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def registered_user_data():
    user_data = generate_user_data()

    setup_driver = create_driver()
    try:
        setup_wait = get_wait(setup_driver)
        create_user(setup_driver, setup_wait, user_data["email"], user_data["password"])
        setup_wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
    finally:
        setup_driver.quit()

    return user_data
