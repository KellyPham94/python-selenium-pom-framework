import pytest
from pages.login_page import LoginPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("username,password,expected_status", [("student","Password123", "success"),("incorrectUser", "Password123", "fail"),("student", "incorrectPassword", "fail")])
def test_login_multiple_accounts(driver, username, password, expected_status ):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_submit()
    if expected_status == "success":
        assert "logged-in-successfully" in driver.current_url.lower()
    else:
        error_msg = login_page.get_error_message()
        assert error_msg != ""
def test_login_xss_payload(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    xss_payload = "<script>alert('XSS')</script>"
    login_page.enter_username(xss_payload)
    login_page.enter_password("Password123")
    login_page.click_submit()
    try:
        login_page.wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert False ,f"XSS ERROR: {alert_text}"
    except TimeoutException:
        print("/n Web is safe")

def test_login_sqli_payload(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username(" ' OR '1' = '1")
    login_page.enter_password("any_password")
    login_page.click_submit()
    assert "logged-in-successfully" not in driver.current_url.lower()
    print("\n The web is safe with basic SQL Injection")

