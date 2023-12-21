from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.aparat.com/mehrabkb")
time.sleep(5)
video_tag = driver.find_elements(By.CSS_SELECTOR, "a.video")
time.sleep(10)
for i in range(0 , 5):
    driver.execute_script('window.scrollBy(0, 3000);')
    time.sleep(5)
links = [elem.get_attribute('href') for elem in video_tag]
count = 0
for link in links :
    driver.execute_script("window.open('" + link + "')")
    time.sleep(10)
    driver.execute_script("document.querySelector('video').play()")
    time.sleep(5)
