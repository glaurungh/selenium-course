import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
        ]

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)
    elm = browser.find_element_by_css_selector("div>textarea")
    answer = math.log(int(time.time()))
    elm.send_keys(str(answer))
    submit_button = browser.find_element_by_css_selector("button.submit-submission")
    submit_button.click()
    time.sleep(1)

    pre = browser.find_element_by_css_selector("pre.smart-hints__hint")
    message = pre.text

    assert message == "Correct!", message
