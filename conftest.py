import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-desk.education-services.ru")
    yield driver
    driver.quit()

@pytest.fixture
def new_user_data():
    import uuid
    unique = uuid.uuid4().hex[:8]
    return {"email": f"user_{unique}@yandex.ru", "password": "Qwerty123"}

@pytest.fixture
def wait_5(driver):
    return WebDriverWait(driver, 5)

