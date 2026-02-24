import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#scroll down the page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixles moved: ",value)

#2scroll down page still the page is visible
# flag = driver.find_element(By.XPATH,"//td[normalize-space()='India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# time.sleep(4)

#scroll down to page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixles moved: ",value)
time.sleep(3)

#scroll up from bottom to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixles moved: ",value)
time.sleep(3)
