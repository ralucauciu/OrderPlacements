from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    ORDER_CONFIRMATION_TITLE = (By.XPATH, "//div[@class='page-title-wrapper']/h1[@class='page-title']/span[@class='base']")
    ORDER_NUMBER = (By.XPATH, "//div[@class='checkout-success']/p")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "div.actions-toolbar div.primary a.action.primary.continue")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "div a.action.primary")

    # Actions
    def get_order_confirmation_title(self):
        order_confirmation_title = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.ORDER_CONFIRMATION_TITLE)
        )
        return order_confirmation_title.text

    def get_order_number(self):
        order_number = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.ORDER_NUMBER)
        )
        return order_number.text

    def get_continue_shopping_button(self):
        continue_shopping_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
        )
        return continue_shopping_button

    def get_create_account_button(self):
        create_account_button = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.CREATE_ACCOUNT_BUTTON)
        )
        return create_account_button
