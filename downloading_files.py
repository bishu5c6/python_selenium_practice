from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import os
location=os.getcwd()

def chrome_options():
    # from selenium import webdriver

    preferences = {"download.default_directory": location} #save file in desired location
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=ops)
    return driver

def edge_options():
    # from selenium import webdriver

    preferences = {"download.default_directory": location} #save file in desired location
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(options=ops)
    return driver

def firefox_options():
    # from selenium import webdriver

    # preferences = {"download.default_directory": location} #save file in desired location
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList",2)
    #0-desktop 1-desktop 2- desired location
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox(options=ops)

    return driver

driver=chrome_options()
driver.get("https://www.princexml.com/samples/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='/samples/icelandic/dictionary.pdf']").click()
time.sleep(4)