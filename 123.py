#!/usr/bin/env python
# encoding: utf-8
import time

from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
#time.sleep(3)
#driver.maximize_window()

# navigate to the application home page
driver.get("http://moxian.com/")
driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div/p/a[1]")



time.sleep(3)
driver.close()
