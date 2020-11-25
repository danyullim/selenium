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

link = driver.find_element_by_css_selector("area")
link.click()

email = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input')
email.click()