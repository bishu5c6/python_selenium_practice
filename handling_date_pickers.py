from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0) #when you have only one frame use this synatx

#it follows mm/dd/yyyy
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("12/02/2026")
# time.sleep(3)

year = "2027"
month = "march"
date = "30"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()


while True:
    mm=  driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yy= driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    # dd= driver.find_element(By.XPATH,"//a[normalize-space()='28']").text
    if mm==month and yy==year:
        break;
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()

        # time.sleep(3)
#select datesd

# dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table//tbody//tr/td")
# for i in dates:
#     if i.text ==date:
#         i.click()
#     break

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break