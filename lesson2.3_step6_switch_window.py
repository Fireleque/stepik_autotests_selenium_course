from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button.trollface")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))

    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
