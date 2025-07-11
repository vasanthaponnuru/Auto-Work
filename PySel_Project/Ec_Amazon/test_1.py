import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EcAmazon:

    def __init__(self, driver):
       self.driver = driver
       # Locators
       self.continue_shopping = (By.CLASS_NAME, "a-button-text")
       self.search_box = (By.ID, "twotabsearchtextbox")
       self.target_product = (By.PARTIAL_LINK_TEXT, "SKDBPM Ice Juice Drinks Glass Can Mug with Straw")
       self.add_to_cart_btn = (By.ID, "add-to-cart-button")
       self.cart_icon = (By.ID, "nav-cart")    

    def search_product(self, url, product_name):
        self.driver.get(url)
        
        WebDriverWait(self.driver, 10).until(EC.title_contains("Amazon.in"))

        try:
            continue_buttons = self.driver.find_elements(*self.continue_shopping)
            for btn in continue_buttons:
                alt = btn.get_attribute("alt")
                if alt and "continue shopping" in alt.lower():
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", btn)
                    self.driver.execute_script("arguments[0].click();", btn)
                    print("🛒 Clicked fallback 'Continue Shopping' button")
                    time.sleep(5)  # Let full UI load
                    break
                else:
                    print("⚠️ No matching button found in fallback container")
        except Exception as e:
            print(f"❌ Exception during fallback detection: {e}")
        
        time.sleep(15)  # Let UI stabilize before locating elements
        
        try:
            search_bar = self.driver.find_element(*self.search_box)
            print("Search bar found!")
            time.sleep(15)
            search_bar.send_keys(product_name)
            time.sleep(5)
            search_bar.send_keys(Keys.RETURN)
            time.sleep(15)
        except Exception as e:
            print(f"Error locating search bar: {e}")

        #time.sleep(13)  # Only if needed, prefer WebDriverWait in production

    def add_item_to_cart(self):
        try:
            target_product = self.driver.find_element(*self.target_product)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", target_product)
            target_product.click()
            print("target found")

            add_to_cart = self.driver.find_element(*self.add_to_cart_btn)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_to_cart)
            add_to_cart.click()
            print("product added to cart")

        except Exception as e:
            print(f"Error adding item to cart: {e}")

           
           
        time.sleep(10)
