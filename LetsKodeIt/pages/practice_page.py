from selenium.webdriver.common.by import By
from LetsKodeIt.lib import helpers

signin_button = (By.XPATH, "//a[@href = '/login']")


def open_sign_in():
    helpers.find_and_click(signin_button)
