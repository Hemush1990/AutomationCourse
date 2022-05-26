from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LetsKodeIt.lib.driver import get_driver
import time
import random
import string


driver = get_driver()


def random_char_to_email():
    rand = ''.join(random.choice(string.ascii_letters) for x in range(2))
    return 'test'+rand+'@mail.com'


def go_to_page(url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()


def find_and_click(loc, timeout=10):
    elem = find(loc, timeout)
    elem.click()


def find_and_send_keys(loc, inp_text, timeout=10):
    elem = find(loc, timeout)
    elem.send_keys(inp_text)


def find(loc, timeout=10, get_text="", get_attribute=""):
    elem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(loc))
    if get_text:
        return elem.text
    elif get_attribute:
        return elem.get_attribute(get_attribute)
    return elem


def find_elemetns(loc, timeout=10, get_text=False, get_attribute=False):
    els = driver.find_elements(*loc)
    if not els:
        # If elements not found - wait and search again
        time.sleep(1)
        els = driver.find_elements(*loc)
    if get_text:
        all_text = [i.text for i in els if i.is_displayed()]
        return all_text
    elif get_attribute:
        all_attr = [i.get_attribute(get_attribute) for i in els]
        return all_attr
    return els


def switch_window(window_id=0):
    driver.switch_to.window(driver.window_handles[window_id])


def switch_to_alert():
    return driver.switch_to.alert


def find_by_xpath_and_send_keys(loc, inp_text):
    elem = driver.find_element_by_xpath(loc)
    elem.send_keys(inp_text)
