from selenium import webdriver
from selenium.webdriver.common.by import By
import time


ops=webdriver.ChromeOptions
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)
driver.get("https://whatmylocation.com/#google_vignette")
driver.maximize_window()

time.sleep(4)