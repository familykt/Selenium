#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# In[2]:


import json
with open("./account.json") as json_file:
    json_data = json.load(json_file)


# In[3]:


driver = webdriver.Chrome()
action = ActionChains(driver)
wait = WebDriverWait(driver, 10)


# In[4]:


#move to reservation_api
url = "http://staging.tripla-hotel.com/"
driver.get(url)
driver.maximize_window()
timeout = 5


# In[5]:


#move to booking_widget
try:
    availabilty_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.search-widget-wrapper-872d0c > form > div > button')))
    availabilty_button.click()
    time.sleep(2)
    print("moved to booking_widget")
except:
    print("booking_widget is unloaded")


# In[6]:


#move to sign-in page
try:
    reservation_modal = driver.find_element_by_css_selector("#tripla-booking-modal > div > div > iframe")
    driver.switch_to.frame(reservation_modal)
    sign_in_button = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='sign-in-button-container']/div[2]/button[1]")))
    sign_in_button.click()
    time.sleep(2)
    print("moved to sign-in page")
except:
    print("failed to move to sign-in page")


# In[7]:


#click the facebook login
try:
    fb_frame = driver.find_element_by_css_selector("body > div.app-wrapper.webkit-overflow-scrolling > div > div.center-wrapper > form > div.mb-3.text-center > div > span > iframe")
    driver.switch_to.frame(fb_frame)
    sign_in_button_2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#u_0_1 > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > span')))
    sign_in_button_2.click()
    time.sleep(2)
    print("clicked the Facebook login")
except:
    print("failed to move to facebook login")


# In[8]:


#input the id/password
try:
    driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_id("email").send_keys(json_data['Account'][1]['id'])
    driver.find_element_by_id("pass").send_keys(json_data['Account'][1]['password'])
    driver.find_element_by_id("u_0_0").click()
    time.sleep(5)
    print("successfully logged in")

except:
    print("login failed")
finally:
    driver.quit()


# In[ ]:




