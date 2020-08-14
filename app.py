# -*- coding: utf-8 -*-

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary

from pages import SearchPage 
from pages import ResultPage

driver = webdriver.Chrome()

search_page = SearchPage(driver)
search_page.open()
search_page.search('Automation tool')

result_page = ResultPage(search_page.driver)
print(result_page.get_result_stats())

sleep(1)
result_page.close()