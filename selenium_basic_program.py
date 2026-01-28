from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Start the browser session (using Chrome in this example)
driver = webdriver.Chrome()

try:
    # 2. Take action on the browser: Navigate to a website
    driver.get("https://www.google.com")
    print(f"Navigated to: {driver.title}")

    # Optional: Maximize the window for better interaction
    driver.maximize_window()

    # 3. Find an element (the search box)
    # The search box on Google often has the 'name' attribute 'q'
    search_box = driver.find_element(By.NAME, "q")

    # 4. Take action on the element: Type text and press Enter
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # Optional: Add a short wait to see the results
    time.sleep(3)

    # 5. Request browser information: Assert the title has changed
    assert "Selenium Python" in driver.title
    print("Search successful, title contains 'Selenium Python'")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 6. End the session: Close the browser
    driver.quit()
    print("Browser closed.")
