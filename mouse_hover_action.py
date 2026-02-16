from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(19)

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys('Admin')
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('admin123')

driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
driver.find_element(By.XPATH,"////button[@class='oxd-icon-button oxd-main-menu-button']").click()
time.sleep(4)
# admin = driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")
# usermgmt=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
# users=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")
#
# act = ActionChains(driver)
# act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()
# time.sleep(5)