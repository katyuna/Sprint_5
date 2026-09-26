from conftest import create_user
from tests.locators import RegistrationPopUpLocators, MainAuthPageLocators
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    def test_registration_with_valid_data(self, driver, new_user_data, wait_5):
        create_user(driver, wait_5, new_user_data["email"], new_user_data["password"])

        assert wait_5.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
        assert wait_5.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_EXIT))

    def test_registration_with_invalid_email(self, driver, invalid_user_data, wait_5):
        create_user(driver, wait_5, invalid_user_data["email"], invalid_user_data["password"])

        assert wait_5.until(EC.visibility_of_element_located(RegistrationPopUpLocators.TEXT_ERROR))

    def test_registration_with_existed_user(self, driver, registered_user_data, wait_5):
        create_user(driver, wait_5, registered_user_data["email"], registered_user_data["password"])

        assert wait_5.until(EC.visibility_of_element_located(RegistrationPopUpLocators.TEXT_ERROR))
        assert wait_5.until(EC.visibility_of_element_located(RegistrationPopUpLocators.INPUT_EMAIL_ERROR))
        assert wait_5.until(EC.visibility_of_element_located(RegistrationPopUpLocators.INPUT_PASSWORD_ERROR))
        assert wait_5.until(EC.visibility_of_element_located(RegistrationPopUpLocators.INPUT_REPEAT_PASSWORD_ERROR))

