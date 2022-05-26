

from LetsKodeIt.lib import helpers
from LetsKodeIt.testdata import test_data
from LetsKodeIt.pages import courses_page, practice_page, sign_in_page, sign_up_paage, home_page


def test():
    try:
        helpers.go_to_page(test_data.URL)
        practice_page.open_sign_in()
        sign_in_page.sign_up()
        sign_up_paage.fill_form()
        courses_page.logout_account()
        home_page.sign_in_home()
        sign_in_page.sign_in()
        courses_page.is_signin_success()
        courses_page.all_courses_selected()
        courses_page.search_courses()
        courses_page.result()
    finally:
        helpers.driver.quit()


if __name__ == '__main__':
    test()