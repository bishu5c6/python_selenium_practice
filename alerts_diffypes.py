from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.implicitly_wait(5)
driver.maximize_window()
#opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(4)

alertwindow= driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Good Morning World")
#accept and dismiss method
alertwindow.accept()
alertwindow.dismiss()#pass the null and close the alert window
time.sleep(4)


