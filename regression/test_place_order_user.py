import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.order_confirmation_page import OrderConfirmationPage
from pages.sign_in_page import SignInPage
from utils import get_driver

class TestOrderPlacementUser:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = get_driver()
        yield self.driver
        self.driver.quit()

    @pytest.mark.dependency(name="sign_in")
    @pytest.mark.testcase("1")
    def test_sign_in(self, setup):
        driver = setup  # Access the driver passed from the fixture
        home_page = HomePage(driver)
        sign_in_page = SignInPage(driver)

        # Click on Sign In button from home page
        home_page.click_sign_in_button()

        # Fill in username field
        sign_in_page.set_username("ralucauciu@gmail.com")

        # Fill in password field
        sign_in_page.set_password("Test1234")

        # Click on Sign in button from logging in page
        sign_in_page.click_sign_in_button()

        # Confirm you are logged in
        time.sleep(5)
        assert "Welcome, RALUCA UCIU!" in sign_in_page.get_user_logged_in()

        # Go to Home Page
        home_page.click_logo()

    @pytest.mark.dependency(name="add_to_cart")
    @pytest.mark.dependency(depends=["sign_in"])
    @pytest.mark.testcase("2")
    def test_add_item_to_cart(self, setup):
        driver = setup  # Access the driver passed from the fixture
        home_page = HomePage(driver)

        # You should access self.home_page here after setup has run
        home_page.select_women_menu()
        home_page.select_tops_menu()
        home_page.click_first_item()

        print("Item title:", home_page.get_item_title())  # Print the title of the item
        assert "Breathe-Easy Tank" in home_page.get_item_title()

        # Select size S
        home_page.select_size_s()

        # Select color Yellow
        home_page.select_color_yellow()

        # Set quantity to 2
        home_page.set_quantity(2)

        # Click on Add to Cart
        home_page.click_add_to_cart()

        # Wait for confirmation message and assert it contains the item title
        print(home_page.get_confirmation_message())
        expected_message = f"You added {home_page.get_item_title()} to your shopping cart."
        assert expected_message in home_page.get_confirmation_message(), \
            f"Expected {expected_message} but got: {home_page.get_confirmation_message()}"

        # Check that cart was updated
        assert home_page.get_quantity_from_cart_icon() == '2', \
            f"Expected quantity in cart to be 2 but got {home_page.get_quantity_from_cart_icon()}"

    @pytest.mark.dependency(depends=["add_to_cart"])
    @pytest.mark.dependency(name="proceed_to_checkout")
    @pytest.mark.testcase("3")
    def test_proceed_to_checkout(self, setup):
        driver = setup  # Access the driver passed from the fixture
        home_page = HomePage(driver)
        checkout_page = CheckoutPage(driver)

        # Get item price
        item_price = home_page.get_item_price()

        # Get quantity from cart icon
        quantity_cart = home_page.get_quantity_from_cart_icon()

        # Click on the cart icon
        home_page.click_on_cart_icon()

        # Calculate the subtotal price
        expected_subtotal = item_price * int(quantity_cart)

        # Assert that the calculated subtotal matches the displayed subtotal
        assert expected_subtotal == home_page.get_subtotal_price(), f"Expected subtotal {expected_subtotal}, but got {home_page.get_subtotal_price()}"

        # Proceed to checkout
        home_page.click_on_proceed_to_checkout()

        assert checkout_page.get_checkout_page_header() == 'Shipping Review & Payments', \
            f"Expected 'Shipping Review & Payments' but got {checkout_page.get_checkout_page_header()}"

    @pytest.mark.dependency(name="confirm_shipping")
    @pytest.mark.dependency(depends=["proceed_to_checkout"])
    @pytest.mark.testcase("4")
    def test_confirm_shipping(self, setup):
        driver = setup
        checkout_page = CheckoutPage(driver)
        order_confirmation_page = OrderConfirmationPage(driver)

        # Verify that the shipping address section is visible
        assert checkout_page.get_shipping_address_section().is_displayed()

        # Verify section for shipping address already save in account is displayed
        assert checkout_page.get_shipping_address_selected().is_displayed()

        # Verify that the shipping method section is visible
        assert checkout_page.get_shipping_method_section().is_displayed()

        # Select a first shipping method
        checkout_page.select_shipping_method()

        # Proceed to payment
        checkout_page.click_next_button()

        # Verify that the payment method section is visible
        assert checkout_page.get_payment_method_section().is_displayed()

        time.sleep(5)
        # Place order
        checkout_page.click_place_order_button()
        print("Clicked place order button, waiting for confirmation...")
        # Wait for the confirmation page URL
        WebDriverWait(driver, 30).until(EC.url_contains("checkout/onepage/success/"))

        # Verify that the order confirmation page is displayed
        assert "Thank you for your purchase!" in order_confirmation_page.get_order_confirmation_title(), \
            f"Expected 'Thank you for your purchase!', but got {order_confirmation_page.get_order_confirmation_title()}"

    @pytest.mark.dependency(depends=["confirm_shipping"])
    @pytest.mark.dependency(name="order_confirmation")
    @pytest.mark.testcase("4")
    def test_order_confirmation(self, setup):
        driver = setup
        order_confirmation_page = OrderConfirmationPage(driver)

        # Check the order number is provided
        assert "Your order number is: " in order_confirmation_page.get_order_number(), \
        f"Expected to provide order number, but got {order_confirmation_page.get_order_number()}"

        # Continue button presence
        assert order_confirmation_page.get_continue_shopping_button().is_enabled()
