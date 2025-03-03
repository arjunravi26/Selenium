import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# service = Service(executable_path="chromedriver.exe")
# options = Options()
# driver = webdriver.Chrome(service=service,options=options)
# driver.get('https://github.com')
import undetected_chromedriver as uc
driver = uc.Chrome()
driver.get('https://google.com')
time.sleep(2)
driver.set_window_size(1920, 1080)
input_element = driver.find_element(By.NAME, "user_email") #gLFyf password
time.sleep(5)
text = "arjunravi1523@gmail.com"
for c in text:
    input_element.send_keys(c)
    t = np.random.uniform(0.1,0.5)
    time.sleep(t)
time.sleep(2)
# input_element = driver.find_element(By.NAME, "password") #gLFyf password
# time.sleep(5)
# text = "3JbZPqHiX3ZFThJ"
# for c in text:
#     input_element.send_keys(c)
#     t = np.random.uniform(0.1,0.5)
#     time.sleep(t)
time.sleep(2)
input_element.send_keys(Keys.ENTER)

time.sleep(30)

driver.quit()