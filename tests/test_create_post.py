from conftest import login_user
from tests.locators import MainNoAuthPageLocators, AuthPopUpLocators, MainAuthPageLocators, CreatePostPageLocators, \
    ProfilePageLocators
from selenium.webdriver.support import expected_conditions as EC

class TestCreatePost:
    def test_create_post_with_no_auth(self, driver, wait_5):
        wait_5.until(EC.element_to_be_clickable(MainNoAuthPageLocators.BUTTON_CREATE_POST)).click()

        assert wait_5.until(EC.visibility_of_element_located(AuthPopUpLocators.TEXT_NO_AUTH_TEXT))

    def test_create_post_with_auth(self, driver, registered_user_data, random_product, wait_5):
        login_user(driver, wait_5, registered_user_data["email"], registered_user_data["password"])

        wait_5.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
        wait_5.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_CREATE_POST_BUTTON)).click()

        name_input = wait_5.until(EC.visibility_of_element_located(CreatePostPageLocators.INPUT_PRODUCT_NAME))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", name_input)
        name_input.send_keys(random_product["name"])

        description_input = wait_5.until(EC.visibility_of_element_located(CreatePostPageLocators.TEXTAREA_PRODUCT_DESCRIPTION))
        driver.execute_script("arguments[0].scrollIntoView();", description_input)
        description_input.send_keys(random_product["description"])

        price_input = wait_5.until(EC.visibility_of_element_located(CreatePostPageLocators.INPUT_PRICE))
        driver.execute_script("arguments[0].scrollIntoView();", price_input)
        price_input.send_keys(str(random_product["price"]))

        category_button = wait_5.until(EC.element_to_be_clickable(CreatePostPageLocators.DROPDOWN_CATEGORY))
        category_button.click()
        wait_5.until(EC.element_to_be_clickable(CreatePostPageLocators.SPAN_CATEGORY)).click()

        city_button = wait_5.until(EC.element_to_be_clickable(CreatePostPageLocators.DROPDOWN_CITY))
        driver.execute_script("arguments[0].scrollIntoView();", city_button)
        city_button.click()
        wait_5.until(EC.element_to_be_clickable(CreatePostPageLocators.SPAN_CITY)).click()

        condition_radio = wait_5.until(EC.element_to_be_clickable(CreatePostPageLocators.RADIOBUTTON_CONDITION))
        driver.execute_script("arguments[0].scrollIntoView();", condition_radio)
        condition_radio.click()

        publish_button = wait_5.until(EC.element_to_be_clickable(CreatePostPageLocators.BUTTON_PUBLISH))
        driver.execute_script("arguments[0].scrollIntoView();", publish_button)
        publish_button.click()

        import time
        time.sleep(2)

        wait_5.until(EC.element_to_be_clickable(MainAuthPageLocators.BUTTON_AVATAR)).click()

        my_posts_block = wait_5.until(EC.visibility_of_element_located(ProfilePageLocators.MY_POSTS_BLOCK))
        driver.execute_script("arguments[0].scrollIntoView();", my_posts_block)

        product_title_element = wait_5.until(EC.visibility_of_element_located(random_product["product_title"]))
        driver.execute_script("arguments[0].scrollIntoView();", product_title_element)

        assert product_title_element.is_displayed()








