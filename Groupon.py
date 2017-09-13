import unittest
from selenium import webdriver
import time 
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By

'''
IP=input("Enter the Admin IP address : - ")
LoginId=input("Enter your Login Id: - ")
LoginPw=input("Enter your Password : - ")
'''

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):                            # change cls to self if you want to use same session of chrome
        cls.driver=webdriver.Chrome()
        
        #self.driver.maximize_window()
        
        cls.driver.get("http://10.65.12.120/")
        
    def test_login(self):
        self.search_field=self.driver.find_element_by_id("login-panel-input-email")
        self.search_field.clear()
        self.search_field.send_keys("admin@ssl.com")
        self.driver.implicitly_wait(50)
        time.sleep(1)
        
        search_field=self.driver.find_element_by_id("login-panel-input-password")
        search_field.clear()        
        search_field.send_keys("admin")
        self.driver.implicitly_wait(50)
        time.sleep(1)
        
        search_field=self.driver.find_element_by_id("login-panel-signin-button")
        search_field.click()
        time.sleep(5)

        self.driver.find_element(by=By.XPATH, value='//*[@id="main-page"]/div[1]/div[8]/div/div[3]/span[2]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="page-header-navbar"]/div/div[1]/div/div[3]/a/i').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="page-header-navbar"]/div/div[1]/div/div[3]/ul/li[1]/ul/li[2]/ul/li[1]/span').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="page-content"]/div/div[2]/div[2]/div[3]/ul/li[2]').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="page-content"]/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div[1]/div[1]/span[1]/span/span/i').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="page-content"]/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div[1]/div[1]/span[1]/span/div/div/div/div/ul/li[1]').click()
        time.sleep(1)

        ################## Selection of APP - Alibaba #####################
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="page-content"]/div/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/span').click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value='//*[@id="page-content"]/div/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/ul/li[9]').click()
        time.sleep(1)     
             
        ####################################################################
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="page-content"]/div/div[2]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/div[1]/div[2]/div/span/span[2]/span').click()
        time.sleep(1)
        
        self.driver.find_element(by=By.XPATH, value='//*[@id="page-content"]/div/div[2]/div[3]/div/div/div/div[4]/div[1]/span[1]').click()
        time.sleep(1)

        
    @classmethod
    def tearDownClass(cls):  
        cls.driver.quit()
        
     
     
        
if __name__=='__main__':
    unittest.main()
    
    
    
    


