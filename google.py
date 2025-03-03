import time
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = uc.Chrome()
try:
    driver.get('https://google.com')
    time.sleep(2)
    driver.set_window_size(1920, 1080)
    WebDriverWait(driver, 5).until(
        ec.presence_of_all_elements_located((By.NAME, "q")))
    input_element = driver.find_element(By.NAME, "q")
    time.sleep(3)
    input_element.clear()
    text = "github arjunravi26"
    input_element.send_keys(text + Keys.ENTER)
    link = driver.find_element(By.PARTIAL_LINK_TEXT,"Arjun Ravi arjunravi26")
    link.click()

    time.sleep(5)
finally:
    driver.quit()
