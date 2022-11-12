import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import random


class TestClass:
    # Take username and password input for Test Case 1.
    username = input("Insert Username: ")
    password = input("Insert Password: ")

    def test_case_1(self):
        # Check's parent directory for chrome web-driver and load it from there.
        driver_path = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
        s = Service(chromedriver_path)
        driver = webdriver.Chrome(service=s)

        # Load targeted website
        driver.get("https://www.saucedemo.com/")

        # Take username and password from parent class variables.
        username = TestClass.username
        password = TestClass.password

        # Find username text-field element on website and insert username from above variable.
        username_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'user-name')))
        username_field.send_keys(username)

        # Find password text-field element on website and insert username from above variable.
        password_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'password')))
        password_field.send_keys(password)

        # Find login button element on website and click on it.
        login_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'login-button')))
        login_btn.click()

        # Find all add to cart buttons elements
        add_to_cart_btn = WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.inventory_item button')))

        # Count total number of add to cart elements found on website.
        total_add_cart_btns = len(add_to_cart_btn)

        # Click 3 items randomly based on total number of add to cart buttons found.
        for i in range(3):
            item_range = random.randint(0, total_add_cart_btns)
            add_to_cart_btn[item_range].click()

    def test_case_2(self):
        # Check's parent directory for chrome web-driver and load it from there.
        driver_path = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
        s = Service(chromedriver_path)
        driver = webdriver.Chrome(service=s)

        # Load targeted website
        driver.get("https://www.saucedemo.com/")

        # Take pre-defined username and password for this test case.
        username = "locked_out_user"
        password = "secret_sauce"

        # Find username text-field element on website and insert username from above variable.
        username_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'user-name')))
        username_field.send_keys(username)

        # Find password text-field element on website and insert username from above variable.
        password_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'password')))
        password_field.send_keys(password)

        # Find login button element on website and click on it.
        login_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'login-button')))
        login_btn.click()

        # Check if error message appeared for locked out user and click to close it.
        error_msg = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME, 'error-button')))
        error_msg.click()

    def test_case_3(self):
        # Check's parent directory for chrome web-driver and load it from there.
        driver_path = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
        s = Service(chromedriver_path)
        driver = webdriver.Chrome(service=s)

        # Load targeted website
        driver.get("https://www.saucedemo.com/")

        # Take pre-defined username and password for this test case.
        username = "problem_user"
        password = "secret_sauce"

        # Find username text-field element on website and insert username from above variable.
        username_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'user-name')))
        username_field.send_keys(username)

        # Find password text-field element on website and insert username from above variable.
        password_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'password')))
        password_field.send_keys(password)

        # Find login button element on website and click on it.
        login_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'login-button')))
        login_btn.click()

        # Find all add to cart buttons elements
        add_to_cart_btn = WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.inventory_item button')))

        # Count total number of add to cart elements found on website.
        total_add_cart_btns = len(add_to_cart_btn)

        # Click 3 items randomly based on total number of add to cart buttons found.
        for i in range(3):
            item_range = random.randint(0, total_add_cart_btns)
            add_to_cart_btn[item_range].click()

    def test_case_4(self):
        # Check's parent directory for chrome web-driver and load it from there.
        driver_path = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
        s = Service(chromedriver_path)
        driver = webdriver.Chrome(service=s)

        # Load targeted website
        driver.get("https://www.saucedemo.com/")

        # Take pre-defined username and password for this test case.
        username = "performance_glitch_user"
        password = "secret_sauce"

        # Find username text-field element on website and insert username from above variable.
        username_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'user-name')))
        username_field.send_keys(username)

        # Find password text-field element on website and insert username from above variable.
        password_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'password')))
        password_field.send_keys(password)

        # Find login button element on website and click on it.
        login_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'login-button')))
        login_btn.click()

        # Find all add to cart buttons elements
        add_to_cart_btn = WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.inventory_item button')))

        # Count total number of add to cart elements found on website.
        total_add_cart_btns = len(add_to_cart_btn)

        # Click 3 items randomly based on total number of add to cart buttons found.
        for i in range(3):
            item_range = random.randint(0, total_add_cart_btns)
            add_to_cart_btn[item_range].click()
