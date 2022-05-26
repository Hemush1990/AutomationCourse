import time

from selenium.webdriver.common.by import By
from LetsKodeIt.lib import helpers
from LetsKodeIt.lib.test_logger import logger
from LetsKodeIt.testdata import test_data

sign_up_btn = (By.XPATH, "//a[@href = '/register']")
email_field = (By.XPATH, "//input[@placeholder = 'Email Address']")
password_field = (By.XPATH, "//input[@placeholder = 'Password']")
login_btn = (By.XPATH, "//*[@type = 'submit']")


def sign_up():
    helpers.find_and_click(sign_up_btn)


def sign_in():
    helpers.find_and_send_keys(email_field, test_data.email)
    helpers.find_and_send_keys(password_field, test_data.password)
    time.sleep(3)
    helpers.find_and_click(login_btn)
    logger(f"Sign in is success for the user {test_data.email}")


