from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Locating path to directory of the chromedriver.exe file
PATH = "/Users/danyullim/Github/selenium/chromedriver"
# Set up the driver using chrome
driver = webdriver.Chrome(PATH)

# Accessing church webpage
driver.get("http://seoulbaptist.org/")
print(driver.title)

link = driver.find_element_by_css_selector("area.rect")
link.click()
