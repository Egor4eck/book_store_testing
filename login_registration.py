# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in")
# myacc = driver.find_element(By.LINK_TEXT, "My Account")
# myacc.click()
# email = driver.find_element(By.CSS_SELECTOR, "#reg_email")
# email.send_keys("egor4eck@gmail.com")
# time.sleep(3)
# paswrd = driver.find_element(By.CSS_SELECTOR, "#reg_password")
# paswrd.send_keys("SLOZHNIYparol")
# time.sleep(3)
# subbtn = driver.find_element(By.CSS_SELECTOR, "p.woocomerce-FormRow.form-row > input.woocommerce-Button.button")
# subbtn.click()


# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in")
# myacc = driver.find_element(By.LINK_TEXT, "My Account")
# myacc.click()
# email = driver.find_element(By.CSS_SELECTOR, "#username")
# email.send_keys("egor4eck@gmail.com")
# time.sleep(3)
# paswrd = driver.find_element(By.CSS_SELECTOR, "#password")
# paswrd.send_keys("SLOZHNIYparol")
# time.sleep(3)
# login = driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
#
# logout_btn = WebDriverWait(driver, 20).until(
# EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))


