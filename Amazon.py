from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
#initialize webdriver
def test_setUp():
    global driver
    executable_path = 'C:\\Users\\Anis\\Desktop\\python\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path)
#expand the window
    driver.maximize_window()
    driver.implicitly_wait(5)
#open the url
def test_logIn():
    driver.get("https://bankofamerica.com")
#Find Element
    driver.find_element_by_id('onlineId1').send_keys('asd@gmail.com')
    driver.find_element_by_xpath('//*[@id="passcode1"]').send_keys('sdasd')
    driver.find_element_by_xpath('//*[@id="signIn"]').click()
def print_functionality():
    print("Test is pass")
    driver.close()
    driver.quit()
