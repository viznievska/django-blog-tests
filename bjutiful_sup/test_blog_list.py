from set_up import set_up
import pytest


@pytest.fixture
def soup():
    return set_up()

def test_blog_main_title(soup):
    title = soup.find(class_ = "page-header")
    assert title != None
    assert title.text.strip() == "Django Girls Blog"

def test_blog_post_list(soup):
    posts = soup.find_all(class_ = "post")
    assert posts != []
    
def test_blog_post_list_titles(soup):
    posts = soup.find_all(class_ = "post")
    for post in posts:
        h2 = post.find("h2")
        assert h2 != None
        a = h2.find("a")     
        assert a!= None
        assert a.text != ""

def test_blog_posts_content(soup):
    posts = soup(class_ = "post")

    for post in posts:
        p = post.find('p')
        assert p != None
        content = p.text
        assert content != ""






