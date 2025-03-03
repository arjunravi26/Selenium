import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin");
time.sleep(5);
email = driver.find_element(By.CLASS_NAME,"whsOnd")
email.send_keys("Email"+Keys.ENTER)
time.sleep(1500);
# email = driver.find_element(By.CLASS_NAME,"aXBtI")
# email.send_keys("Password"+Keys.ENTER)
# time.sleep(300)
driver.quit()
# aXBtI Wic03c XmnwAc