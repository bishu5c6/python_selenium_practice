from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_condition as EC

driver=webdriver.Chrome()
driver.get("https://www.google.co.in")
mywait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
driver.maximize_window()
a=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("biswanth_Pinnika")
a.submit()

mywait.until(EC.presenece_of_element_located("//h3[@id='_qcuFaYOaL-vInesPkK-V6A0_61']")).click()
# driver.find_element(By.XPATH,"//h3[@id='_qcuFaYOaL-vInesPkK-V6A0_61']").click()
