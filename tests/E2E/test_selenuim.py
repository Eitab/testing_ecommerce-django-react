import time
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


from selenium.webdriver.firefox import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture()
def driver():
    firefox_driver_binary = "./geckodriver.exe"
    ser_firefox = firefoxService(firefox_driver_binary)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    yield driver
    driver.close()

def test_success_login(driver):
    driver.get("http://localhost:8000/")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,'#navbarScroll > div > a:nth-child(2)').click() #login link
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > div > div > a").click() #register
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("nancy") #name
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("nana987@hotmail.com") #email
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("bbbbggggg")
    driver.find_element(By.CSS_SELECTOR, "#passwordConfirm").send_keys("bbbbggggg")
    element = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button")
    driver.execute_script("arguments[0].click();", element)



    # driver.find_element(By.CSS_SELECTOR,"#email").send_keys("toti_loti@hotmail.com")
    # driver.find_element(By.CSS_SELECTOR, "#password").send_keys("totiloti")
    # driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > form > button").click()
    # time.sleep(3)
