#encoding:utf-8
from selenium import webdriver

br = webdriver.Firefox()
br.get("http://moxian.com/")
br.find_elements_by_partial_link_text("登录").click()





