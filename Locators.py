# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class SearchPageLocater:

    def __init__(self):
        pass

    search_box = (By.XPATH,'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

class ResultPageLocator:
    def __init(self):
        pass

    result_stats = (By.XPATH,'//*[@id="result-stats"]')