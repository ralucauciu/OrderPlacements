from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME_INPUT = (By.NAME, "login[username]")
    PASSWORD_INPUT = (By.ID, "pass")
    SIGN_IN_BUTTON = (By.ID, "send2")
    USER_LOGGED_NAME = (By.CSS_SELECTOR, "li.greet.welcome span.logged-in")

    # Actions
    def set_username(self, username):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        username_input.clear()
        username_input.send_keys(username)

    def set_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_sign_in_button(self):
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        )
        sign_in_button.click()

    def get_user_logged_in(self):
        user_logged_name = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.USER_LOGGED_NAME)
        )
        return user_logged_name.text