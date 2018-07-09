#!/usr/bin/env python
# encoding: utf-8
import time
from selenium import webdriver
dirver=webdriver.Firefox()
dirver.get("http://moxian.com/user/login?_lang_=cs&redirect_url=http://moxian.com/main/")
driver.find_element_by_id("txtEmailUser").clear() 
driver.find_element_by_id("txtEmailUser").send_keys("1@126.com") 
driver.find_element_by_id("txtEmailPwd").clear() 
driver.find_element_by_id("txtEmailPwd").send_keys("123456") 
driver.find_element_by_css_selector("signbtn").click() 
dirver.close()