from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/danyullim/Github/selenium/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://danyullim.github.io")
print(driver.title)

search = driver.find_element_by_name("")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
except:
    driver.quit()

print(main.text)
