from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest

class Test_Fb_Login_Functionality:
    @pytest.fixture()
    def test_setup(self):
        global driver
        executable_path = 'C:\\Users\\Anis\\Desktop\\python\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path)
        driver.maximize_window()
        driver.get("https://facebook.com")
        driver.implicitly_wait(5)

        yield
        print("Test is pass")
        sleep(5)
        driver.close()
        driver.quit()

    def test_loginFunctionality_01(self, test_setup):
        driver.find_element(By.ID, "email").send_keys('asdsad@asa.com')
        driver.find_element(By.ID, "pass").send_keys('a123344')
        driver.find_element(By.NAME, "login").click()
        driver.implicitly_wait(5)
    def test_loginFunctionality_02(self, test_setup):
        driver.find_element(By.ID, "email").send_keys('asdsad@asa.com')
        driver.find_element(By.ID, "pass").send_keys('a123344')
        driver.find_element(By.NAME, "login").click()
        driver.implicitly_wait(5)

