import pytest
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

class SelectMore:

    def __init__(self, driver):
        self.driver = driver
         # Locators
        self.home_logo =(By.ID,"nav-logo-sprites")
        self.list_container = (By.CSS_SELECTOR, "#tp-inline-twister-dim-values-container > ul")
        self.options = (By.XPATH, "//*[@id='tp-inline-twister-dim-values-container']/ul/li" )
        self.add_cart = (By.ID, "add-to-cart-button")

    def nav_back(self, expected_keyword):

        max_attempts = 2  # just in case to avoid infinite loop
        attempts = 0

        while attempts < max_attempts:
            current_title = self.driver.title
            print(f"⬅️ Back attempt {attempts+1}, current_title{current_title}")

            if expected_keyword.lower() in current_title.lower():
                print(f"🏠 Reached target page")
                return

            self.driver.back()
            time.sleep(10)
            attempts += 1

            # Optional wait for page to settle
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

        print("⚠️ Target page not found within back attempts.")

    def hover_select_addcart(self,expected_name):

        list_container = self.driver.find_element(*self.list_container)
        self.driver.implicitly_wait(10)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", list_container)
        options = self.driver.find_elements(*self.options)
        self.driver.implicitly_wait(10)

        for option in options:
            ActionChains(self.driver).move_to_element(option).perform()
            time.sleep(10)

            tooltip_text = option.get_attribute("title") or option.get_attribute("aria-label") or option.text

            if expected_name.lower() in tooltip_text.lower():
                print(f"✅ Found : {tooltip_text}")
                option.click()
                break
        print("selected specific item")
        
        try:
            add_cart = self.driver.find_element(*self.add_cart)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_cart)
            self.driver.execute_script("arguments[0].click();", add_cart)
            print("added one more to 🛒")
        except Exception as e:
            print(f"Error adding item to cart: {e}")
            
    def nav_back_home(self):
        home_logo = self.driver.find_element(*self.home_logo)
        home_logo.click()
        print("back to home page")
    

