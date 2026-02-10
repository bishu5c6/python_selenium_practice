from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(4)
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowids = driver.window_handles

parentwindowid = windowids[0] #B2B21B58640E4C249A8B5013621B0F44
childwindowid = windowids[1] #41B94FBAA8D7FA054E43AEE25E273415
print(parentwindowid, childwindowid)

driver.switch_to.window(childwindowid)
print(driver.title)
time.sleep(5)
driver.switch_to.window(parentwindowid)
print("parent title: ",driver.title)
time.sleep(5)
# windowid = driver.current_window_handle
# print(windowid) #A212CCC94AAAF8000F715030C3C9087B








driver.close()



