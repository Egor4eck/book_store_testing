import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in")
driver.execute_script("window.scrollBy(0, 600);")
book = driver.find_element(By.CSS_SELECTOR, "#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > img")
book.click()
rew = driver.find_element(By. CLASS_NAME, "reviews_tab")
rew.click()
driver.execute_script("window.scrollBy(0, 800);")
star = driver.find_element(By.CLASS_NAME, "star-5")
star.click()
comment = driver.find_element(By.CSS_SELECTOR, "#comment")
comment.send_keys("Nice book!")
name = driver.find_element(By.CSS_SELECTOR, "#author")
name.send_keys("John")
mail = driver.find_element(By.CSS_SELECTOR, "#email")
mail.send_keys("johnbrown@gmail.com")
submit = driver.find_element(By.CLASS_NAME, "submit")
submit.click()

