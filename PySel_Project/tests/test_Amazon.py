import pytest
#from Ec_Amazon.Ec_amazon import ec_amazon
from Ec_Amazon.test_1 import EcAmazon
from Ec_Amazon.test_2 import SelectMore
from Ec_Amazon.test_3 import select_tshirt
   
@pytest.fixture(scope="session")
def test_1(driver):
    return EcAmazon(driver)

@pytest.fixture(scope="session")
def test_2(driver):
    return SelectMore(driver)

@pytest.fixture(scope="session")
def test_3(driver):
    return select_tshirt(driver)

def test_case_1(test_1):
    test_1.search_product("https://www.amazon.in","tumbler with straw")
    test_1.add_item_to_cart()

def test_case_2(test_2):
    test_2.nav_back(" SKDBPM Ice Juice Drinks Glass Can Mug with Straw")
    test_2.hover_select_addcart("SCHON MUG")
    test_2.nav_back_home()

def test_case_3(test_3):
    test_3.search_product("Tshirt for women")
    test_3.select_size()
    test_3.checkout_procedure()