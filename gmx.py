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


def gmx_function(driver):
      usernameStr = 'sidneylewiswfp1@gmx.com'
      passwordStr = 'mypass123456789'
      
      driver.get('https://www.gmx.com/mail/campaign/5019856.html')
      button = driver.find_element_by_id('login-button')
      button.click()
         
      time.sleep(10)
      username = driver.find_element_by_id('login-email')
      username.send_keys(usernameStr)


      password = driver.find_element_by_id('login-password')
      password.send_keys(passwordStr)
        
      time.sleep(15)

      signInButton = driver.find_element_by_xpath('//*[@id="login-form"]/button/span').click()
      time.sleep(20)
