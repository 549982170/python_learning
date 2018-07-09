#!/usr/bin/env python
# encoding: utf-8
import time

from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://automationtesting.sinaapp.com/")

# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("webdriver")
search_field.submit()



time.sleep(6)
products = driver.find_elements_by_xpath("//a[@class='searchable']")
# get the number of anchor elements found
print "Found " + str(len(products)) + " pages:"

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print product.get_attribute('href')

# close the browser window
driver.quit()