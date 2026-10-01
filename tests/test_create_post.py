from helpers import get_wait, generate_product_data, login_user
from locators import MainNoAuthPageLocators, AuthPopUpLocators, MainAuthPageLocators, CreatePostPageLocators, \
    ProfilePageLocators
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL, CREATE_POST_URL, PROFILE_URL

class TestCreatePost:
    def test_create_post_with_no_auth(self, driver):
        wait = get_wait(driver)
        wait.until(EC.element_to_be_clickable(MainNoAuthPageLocators.BUTTON_CREATE_POST)).click()

        assert wait.until(EC.visibility_of_element_located(AuthPopUpLocators.TEXT_NO_AUTH_TEXT))

    def test_create_post_with_auth(self, driver, registered_user_data):
        product = generate_product_data()
        wait = get_wait(driver)
        login_user(driver, wait, registered_user_data["email"], registered_user_data["password"])

        wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_AVATAR))
        wait.until(EC.visibility_of_element_located(MainAuthPageLocators.BUTTON_CREATE_POST_BUTTON)).click()
        wait.until(EC.url_to_be(CREATE_POST_URL))

        name_input = wait.until(EC.visibility_of_element_located(CreatePostPageLocators.INPUT_PRODUCT_NAME))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", name_input)
        name_input.send_keys(product["name"])

        description_input = wait.until(EC.visibility_of_element_located(CreatePostPageLocators.TEXTAREA_PRODUCT_DESCRIPTION))
        driver.execute_script("arguments[0].scrollIntoView();", description_input)
        description_input.send_keys(product["description"])

        price_input = wait.until(EC.visibility_of_element_located(CreatePostPageLocators.INPUT_PRICE))
        driver.execute_script("arguments[0].scrollIntoView();", price_input)
        price_input.send_keys(str(product["price"]))

        category_button = wait.until(EC.element_to_be_clickable(CreatePostPageLocators.DROPDOWN_CATEGORY))
        category_button.click()
        wait.until(EC.element_to_be_clickable(CreatePostPageLocators.SPAN_CATEGORY)).click()

        city_button = wait.until(EC.element_to_be_clickable(CreatePostPageLocators.DROPDOWN_CITY))
        driver.execute_script("arguments[0].scrollIntoView();", city_button)
        city_button.click()
        wait.until(EC.element_to_be_clickable(CreatePostPageLocators.SPAN_CITY)).click()

        condition_radio = wait.until(EC.element_to_be_clickable(CreatePostPageLocators.RADIOBUTTON_CONDITION))
        driver.execute_script("arguments[0].scrollIntoView();", condition_radio)
        condition_radio.click()

        publish_button = wait.until(EC.element_to_be_clickable(CreatePostPageLocators.BUTTON_PUBLISH))
        driver.execute_script("arguments[0].scrollIntoView();", publish_button)
        publish_button.click()

        wait.until(EC.url_to_be(MAIN_PAGE_URL))

        wait.until(EC.element_to_be_clickable(MainAuthPageLocators.BUTTON_AVATAR)).click()
        wait.until(EC.url_to_be(PROFILE_URL))

        my_posts_block = wait.until(EC.visibility_of_element_located(ProfilePageLocators.MY_POSTS_BLOCK))
        driver.execute_script("arguments[0].scrollIntoView();", my_posts_block)

        assert wait.until(EC.visibility_of_element_located(ProfilePageLocators.product_title(product["name"])))








