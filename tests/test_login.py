from helpers import get_wait, login_user
from locators import MainAuthPageLocators
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def test_login_with_valid_data(self, driver, registered_user_data):
        wait = get_wait(driver)
        login_user(driver, wait, registered_user_data["email"], registered_user_data["password"])

        assert wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
        assert 'User' in wait.until(EC.visibility_of_element_located(MainAuthPageLocators.TEXT_PROFILE_TEXT)).text

