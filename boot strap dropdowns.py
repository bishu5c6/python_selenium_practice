from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countrieslist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

print(len(countrieslist))

for i in countrieslist:
    if i.text == "Iran":
        i.click()
        break
time.sleep(7)