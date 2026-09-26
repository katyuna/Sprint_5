from conftest import login_user
from tests.locators import MainAuthPageLocators
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def test_login_with_valid_data(self, driver, registered_user_data, wait_5):
        login_user(driver, wait_5, registered_user_data["email"], registered_user_data["password"])

        assert wait_5.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
        assert 'User' in wait_5.until(EC.visibility_of_element_located(MainAuthPageLocators.TEXT_PROFILE_TEXT)).text

