from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector(".form-control")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector(".form-check-custom .form-check-input")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
