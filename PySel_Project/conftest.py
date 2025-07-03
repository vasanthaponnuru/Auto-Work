import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    #options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
