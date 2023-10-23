import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    first = browser.find_element(By.NAME, "firstname")
    first.click()
    first.send_keys("Alex")
    second = browser.find_element(By.NAME, "lastname")
    second.click()
    second.send_keys("A")
    third = browser.find_element(By.NAME, "email")
    third.click()
    third.send_keys("a@a.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    choosefile = browser.find_element(By.ID, "file")
    choosefile.send_keys(file_path)
    print(os.path.abspath(__file__))

    button = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
