# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

# %%
@pytest.mark.parametrize(
    ("input","expected"),[
        
    ("red", "<em>RED</em>/レッド - Wikipedia"),
    ("青", "<em>青</em> - Wikipedia"),
    ("きいろ", "五丁目 千 <em>きいろ</em>")
    ]
)
        


# %%
def test_search(input,expected):
    driver = webdriver.Chrome()
    driver.get("http://www.google.co.jp/")
    elem = driver.find_element_by_name("q")
    elem.send_keys(input)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    assert expected in driver.page_source
    driver.close