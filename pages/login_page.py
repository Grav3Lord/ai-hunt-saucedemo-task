from playwright.sync_api import Page, expect


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
        self.page.goto(self.URL)

    def login(self, user: str, password: str):
        self.username_input.fill(user)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error(self, text: str):
        expect(self.error_message).to_contain_text(text)