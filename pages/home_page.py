from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "li.authorization-link a")
    WOMEN_MENU = (By.LINK_TEXT, "Women")
    TOPS_MENU = (By.LINK_TEXT, "Tops")
    FIRST_ITEM = (By.CSS_SELECTOR, ".products-grid .item:first-child .product-item-link")
    ITEM_TITLE = (By.CLASS_NAME, "page-title")
    SIZE_S = (By.XPATH, "//div[@option-label='S']")
    ITEM_COLOR_YELLOW = (By.XPATH, "//div[@option-label='Yellow']")
    QUANTITY_INPUT = (By.XPATH, "//input[@title='Qty']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@title='Add to Cart']")
    CONFIRMATION_MESSAGE = (By.XPATH, "//div[contains(@data-bind, 'message.text')]")
    ITEM_PRICE = (By.ID, "product-price-1812")
    QUANTITY_CART = (By.CLASS_NAME, "counter-number")
    CART_ICON = (By.CSS_SELECTOR, ".action.showcart")
    SUBTOTAL_PRICE = (By.XPATH, "//span[@class='price-wrapper']/span[@class='price']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.ID, "top-cart-btn-checkout")

    #Actions
    def click_sign_in_button(self):
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        )
        sign_in_button.click()

    def select_women_menu(self):
        women_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.WOMEN_MENU)
        )
        women_menu.click()

    def select_tops_menu(self):
        tops_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TOPS_MENU)
        )
        tops_menu.click()

    def click_first_item(self):
        first_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_ITEM)
        )
        first_item.click()

    def get_item_title(self):
        item_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ITEM_TITLE)
        )
        return item_title.text

    def select_size_s(self):
        size_s = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIZE_S)
        )
        size_s.click()

    def select_color_yellow(self):
        item_color_yellow = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ITEM_COLOR_YELLOW)
        )
        item_color_yellow.click()

    def set_quantity(self, quantity):
        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.QUANTITY_INPUT)
        )
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def click_add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_to_cart_button.click()

    def get_confirmation_message(self):
        confirmation_message = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.CONFIRMATION_MESSAGE)
        )
        return confirmation_message.text

    def get_item_price(self):
        item_price_with_sign = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ITEM_PRICE)
        )
        item_price = float(item_price_with_sign.text.replace("$", ""))
        return item_price

    def get_quantity_from_cart_icon(self):
        quantity_from_cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.QUANTITY_CART)
        )
        quantity_text = quantity_from_cart.text
        return quantity_text

    def click_on_cart_icon(self):
        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart_icon.click()

    def get_subtotal_price(self):
        subtotal_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUBTOTAL_PRICE)
        )
        subtotal_price = float(subtotal_price_element.text.replace("$", ""))
        return subtotal_price

    def click_on_proceed_to_checkout(self):
        proceed_to_checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PROCEED_TO_CHECKOUT_BUTTON)
        )
        proceed_to_checkout_button.click()
