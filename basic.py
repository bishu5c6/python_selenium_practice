from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"(//button[normalize-space()='Login'])[1]").click()
# driver.find_element_by_name()
print(driver.title)
expected_title = "OrangeHRM"
if expected_title == driver.title:
    print("login passed")
else:
    print("login failed")
time.sleep(5)

driver.quit()


