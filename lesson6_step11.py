from selenium import webdriver
import time

try: 
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    fname = browser.find_element_by_css_selector("div.first_block>div.form-group.first_class>input.form-control.first")
    fname.send_keys('Имя')

    lname = browser.find_element_by_css_selector("div.first_block>div.form-group.second_class>input.form-control.second")
    lname.send_keys('Фамилия')

    email = browser.find_element_by_css_selector("div.first_block>div.form-group.third_class>input.form-control.third")
    email.send_keys('E-mail')

    phone = browser.find_element_by_css_selector("div.second_block>div.form-group.first_class>input.form-control.first")
    phone.send_keys('666')

    address = browser.find_element_by_css_selector("div.second_block>div.form-group.second_class>input.form-control.second")
    address.send_keys('xxx')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

