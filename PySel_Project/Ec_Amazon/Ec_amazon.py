import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ec_amazon:

    def __init__(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())


        self.driver = webdriver.Chrome(service=service, options=options)


    def search_product(self, product_name):
        self.driver.get("https://www.amazon.in")
        time.sleep(5)
        try:
            search_bar = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )  
            if search_bar:
                print("Search bar found!")
                search_bar.send_keys(product_name)
                search_bar.send_keys(Keys.RETURN)
            else:
                print("Search bar not found.")
        except Exception as e:
            print(f"Exception occurred while locating search bar: {e}")
        
            
        time.sleep(3)

    def add_item_to_cart(self):

        #wait for specific element to load 
        print("looking for element")
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "SKDBPM Ice Juice Drinks Glass Can Mug with Straw"))
            )

        #scroll container till element visible
        print("element found")
        self.driver.save_screenshot("screenshot.png")
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        element.click()
        print("selected product")

        add_to_cart = self.driver.find_element(By.ID, "add-to-cart-button")
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_to_cart)
        add_to_cart.click()
        print("product added to cart")
   
    def checkout_procidure(self):
        cart = self.driver.find_element(By.ID, "nav-cart")
        cart.click()
        print("checked  cart")

    def teardown(self):
        print("Closing browser...")
        self.driver.quit()

if __name__ == "__main__":
    test = ec_amazon()
    test.search_product("tumbler with straw")
    test.add_item_to_cart()
    test.checkout_procidure()
    test.teardown()


