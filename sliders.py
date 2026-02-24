import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

first_slider = driver.find_element(By.XPATH,"//span[1]")
second_slider = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(2) > span:nth-child(3)")

print("Location of slider befor moving")
print(first_slider.location) #'x': 425, 'y': 28}
print(second_slider.location) # {'x': 521, 'y': 247}

act = ActionChains(driver)
act.drag_and_drop_by_offset(first_slider,100,0).perform()
act.drag_and_drop_by_offset(second_slider,-55,0).perform()
time.sleep(5)