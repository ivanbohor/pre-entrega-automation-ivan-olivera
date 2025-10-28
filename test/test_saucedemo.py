import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


from utils.helpers import login_saucedemo, get_driver




@pytest.fixture

def driver():
    #confg para consultar a selenium
    driver= get_driver()
    yield driver 
    driver.quit()


def test_login(driver):
    #logueo usuario,click login,redireccion a inventario
    login_saucedemo(driver)
    assert '/inventory.html' in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text    
    assert titulo=='Products'


def test_catalogo(driver): 
    login_saucedemo(driver)
    products= driver.find_elements(By.CLASS_NAME,'inventory_list')
    assert len(products) > 0

def test_carrito(driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    total_productos = len(products) 

    if total_productos >= 2:
        products[0].find_element(By.TAG_NAME, 'button').click()
        products[1].find_element(By.TAG_NAME, 'button').click()

        badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert badge == "2"

