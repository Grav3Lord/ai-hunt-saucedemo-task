import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.mark.usefixtures("login_page")
class TestLoginPage:

    def test_succesful_login(self, login_page):
        login_page.login("standard_user", "secret_sauce")
        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(login_page.page.locator('.inventory_list')).to_be_visible()

    @pytest.mark.parametrize("user, pwd, error", [
        ("standard_user", "wrong_password", LoginPage.ERROR_WRONG_PASSWORD),
        ("locked_out_user", "secret_sauce", LoginPage.ERROR_LOCKED_OUT),
        ("", "", LoginPage.ERROR_USERNAME_REQUIRED)
    ])
    def test_login_errors(self, login_page, user, pwd, error):
        login_page.login(user, pwd)
        login_page.assert_error(error)

    def test_performance_glitch_user(self, login_page):
        expect(login_page.page).to_have_url("https://www.saucedemo.com/")
        login_page.login("performance_glitch_user", "secret_sauce")
        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(login_page.page.locator('.inventory_list')).to_be_visible()