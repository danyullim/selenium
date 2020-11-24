from selenium import webdriver
# from selenium.webdriver.common.key import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Locating path to directory of the chromedriver.exe file
PATH = "/Users/danyullim/Github/selenium/chromedriver"
# Set up the driver using chrome
driver = webdriver.Chrome(PATH)

# Accessing church webpage
driver.get("http://seoulbaptist.org/")
print(driver.title)

search = driver.find_element_by_name("covid_01")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
except:
    driver.quit()

print(main.text)
