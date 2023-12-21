from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.aparat.com/v/pyCHA")
time.sleep(20)
tag = driver.find_element(By.CSS_SELECTOR , "a.video-playlist")
tag.click()
#ActionChains(driver).key_down('\ue00d') 

#randomNumber = randint(120 , 1600)
driver.refresh()
