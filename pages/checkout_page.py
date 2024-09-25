from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    CHECKOUT_PAGE_HEADER = (By.CLASS_NAME, "opc-progress-bar")
    SHIPPING_ADDRESS_SECTION = (By.CLASS_NAME, "checkout-shipping-address")
    SHIPPING_ADDRESS_SELECTED = (By.CSS_SELECTOR, "div.shipping-address-item.selected-item")
    EMAIL_INPUT = (By.ID, "customer-email")
    FIRST_NAME_INPUT = (By.NAME, "firstname")
    LAST_NAME_INPUT = (By.NAME, "lastname")
    ADDRESS_INPUT = (By.NAME, "street[0]")
    CITY_INPUT = (By.NAME, "city")
    REGION_DROPDOWN = (By.NAME, "region_id")
    POSTAL_CODE_INPUT = (By.NAME, "postcode")
    COUNTRY_DROPDOWN = (By.NAME, "country_id")
    PHONE_NUMBER_INPUT = (By.NAME, "telephone")
    SHIPPING_METHOD_SECTION = (By.CLASS_NAME, "checkout-shipping-method")
    SHIPPING_METHOD_BUTTON = (By.XPATH, "//table[@class='table-checkout-shipping-method']/tbody/tr[1]/td[1]")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".button.button.action.continue.primary")
    PAYMENT_METHOD_SECTION = (By.CLASS_NAME, "payment-group")
    CHECKBOX_ADDRESS_BUTTON = (By.ID, "billing-address-same-as-shipping-checkmo")
    PLACE_ORDER_BUTTON = (By.XPATH, "//div[@class='actions-toolbar']/div[@class='primary']/button[@class='action primary checkout']")


    # Actions
    def get_checkout_page_header(self):
        checkout_page_header = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.CHECKOUT_PAGE_HEADER)
        )
        return checkout_page_header.text

    def get_shipping_address_section(self):
        shipping_address_section = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.SHIPPING_ADDRESS_SECTION)
        )
        return shipping_address_section

    def get_shipping_address_selected(self):
        shipping_address_selected = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.SHIPPING_ADDRESS_SELECTED)
        )
        return shipping_address_selected

    def set_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)

    def set_first_name(self, first_name):
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def set_last_name(self,last_name):
        last_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LAST_NAME_INPUT)
        )
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def set_address(self,address):
        address_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ADDRESS_INPUT)
        )
        address_input.clear()
        address_input.send_keys(address)

    def set_city(self,city):
        city_input = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.CITY_INPUT)
        )
        city_input.clear()
        city_input.send_keys(city)

    def set_region(self,region):
        region_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REGION_DROPDOWN)
        )
        region_dropdown.click()
        region_dropdown.send_keys(region)

    def set_postal_code(self,postal_code):
        postal_code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.POSTAL_CODE_INPUT)
        )
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)

    def set_country(self,country):
        country_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COUNTRY_DROPDOWN)
        )
        country_dropdown.click()
        country_dropdown.send_keys(country)

    def set_phone_number(self,phone_number):
        phone_number_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PHONE_NUMBER_INPUT)
        )
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)

    def get_shipping_method_section(self):
        shipping_method_section = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.SHIPPING_METHOD_SECTION)
        )
        return shipping_method_section

    def select_shipping_method(self):
        shipping_method_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SHIPPING_METHOD_BUTTON)
        )
        shipping_method_button.click()

    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        )
        next_button.click()

    def get_payment_method_section(self):
        payment_method_section = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.PAYMENT_METHOD_SECTION)
        )
        return payment_method_section

    def click_checkbox_address(self):
        checkbox_address_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKBOX_ADDRESS_BUTTON)
        )
        checkbox_address_button.click()

    def click_place_order_button(self):
        place_order_button = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.PLACE_ORDER_BUTTON)
        )
        place_order_button.click()
