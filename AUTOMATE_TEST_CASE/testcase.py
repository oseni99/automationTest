from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time 

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10)

username = driver.find_element(By.NAME,"username")
#username.clear()
username.send_keys("Admin")
username.send_keys(Keys.RETURN)
time.sleep(10)
password = driver.find_element(By.NAME, "password")
#password.clear()
password.send_keys("admin123")
password.send_keys(Keys.RETURN)
time.sleep(10)
#logins = driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button")
#logins.click()



act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.quit()


