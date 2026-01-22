from playwright.sync_api import Playwright

def pytest_playwright_config(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")
