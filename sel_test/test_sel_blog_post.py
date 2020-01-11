from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="module")
def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
    yield driver
    driver.quit()

@pytest.fixture
def browser(open_browser):
    driver = open_browser
    driver.get("http://127.0.0.1:8000/post/1/")
    return driver 

def test_blog_post_main_title(browser: WebDriver):
    main_title = browser.find_element_by_css_selector(".page-header > h1 > a")
    assert main_title != None
    assert main_title.text == "Django Girls Blog"

def test_blog_post_title(browser: WebDriver):
    post_title = browser.find_element_by_css_selector(".post > h2")
    assert post_title != None
    assert post_title.text != ""

def test_blog_post_content(browser: WebDriver):
    post_content = browser.find_element_by_css_selector(".post > p")
    assert post_content != None
    assert post_content.text != ""