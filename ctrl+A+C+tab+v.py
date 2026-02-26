from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()

# ctrl+A
# ctrl+c
# ctrl+v
# tab

input1=driver.find_element(By.XPATH,"//textarea[@name='text1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("My name is Pinnika Biswanth")

act=ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()


#inpuy 1--> ctrl+c copy text
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

#pressing tab key
act.send_keys(Keys.TAB).perform()

#performing ctrl v
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(3)