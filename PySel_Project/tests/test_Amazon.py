import pytest
from Ec_Amazon.Ec_amazon import ec_amazon
from Ec_Amazon.test_1 import EcAmazon

@pytest.mark
def test_search_add_to_cart(driver):
    amazon = EcAmazon(driver)
    amazon.search_product("https://www.amazon.in","tumbler with straw")
    amazon.add_item_to_cart()
    amazon.checkout_procedure()
    amazon.teardown()
