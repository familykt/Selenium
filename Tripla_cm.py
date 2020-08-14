#%%
class triplaCM:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    

    def __init__(self,account_id,account_pw):
        self.account_id = account_id
        self.account_pw = account_pw
        
        print("account is registered")
    def login(self):
        
        self.account_id = account_id
        self.account_pw = account_pw
        
        # move to tripla api
        url = "https://cm.staging.tripla.ai/"
        driver = self.webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_id('__BVID__36').send_keys(self.account_id)
            driver.find_element_by_id('__BVID__38').send_keys(self.account_pw)
            driver.find_element_by_css_selector('.btn').click()
            print("successfully logged in")
        except:
            print("login failed")
    def quit(self):
        driver = self.webdriver
        url = driver.command_executor._url
        session_id = driver.session_id
        driver.Remote(command_executor=url,desired_capabilities={})
        driver.session_id = session_id
        driver.quit()

        



# %%
import json
with open("./account.json") as account_file:
    account_data = json.load(account_file)
account_id = account_data['Account'][0]['id']
account_pw = account_data['Account'][0]['password']


CM = triplaCM(account_id,account_pw)
CM.login()

# %%
CM.quit()

# %%
