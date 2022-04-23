from selenium import webdriver
import os
import time

url = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "lesson2.2_step8_app.txt"
file_path = os.path.join(current_dir, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(url)

    firsname = browser.find_element_by_name("firstname")
    firsname.send_keys('Ivantest')

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys('Ivanovtest')

    email = browser.find_element_by_name("email")
    email.send_keys('ivanivanovtest@mail.inbox.ru')

    sendfile = browser.find_element_by_css_selector('[type="file"]')
    sendfile.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()
    
finally:
    time.sleep(10)
    browser.quit()
