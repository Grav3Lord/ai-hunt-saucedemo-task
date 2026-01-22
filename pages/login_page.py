from playwright.sync_api import Page, expect
import allure

class LoginPage:
    URL = "https://www.saucedemo.com/"
    ERROR_WRONG_PASSWORD = "Epic sadface: Username and password do not match any user in this service"
    ERROR_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    ERROR_USERNAME_REQUIRED = "Epic sadface: Username is required"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[data-test=username]")
        self.password_input = page.locator("input[data-test=password]")
        self.login_button = page.locator("input[data-test=login-button]")
        self.error_message = page.locator("h3[data-test=error]")

    def open(self):
        with allure.step(f"Open page {self.URL}"):
            self.page.goto(self.URL)

    def login(self, user: str, password: str):
        with allure.step(f"Filling username"):
            self.username_input.fill(user)
        with allure.step(f"Filling password"):
            self.password_input.fill(password)
        with allure.step(f"Clcking on login button"):
            self.login_button.click()

    def assert_error(self, text: str):
        with allure.step(f"Check error message contains: {text}"):
            expect(self.error_message).to_contain_text(text)

    def assert_logged_in(self):
        with allure.step("Verify user is logged in"):
            expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
            expect(self.page.locator(".inventory_list")).to_be_visible()