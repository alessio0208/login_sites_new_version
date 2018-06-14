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

def rediff_function(driver):
      usernameStr = 'sidneylewiswfp'
      passwordStr = "mypass"
      
      
      driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
      
     
      username = driver.find_element_by_id('login1')
      username.send_keys(usernameStr)
        
        
      time.sleep(5)

      password = driver.find_element_by_id('password')
      password.send_keys(passwordStr)
        
      time.sleep(5)
       
      signInButton = driver.find_element_by_name('proceed')
      signInButton.click()
      
      time.sleep(30)
   
      driver.get('https://f5mail.rediff.com/ajaxprism/container?angular=1&els=8315a962fd30ca71491059ba2683e937&user_size=1#folder/Drafts')
