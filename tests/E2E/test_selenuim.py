import time
import warnings
from threading import Thread
import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as firefoxService

@pytest.fixture()
def driver():
    firefox_driver_binary = "./geckodriver.exe"
    ser_firefox = firefoxService(firefox_driver_binary)

    browser_name='firefox'
    if browser_name == "firefox-webdriver":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":
        dc = {
            "browserName": "firefox",
            "platformName": "Windows 11"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)

    elif browser_name == "MicrosoftEdge":
        dc = {
            "browserName": "MicrosoftEdge",
            "platformName": "Windows 11"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)

    elif browser_name == "chrome":
        dc = {
            "browserName": "chrome",
            "platformName": "Windows 11"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)
    elif browser_name == "firefox-mobile":
        firefox_options = FireFoxOptions()
        firefox_options.add_argument("--width=375")
        firefox_options.add_argument("--height=812")
        firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 "
                                                                     "(iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like "
                                                                     "Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
        # firefox_options.set_preference("general.useragent.override", "Nexus 7")

        driver = webdriver.Firefox(service=ser_firefox, options=firefox_options)
    else:
        raise Exception("driver doesn't exists")
    yield driver
    driver.close()


def test_registration(driver):
    driver.get("http://localhost:8000/")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,'#navbarScroll > div > a:nth-child(2)').click() #login link
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > div > div > a").click() #register
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("nancy") #name
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("nana1976543@hotmail.com") #email
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("bbbbggggg")
    driver.find_element(By.CSS_SELECTOR, "#passwordConfirm").send_keys("bbbbggggg")
    element = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)
    user_name=driver.find_element(By.CSS_SELECTOR,"#username").text
    time.sleep(5)
    assert "NANCY"==user_name

def test_success_login(driver):
    driver.get("http://localhost:8000/")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#navbarScroll > div > a:nth-child(2)").click() #login link
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("toti_loti@hotmail.com")  # email
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("totiloti")
    element = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    user_name = driver.find_element(By.CSS_SELECTOR, "#username").text
    time.sleep(5)
    assert "TOTI" == user_name


def test_buy_product(driver):
    driver.get("http://127.0.0.1:8000/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#navbarScroll > div > a:nth-child(2)").click() # login link
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("toti_loti@hotmail.com")  # email
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("totiloti")
    element = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,".w-100").click() # add to cart
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".w-100").click() # procced to checkout
    driver.find_element(By.CSS_SELECTOR, "#address").send_keys("Hertzel")
    driver.find_element(By.CSS_SELECTOR, "#city").send_keys("akko")
    driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys("2420706")
    driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Israel")
    shipping_ele = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button")
    driver.execute_script("arguments[0].click();", shipping_ele) #continue
    payment_ele = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button")
    driver.execute_script("arguments[0].click();", payment_ele)
    driver.find_element(By.CSS_SELECTOR,
                        "#root > div > main > div > div.row > div.col-md-4 > div > div > div:nth-child(7) > button").click()

