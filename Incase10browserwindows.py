# we will use looping approach

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(4)
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowids = driver.window_handles

# for i in windowids:
#     driver.switch_to.window(i)
#     print(driver.title)


for i in windowids:
    driver.switch_to.window(i)
    if driver.title=="OrangeHRM":
        driver.close()

time.sleep(3)

#suppose you want to close 2 and 3 pages use title

for i in windowids:
    driver.switch_to.window(i)
    if driver.title=="OrangeHRM" and driver.title=="XYZ":
        driver.close()

time.sleep(3)
