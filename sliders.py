import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()