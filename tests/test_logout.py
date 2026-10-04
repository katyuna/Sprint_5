from helpers import get_wait, login_user, logout_user
from locators import MainNoAuthPageLocators
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:
    def test_logout(self, driver, registered_user_data):
        wait = get_wait(driver)
        login_user(driver, wait, registered_user_data["email"], registered_user_data["password"])

        logout_user(driver, wait)

        assert wait.until(EC.visibility_of_element_located(MainNoAuthPageLocators.BUTTON_ENTER_AND_REG))

