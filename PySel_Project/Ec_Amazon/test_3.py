import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class select_tshirt:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.tshirt = (By.PARTIAL_LINK_TEXT, "Round Neck Drop Shoulder Round Neck Black & White Graphic Printed Pure Cotton Oversized Baggy Fit Half Sleeve T-Shirt for Women & Girls (Sizes: S to 2XL)")
        self.next = (By.XPATH, "//a[contains(@aria-label, 'Go to next page')]")
        self.tshirt_size = (By.ID,"size_name_3")
        self.add_to_cart = (By.ID, "add-to-cart-button")
        self.cart = (By.ID, "nav-cart")
        self.bill = (By.ID,"sc-subtotal-amount-buybox")
        self.proceedto_checkout = (By.NAME,"proceedToRetailCheckout")

    def search_product(self,product_name):
        
        try:
            search_bar =self.driver.find_element(*self.search_box)
            if search_bar:
                print("Search bar found!")
                search_bar.send_keys(product_name)
                search_bar.send_keys(Keys.RETURN)
            else:
                print("Search bar not found.")
                        
        except Exception as e:
            print(f"Exception occurred while locating search bar: {e}")
        
            
        time.sleep(3)

        print("looking for 👕")

        max_pages = 10  # safety limit to avoid infinite loop
        pages_tried = 0

        while pages_tried < max_pages:

            try:
                element = self.driver.find_element(*self.tshirt)
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                print("👕 found")
                element.click()
                break  # ✅ Exit loop on success


            except :
                print(f"🔍 Product not found on page {pages_tried+1}")
                try:  # Click on "Next Page"
                    next_btn = self.driver.find_element(*self.next)
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_btn)
                    next_btn.click()
                    pages_tried += 1
                    print(f"➡️ Moved to page {pages_tried+1}")
                except:
                    print("❌ No more pages available. Product not found.")
                    break

        time.sleep(3)
    def select_size(self):
        size = self.driver.find_element(*self.tshirt_size)
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", size)
        size.click()
        print("selected xl size") 
        time.sleep(10)
        add_cart = self.driver.find_element(*self.add_to_cart)
        print("searching for button") 
        
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_cart)
        print("located button") 
        time.sleep(10)
        self.driver.execute_script("arguments[0].click();", add_cart)
        print("added 👕 to 🛒")

        time.sleep(5)
    def checkout_procedure(self):
        try:
            cart = self.driver.find_element(*self.cart)
            cart.click()
        except Exception as e:
            print(f"Checkout navigation failed: {e}")

        print("checked ✅ cart")
        total_amount = self.driver.find_element(*self.bill)
        time.sleep(10)
        total_bill = total_amount.text
        print("🧾 Subtotal = ",total_bill)
        proceed_to_checkout = self.driver.find_element(*self.proceedto_checkout)
        proceed_to_checkout.click()
        time.sleep(5)
        self.driver.save_screenshot("screenshot.png")