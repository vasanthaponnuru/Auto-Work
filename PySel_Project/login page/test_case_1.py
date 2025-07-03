from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import test_case_1_inputs
def test_case_1():
    
    print("Launching browser...")
    #driver = webdriver.Chrome(service=Service("F:/LANGUAGES/selenium_python/Drivers/chromedriver.exe"))
    driver = webdriver.Chrome()
   
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    print("Waiting before interaction...")
    time.sleep(5)
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    username = driver.find_element(By.NAME, "username")
    username.send_keys(test_case_1_inputs.username)
    time.sleep(5)

    password = driver.find_element(By.NAME, "password")
    password.send_keys("admin123")

    login = driver.find_element(By.CSS_SELECTOR, "button")
    login.click()

    print("Login attempted. Waiting before closing...")
    time.sleep(5)
    driver.quit()

test_case_1()