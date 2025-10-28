from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#    pip install webdriver-manager
from selenium.webdriver.chrome.service import Service
import time

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    options= Options()
    options.add_argument('--start-maximized')



    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    time.sleep(5)

    return driver

def login_saucedemo(driver) :
    driver.get(URL)

    driver.find_element(By.NAME,'user-name').send_keys(USERNAME)
    driver.find_element(By.NAME,'password').send_keys(PASSWORD)
    driver.find_element(By.ID,'login-button').click()

    time.sleep(7)
