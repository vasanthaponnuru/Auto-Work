from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class ec_amazon:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def search_product(self, product_name):
        self.driver.get("https://www.amazon.in")
        try:
            search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")  
            if search_bar:
                print("Search bar found!")
                search_bar.send_keys(product_name)
            else:
                print("Search bar not found.")
        except Exception as e:
            print(f"Exception occurred while locating search bar: {e}")
        
        time.sleep(3)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(3)

    def add_item_to_cart(self):

        #find Element
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "SKDBPM Ice Juice Drinks Glass Can Mug with Straw")
       #scroll container till element visible
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        element.click()

        add_to_cart = self.driver.find_element(By.ID, "add-to-cart-button")
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_to_cart)
        add_to_cart.click()
   
    def checkout_procidure(self):
        cart = self.driver.find_element(By.ID, "nav-cart")
        cart.click()

    def teardown(self):
        print("Closing browser...")
        self.driver.quit()

if __name__ == "__main__":
    test = ec_amazon()
    test.search_product("tumbler with straw")
    test.add_item_to_cart()
    test.checkout_procidure()
    test.teardown()


