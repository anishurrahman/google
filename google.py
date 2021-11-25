import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Anis\\Desktop\\python\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get('https://google.com')
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Anishur")
driver.find_element_by_name("btnK").click()
print(driver.title)
time.sleep(10)
driver.close()
driver.quit()

