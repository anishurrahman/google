"""
Test Case: 05
1) Navigate to google.com
2) Open orangehrm app
3) Enter correct username
4) Enter correct password
5) Click submit button
7) Report bug(s) on Jira
"""
import time

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
executable_path = 'C:\\Users\\Anis\\Desktop\\python\\chromedriver.exe'
driver = webdriver.Chrome(executable_path)

#driver.get('https://google.com')
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.find_element(By.NAME, 'txtUsername').send_keys('Admin')
driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()
#sleep(10)
print(driver.title)
time.sleep(5)
driver.close()
driver.quit()
