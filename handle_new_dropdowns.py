from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(12)
driver.maximize_window()

drpcountry_ele=driver.find_element(By.XPATH,"//select[@id='country']")
#whenever you have select dropdown it is best practice tuse select dropdown

drpcountry=Select(drpcountry_ele)
# drpcountry.select_by_visible_text('India')
# drpcountry.select_by_value("canada")#onlyvisisble in inspect element
# drpcountry.select_by_index(4)#count manualsyy
# time.sleep(3)


# capture all the options and print them
alloptions=drpcountry.options
print("total number of options:",len(alloptions))

# for i in alloptions:
#     print(i.text)

# select option from dropdown without using built-in method
# for opt in alloptions:
#     if opt.text=="India":
#         opt.click()
#         break
# time.sleep(3)

allOptions=driver.find_elements(By.XPATH,'//*[@id="input-country"]/option')
print(len(allOptions))
