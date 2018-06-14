import sys, os
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 


def mailchimp_function(driver):
        usernameStr = 'sidneylewiswfp1'
        passwordStr = 'Mypass12345678#'
   
        driver.get('https://login.mailchimp.com/')
   
        username = driver.find_element_by_id('username')
        username.send_keys(usernameStr)
        
        
        time.sleep(5)

        password = driver.find_element_by_id('password')
        password.send_keys(passwordStr)
        
        time.sleep(5)
        
        driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[4]/button').click()
       
        time.sleep(20)
        #driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/div/div/p[2]/a').click()
        
        #time.sleep(25)
        #driver.find_element_by_id('onward').click()
