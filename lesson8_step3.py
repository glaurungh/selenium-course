from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector('#num1')
    num2 = browser.find_element_by_css_selector('#num2')
    x = int(num1.text) + int(num2.text)

#    browser.find_element_by_css_selector('#dropdown').click()
#    browser.find_element_by_css_selector("option[value='"+str(x)+"']").click()

    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(x))

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

