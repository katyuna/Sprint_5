from conftest import login_user, logout_user
from tests.locators import MainNoAuthPageLocators
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:
    def test_logout(self, driver, registered_user_data, wait_5):
        login_user(driver, wait_5, registered_user_data["email"], registered_user_data["password"])

        logout_user(driver, wait_5)

        assert wait_5.until(EC.visibility_of_element_located(MainNoAuthPageLocators.BUTTON_ENTER_AND_REG))

