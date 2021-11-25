from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
executable_path = "C:\\Users\\Anis\\Desktop\\python\\chromedriver.exe"
driver = webdriver.Chrome(executable_path)
#sleep(5)
driver.maximize_window()
#driver.quit()
#URL
driver.get('https://bankofamerica.com')
driver.find_element(By.NAME,'onlineId1').send_keys('asdddd')
driver.find_element(By.ID, 'passcode1').send_keys('ddas1212')
#driver.find_element(By.XPATH,'//*[@id="saveOnlineIdCheckBox"]/div/ul/li/label').click()
driver.find_element(By.ID, 'signIn').click()
sleep(15)
driver.close()
driver.quit()
