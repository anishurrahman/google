from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
executable_path = "C:\\Users\\Anis\\Desktop\\python\\chromedriver.exe"
driver = webdriver.Chrome(executable_path)
#sleep(5)
driver.maximize_window()
#driver.quit()
#URL
driver.get('https://td.com')
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/section/div/div/div/div/div[2]/div[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="formElement_0"]').send_keys('ddas')
driver.find_element(By.NAME,'password').send_keys('add')
driver.find_element(By.ID, '186-loginCheckbox').click()
driver.find_element(By.XPATH, '//*[@id="loginForm"]/button').click()
driver.close()
driver.quit()

