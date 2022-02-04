from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text

    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    sum=int(x)+int(y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))  # ищем элемент с текстом "Python"



    sub_button = browser.find_element_by_css_selector('[type="submit"]')
    sub_button.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
        # закрываем браузер после всех манипуляций
    browser.quit()