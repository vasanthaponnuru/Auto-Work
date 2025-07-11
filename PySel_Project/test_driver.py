from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_case_1():
    print("Launching browser...")
    #driver = webdriver.Chrome(service=Service("F:\\WebDrivers\\chromedriver.exe"))
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print("Page loaded:", driver.title)

    time.sleep(5)  # Keep browser open for observation
    driver.quit()

test_case_1()