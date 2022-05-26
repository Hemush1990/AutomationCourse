import time

from selenium.webdriver.common.by import By
from LetsKodeIt.lib import helpers
from LetsKodeIt.lib.test_logger import logger
from LetsKodeIt.testdata import test_data

signUp_btn = (By.XPATH, "//input[@value= 'Sign Up']")

list_loc = ["First Name", "Last Name", "Email Address", "Password", "Confirm Password"]


def get_locator(loc):
    locator = f"//input[@placeholder= '{loc}']"
    return locator


def fill_form():
    for loc, val in zip(list_loc, test_data.user_data):
        helpers.find_by_xpath_and_send_keys(get_locator(loc), val)
    helpers.find_and_click(signUp_btn)
    logger("Sign up is success")


def reg_user():
    helpers.find_and_click(signUp_btn)
