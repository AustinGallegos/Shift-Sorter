import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import file_handler as fh


def setup_driver():
    """Set up and return Selenium WebDriver and wait object."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, sys.maxsize)
    return driver, wait


def get_shift(codes, shift_code):
    """Return the shift name corresponding to a given PT code."""
    if shift_code in codes["MOR"]:
        return "MOR"
    elif shift_code in codes["DAY"]:
        return "DAY"
    elif shift_code in codes["TWI"]:
        return "TWI"
    elif shift_code in codes["NIT"]:
        return "NIT"
    else:
        return "ACCOM"


def process_login(codes, driver, login):
    """Search for an AA by login and assign them to the appropriate shift file."""
    search_bar = driver.find_element(By.ID, "navEmployeeSearch")
    search_bar.send_keys(login)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)

    name_text = driver.find_element(By.ID, "userLogin").text
    name_list = name_text.split("(")
    name = name_list.pop()
    name = name.strip(")")

    login = login.strip()
    if name == login:
        shift_code = driver.find_element(By.ID, "ptCode").text
        shift = get_shift(codes, shift_code)
        fh.assign_aa_to_shift(login, shift)
    else:
        for _ in range(15):
            search_bar.send_keys(Keys.BACKSPACE)
