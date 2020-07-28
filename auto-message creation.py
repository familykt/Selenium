#!/usr/bin/env python
# coding: utf-8

# In[45]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[46]:


import json
with open("./account.json") as json_file:
    json_data = json.load(json_file)


# In[47]:


driver = webdriver.Chrome()

action = ActionChains(driver)
wait = WebDriverWait(driver, 10)


# In[48]:


# move to tripla api
url = "https://cm.staging.tripla.ai/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)


# In[49]:


# log in
try:
    driver.find_element_by_id('__BVID__36').send_keys(json_data['Account'][0]['id'])
    driver.find_element_by_id('__BVID__38').send_keys(json_data['Account'][0]['password'])
    driver.find_element_by_css_selector('.btn').click()
    print("successfully logged in")
except:
    print("login failed")



# In[50]:


# move to auto-message page
time.sleep(5)
hotel_url = "https://cm.staging.tripla.ai/hotels/4/auto-messages/"
driver.get(hotel_url)


# In[33]:


# move to creating page
button_1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-success')))
button_1.click()


# In[34]:


#creating auto message
am_text = "test_by_selenium(john)"
time.sleep(2)
try:
    driver.find_element_by_css_selector('.custom-checkbox').click()
    driver.find_element_by_xpath('//*[@id="4"]/div[1]/div/div[2]/fieldset[3]/div[1]/input').send_keys(am_text)
    driver.find_element_by_xpath('//*[@id="4"]/div[1]/div/div[2]/div[1]/div[9]').click()
    driver.find_element_by_xpath('//*[@id="4"]/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/div[1]/fieldset[1]/div[1]/textarea[1]').send_keys(am_text)
    driver.find_element_by_css_selector('.btn.minw-3.btn-success').click()
    print("successfully created")
except:
    print("failed creation")


# In[35]:


#move to edit page
button_2 = wait.until(EC.presence_of_element_located((By.XPATH,"//td[contains(text(),'"+am_text+"')]")))
try:
    button_2.click()
    print("successfully moved to created auto-message")
    time.sleep(5)
except:
    print("failed to move to created auto-message")


# In[36]:


#click the delete button
button_3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.minw-3.btn-outline-info')))
try:
    button_3.click()
    driver.find_element_by_css_selector('.btn.btn-info').click()
    print("successfully deleted")
    time.sleep(5)
except:
    print("failed to deleted")

finally:
    driver.quit()

