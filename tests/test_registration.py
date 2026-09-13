from tests.locators import MainNoAuthPageLocators, RegistrationPopUpLocators, AuthPopUpLocators, MainAuthPageLocators
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    def test_registration_with_valid_data(self, driver, new_user_data, wait_5):
        driver.find_element(*MainNoAuthPageLocators.BUTTON_ENTER_AND_REG).click()
        driver.find_element(*AuthPopUpLocators.BUTTON_NO_ACC).click()

        wait_5.until(EC.visibility_of_element_located(RegistrationPopUpLocators.INPUT_EMAIL))

        driver.find_element(*RegistrationPopUpLocators.INPUT_EMAIL).send_keys(new_user_data["email"])
        driver.find_element(*RegistrationPopUpLocators.INPUT_PASSWORD).send_keys(new_user_data["password"])
        driver.find_element(*RegistrationPopUpLocators.INPUT_REPEAT_PASSWORD).send_keys(new_user_data["password"])
        driver.find_element(*RegistrationPopUpLocators.BUTTON_CREATE_ACCOUNT).click()

        assert wait_5.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
        assert wait_5.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_EXIT))

    #def test_registration_with_invalid_email(self, driver):
     #   pass