from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest_treasure = browser.find_element_by_id("treasure")
    treasure_value = chest_treasure.get_attribute("valuex")
    answer = calc(treasure_value)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(answer)

    time.sleep(3)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()