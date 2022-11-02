import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in")
myacc = driver.find_element(By.LINK_TEXT, "My Account")
myacc.click()
email = driver.find_element(By.CSS_SELECTOR, "#username")
email.send_keys("egor4eck@gmail.com")
# time.sleep(3)
paswrd = driver.find_element(By.CSS_SELECTOR, "#password")
paswrd.send_keys("SLOZHNIYparol")
# time.sleep(3)
login = driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input.woocommerce-Button.button")
login.click()
shop = driver.find_element(By.LINK_TEXT, "Shop")
shop.click()
html5 = driver.find_element(By.CSS_SELECTOR, ".post-181.product")
html5.click()
title = WebDriverWait(driver, 20).until(
       EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title.entry-title"), "HTML5 Forms"))


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
# # time.sleep(3)
# paswrd = driver.find_element(By.CSS_SELECTOR, "#password")
# paswrd.send_keys("SLOZHNIYparol")
# # time.sleep(3)
# login = driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# html = driver.find_element(By.LINK_TEXT, "HTML")
# html.click()
# goods = driver.find_elements(By.CLASS_NAME, "status-publish")
# if len(goods) == 3:
#        print ("На странице 3 книги")
# else:
#        print("Ошибка. Количество книг:" + str(len(goods)))
#


#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
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
# # time.sleep(3)
# paswrd = driver.find_element(By.CSS_SELECTOR, "#password")
# paswrd.send_keys("SLOZHNIYparol")
# # time.sleep(3)
# login = driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# sometext = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element_value((By.CLASS_NAME, "orderby"), "menu_order"))
# time.sleep(5)
# def_text = driver.find_element(By.CLASS_NAME, "orderby")
# sort = Select(def_text)
# Select.select_by_visible_text(sort, "Sort by price: high to low")
# time.sleep(5)
# def_text = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element_value((By.CLASS_NAME, "orderby"), "price-desc"))


#
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
# # time.sleep(3)
# paswrd = driver.find_element(By.CSS_SELECTOR, "#password")
# paswrd.send_keys("SLOZHNIYparol")
# # time.sleep(3)
# login = driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input.woocommerce-Button.button")
# login.click()
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# android_book = driver.find_element(By.CSS_SELECTOR, ".post-169 h3")
# android_book.click()
# old_price = driver.find_element(By.CSS_SELECTOR, ".price > del > span")
# old_price_text = old_price.text
# new_price = driver.find_element(By.CSS_SELECTOR, ".price > ins > span")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# cover = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# cover.click()
# cover_x = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# cover_x.click()

#
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
#
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# driver.execute_script("window.scrollBy(0, 400);")
# html_book = driver.find_element(By.CSS_SELECTOR, "li.post-182 > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
# html_book.click()
# time.sleep(5)
# item = driver.find_element(By.CLASS_NAME, "cartcontents")
# item_text = item.text
# price = driver.find_element(By.CSS_SELECTOR, "a > span.amount")
# price_text = price.text
# assert item_text == "1 Item"
# assert price_text == "₹180.00"
# cart = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-icon-shopping-cart-0")
# cart.click()
# subtotal = WebDriverWait(driver, 20).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal > td > span"), "₹180.00"))
#
# total = WebDriverWait(driver, 20).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.order-total > td > strong > span"), "₹183.60"))





#
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
#
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# html_book = driver.find_element(By.CSS_SELECTOR, "li.post-182 > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
# html_book.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 500);")
# js_book = driver.find_element(By.CSS_SELECTOR, " li.post-180> a.button.product_type_simple")
# js_book.click()
# cart = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-icon-shopping-cart-0")
# cart.click()
# time.sleep(3)
# rem = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td.product-remove > a")
# rem.click()
# time.sleep(3)
# undo = driver.find_element(By.LINK_TEXT, "Undo?")
# undo.click()
# time.sleep(3)
# js3 = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td.product-quantity > div > input")
# js3.clear()
# js3.send_keys("3")
# upd = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > input.button")
# upd.click()
# quantity = WebDriverWait(driver, 20).until(
#       EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "tr:nth-child(1) > td.product-quantity > div > input"), "3"))
# time.sleep(3)
# apply = driver.find_element(By.CSS_SELECTOR, ".coupon > input.button")
# apply.click()
# inf = WebDriverWait(driver, 20).until(
#       EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error > li"), "Please enter a coupon code."))


#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in")
#
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# html_book = driver.find_element(By.CSS_SELECTOR, "li.post-182 > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
# html_book.click()
# time.sleep(3)
# cart = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-icon-shopping-cart-0")
# cart.click()
# checkout = WebDriverWait(driver, 20).until(
#        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.woocommerce > div > div > div > a")))
# checkout.click()
# first_name = WebDriverWait(driver, 20).until(
#        EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")))
# first_name.send_keys("John")
# last_name = driver.find_element(By.CSS_SELECTOR, "#billing_last_name")
# last_name.send_keys("Brown")
# mail = driver.find_element(By.CSS_SELECTOR, "#billing_email")
# mail.send_keys("johnbrown@gmail.com")
# country = driver.find_element(By.CSS_SELECTOR, "#select2-chosen-1")
# country.click()
# country2 = driver.find_element(By.ID, "select2-result-label-104")
# country2.click()
# phone = driver.find_element(By.ID, "billing_phone")
# phone.send_keys("88005553535")
# adress = driver.find_element(By.ID, "billing_address_1")
# adress.send_keys("Down st 21")
# code = driver.find_element(By.ID, "billing_postcode")
# code.send_keys("123456789")
# city = driver.find_element(By.ID, "billing_city")
# city.send_keys("Barcelona")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# check = driver.find_element(By.CSS_SELECTOR, "#payment_method_cheque")
# check.click()
# PO = driver.find_element(By.CSS_SELECTOR, "#place_order")
# PO.click()
# inf = WebDriverWait(driver, 20).until(
#        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# payment = WebDriverWait(driver, 20).until(
#        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) > td"), "Check Payments"))
