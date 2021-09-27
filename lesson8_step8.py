from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element_by_css_selector("input.form-control[name='firstname']")
    fname.send_keys("Ivan")
    lname = browser.find_element_by_css_selector("input.form-control[name='lastname']")
    lname.send_keys("Petrov")
    email = browser.find_element_by_css_selector("input.form-control[name='email']")
    email.send_keys("ivan@petrov.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload = browser.find_element_by_css_selector("#file")
    upload.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

