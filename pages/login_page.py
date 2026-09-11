from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.submit_button = (By.ID, 'submit')
        self.success_h1 = (By.TAG_NAME, 'h1')
        self.error_message_label = (By.ID, 'error')
    #defining all the actions users do.
    def open_login_page(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
    def enter_username(self,username):
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)
    def enter_password(self,password):
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)
    def click_submit(self):
        self.wait.until(EC.presence_of_element_located(self.submit_button)).click()
    def get_error_message(self):
        element =self.wait.until(EC.visibility_of_element_located(self.error_message_label))
        return element.text
    def get_success_message(self):
        return self.wait.until(EC.presence_of_element_located(self.success_h1)).text.lower()





