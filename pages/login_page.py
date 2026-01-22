from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_test_id("username")
        self.password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")
        self.error_message = page.get_by_test_id("error")

    def open(self):
        self.page.goto(self.URL)

    def login(self, user: str, password: str):
        self.username_input.fill(user)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error(self, text: str):
        expect(self.error_message).to_contain(text)