#as soon as you open the application it will ask username and password

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://admin:admin@the-internet.herokuapp.com//basic_auth")
time.sleep(5)

