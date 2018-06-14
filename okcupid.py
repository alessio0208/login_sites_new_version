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

def okcupid_function(driver): 
      usernameStr = 'sidneylewiswfp@rediffmail.com'
      passwordStr = 'mypass'

      driver.get('https://www.okcupid.com/')

      signin = driver.find_element_by_class_name('splashdtf-header-signin-splashButton')
      signin.click()
      
      time.sleep(5)
      username = driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[2]/div[1]/span[2]/input')
      username.send_keys(usernameStr)


      password = driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[2]/div[2]/span[2]/input')
      password.send_keys(passwordStr)


      signInButton = driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[3]/input')
      signInButton.click()
      time.sleep(20)
