from selenium.webdriver.common.by import By
from LetsKodeIt.lib import helpers
from LetsKodeIt.lib.test_logger import logger


sign_in = (By.XPATH, "//a[normalize-space()='Sign In']")


def sign_in_home():
    helpers.find_and_click(sign_in)
    logger("Signed in to the account")

