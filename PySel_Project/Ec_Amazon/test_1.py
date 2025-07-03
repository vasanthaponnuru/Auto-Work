from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class EcAmazon:
    def __init__(self, driver):
       self.driver = driver
       # Locators
       self.search_box = (By.ID, "twotabsearchtextbox")
       #self.search_button = (By.ID, "nav-search-submit-button")
       self.target_product = (By.PARTIAL_LINK_TEXT, "SKDBPM Ice Juice Drinks Glass Can Mug with Straw")
       self.add_to_cart_btn = (By.ID, "add-to-cart-button")
       self.cart_icon = (By.ID, "nav-cart")

        

    def search_product(self, url, product_name):
        self.driver.get(url)
        try:
            search_bar = self.driver.find_element(*self.search_box)
            print("Search bar found!")
            search_bar.send_keys(product_name)
            search_bar.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Error locating search bar: {e}")

        time.sleep(3)  # Only if needed, prefer WebDriverWait in production

    def add_item_to_cart(self):
        try:
            target_product = self.driver.find_element(*self.target_product)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", target_product)
            target_product.click()

            add_to_cart = self.driver.find_element(*self.add_to_cart_btn)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_to_cart)
            add_to_cart.click()
        except Exception as e:
            print(f"Error adding item to cart: {e}")

    def checkout_procedure(self):
        try:
            cart = self.driver.find_element(*self.cart_icon)
            cart.click()
        except Exception as e:
            print(f"Checkout navigation failed: {e}")

    def teardown(self):
        print("Closing browser...")
        self.driver.quit()