from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="module")
def open_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()

@pytest.fixture
def browser(open_browser):
    driver = open_browser
    driver.get("http://127.0.0.1:8000")
    return driver
    

def test_blog_list_main_title(browser):
    main_title = browser.find_element_by_css_selector(
        "div.page-header > h1 > a")

    assert main_title != None
    assert main_title.text == "Django Girls Blog"


def test_blog_post_list(browser):
    post_list = browser.find_elements_by_css_selector(".post")

    assert post_list != []
    assert len(post_list) > 0


def test_blog_posts_titles(browser):
    posts_titles = browser.find_elements_by_css_selector(".post h2 > a")

    assert posts_titles != []
    for a in posts_titles:
        title = a.text
        assert title != ""


def test_blog_posts_contents(browser):
    posts_contents = browser.find_elements_by_css_selector(".post > p")

    assert posts_contents != []
    for p in posts_contents:
        assert p.text != ""

def test_blog_click_title_post(browser):
    post_title = browser.find_element_by_css_selector(".post h2 > a")
    text = post_title.text
    post_title.click()
    single_post_title = browser.find_element_by_css_selector(".post > h2")
    assert text == single_post_title.text