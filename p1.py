from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.get('D:/Honors/loginmapping/home.html')
time.sleep(3)
driver.find_element(By.ID, "login").click()
driver.find_element(By.ID, "email").send_keys('maneesha@gmail.com')
time.sleep(1)
driver.find_element(By.ID, "password").send_keys('123')
time.sleep(1)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
alert = Alert(driver)
alert.accept()
driver.find_element(By.ID, "origin").send_keys('Bapatla')
time.sleep(2)
driver.find_element(By.ID, "destination").send_keys('Guntur')
time.sleep(2)
driver.find_element(By.ID, "bt").click()
time.sleep(5)
driver.find_element(By.ID, "home").click()
time.sleep(1)

driver.close()
