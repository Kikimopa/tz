from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser', "-B", action='store', default="Chrome", help='Choose browser: Chrome, Firefox')


@pytest.fixture(scope="session")
def driver(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
        yield driver
        print("\nquit browser..")
        driver.close()
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()
        yield driver
        print("\nquit browser..")
        driver.close()