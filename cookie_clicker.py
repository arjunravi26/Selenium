import undetected_chromedriver as uc
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


cookie_site = "https://orteil.dashnet.org/cookieclicker/"
button_id = "bigCookie"
cookie_text_id = "cookies"
driver = uc.Chrome()
driver.get(url=cookie_site)
WebDriverWait(driver=driver, timeout=5).until(
    ec.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'English')]")))
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()
time.sleep(4)
WebDriverWait(driver=driver, timeout=5).until(
    ec.presence_of_all_elements_located((By.ID, button_id)))
cookie_btn = driver.find_element(By.ID, button_id)
WebDriverWait(driver=driver, timeout=5).until(
    ec.presence_of_all_elements_located((By.ID, cookie_text_id)))
product_prefix = "product"
product_price_prefix = "productPrice"
product_owned_prefix = "productOwned"
for i in range(12000):
    cookie_btn.click()
    cookie_text = driver.find_element(By.ID, cookie_text_id)
    cookie_count = cookie_text.text
    count, *text = cookie_count.split()
    cookie_count = int(count)
    for j in range(4):
        product_owned_count = 0
        price =  driver.find_element(By.ID, product_price_prefix + str(j)).text
        if price:
            price = int(price.replace(",",""))
        else:
            price = float('inf')
        product_owned = driver.find_element(By.ID,product_owned_prefix + str(j)).text
        if product_owned:
            product_owned_count = int(product_owned)
        if cookie_count >= price and product_owned_count < 2:
            product = driver.find_element(By.ID,product_prefix + str(j))
            product.click()
            break
time.sleep(3)
time.sleep(15)
driver.quit()
