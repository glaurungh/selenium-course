from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price_element =  WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button_book = browser.find_element_by_css_selector("button#book")
    button_book.click()

    x_element = browser.find_element_by_css_selector('span#input_value')
    x = x_element.text
    y = calc(x)

    input_ans = browser.find_element_by_id('answer')
    input_ans.send_keys(y)

    button = browser.find_element_by_css_selector("button#solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

