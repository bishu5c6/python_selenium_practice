from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
driver = webdriver.Chrome()

driver.implicitly_wait(10)

# driver.get("https://demo.nopcommerce.com/")
#
# driver.maximize_window()
#
# registration_link=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.XPATH,"//a[normalize-space()='Register']").send_keys(registration_link)

#selenium 4 switches to new tab
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.youtube.com/")

driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://www.youtube.com/")