from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element_by_id("num1")

    value2 = browser.find_element_by_id("num2")
    result = int(value1.text) + int(value2.text)
    print("Сумма равна:", result)

    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector(f'[value="{str(result)}"]').click() # формат стоки

    time.sleep(3)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
