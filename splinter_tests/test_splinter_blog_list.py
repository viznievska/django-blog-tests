from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pytest

executable_path = {'executable_path': ChromeDriverManager().install()}


@pytest.fixture(scope="module")
def open_browser():
    with Browser("chrome", **executable_path) as browser:
        yield browser


@pytest.fixture
def driver(open_browser):
    open_browser.visit("http://127.0.0.1:8000")
    return open_browser


def test_blog_main_title(driver):
    main_title = driver.find_by_css(".page-header a")
    assert main_title != []
    assert main_title.text != ""
