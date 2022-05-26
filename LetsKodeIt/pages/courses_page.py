from selenium.webdriver.common.by import By
from LetsKodeIt.lib import helpers
from LetsKodeIt.lib.test_logger import logger
from LetsKodeIt.testdata import test_data

dropdown = (By.ID, "dropdownMenu1")
logout_btn = (By.XPATH, "//*[@href = '/logout']")
heading_my_courses = (By.XPATH, "//h1[normalize-space()='My Courses']")
all_courses_btn = (By.XPATH, "//a[normalize-space()='ALL COURSES']")
search_fld = (By.XPATH, "//input[@name='course']")
search_btn = (By.XPATH, "//button[@type='submit']")
search_result = (By.XPATH, "//div[@id='course-list']//div[@class = 'col-lg-4 col-md-4 col-sm-6 col-xs-12']")


def logout_account():
    helpers.find_and_click(dropdown)
    helpers.find_and_click(logout_btn)
    logger("Logging out from the account")


def is_signin_success():
    heading = helpers.find(heading_my_courses, get_text=True)
    assert str(heading) == "My Courses", "User do not sign in"


def all_courses_selected():
    helpers.find_and_click(all_courses_btn)


def search_courses():
    helpers.find_and_send_keys(search_fld, test_data.search_word)
    helpers.find_and_click(search_btn)
    logger(f"Searching the word {test_data.search_word}")


def result():
    results = helpers.find_elemetns(search_result, get_text=True)
    logger(f"The amount of results is {len(results)}")


def get_result():
    pass
