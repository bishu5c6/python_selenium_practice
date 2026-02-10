from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.maximize_window()

# driver.switch_to.frame("packagelistframe")
driver.find_element(By.XPATH,"//a[normalize-space()='org.openqa.selenium']").click()
# driver.switch_to.default_content()
# driver.switch_to.frame("packagelistframe")
driver.find_element(By.XPATH,"//a[normalize-space()='Architecture']").click()
# driver.switch_to.frame("packagelistframe")
# driver.switch_to.frame("packagelistframe")
driver.find_element(By.XPATH,"//a[normalize-space()='Help']").click()
time.sleep(5)







