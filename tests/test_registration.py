from helpers import get_wait, generate_user_data, generate_invalid_user_data, create_user
from locators import RegistrationPopUpLocators, MainAuthPageLocators
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    def test_registration_with_valid_data(self, driver):
        user_data = generate_user_data()
        wait = get_wait(driver)
        create_user(driver, wait, user_data["email"], user_data["password"])

        assert wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
        assert wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_EXIT))

    def test_registration_with_invalid_email(self, driver):
        user_data = generate_invalid_user_data()
        wait = get_wait(driver)
        create_user(driver, wait, user_data["email"], user_data["password"])

        assert wait.until(EC.visibility_of_element_located(RegistrationPopUpLocators.TEXT_ERROR))

    def test_registration_with_existed_user(self, driver, registered_user_data):
        wait = get_wait(driver)
        create_user(driver, wait, registered_user_data["email"], registered_user_data["password"])

        assert wait.until(EC.visibility_of_element_located(RegistrationPopUpLocators.TEXT_ERROR))
        assert wait.until(EC.visibility_of_element_located(RegistrationPopUpLocators.INPUT_EMAIL_ERROR))
        assert wait.until(EC.visibility_of_element_located(RegistrationPopUpLocators.INPUT_PASSWORD_ERROR))
        assert wait.until(EC.visibility_of_element_located(RegistrationPopUpLocators.INPUT_REPEAT_PASSWORD_ERROR))

