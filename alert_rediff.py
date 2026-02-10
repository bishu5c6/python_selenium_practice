from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
alertq=driver.switch_to.alert
print(alertq.text)
alertq.accept()
alertq.dismiss()
time.sleep(4)






