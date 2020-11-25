from selenium import webdriver
import time

# Locating path to directory of the chromedriver.exe file
PATH = "/Users/danyullim/Github/selenium/chromedriver"
# Set up the driver using chrome
web = webdriver.Chrome(PATH)
# Accessing church's homepage
web.get('desiredURL')

# Allow the form to load 
time.sleep(2)

##### FIRST PAGE – EMAIL SECTION #####
# Input this email
emailInput = input("What is your email you want to input: \n")
# Find element with the XPATH
email = web.find_element_by_css_selector('inspect elements and copy the css selector and paste it here')
# Fill in with the emailInput
email.send_keys(emailInput)
# Locate Submit Button
firstNext = web.find_element_by_css_selector('inspect elements and copy the css selector and paste it here')
# Click Submit Button
firstNext.click()

# Allow the form to load 
time.sleep(2)

##### SECOND PAGE – NUMBER OF ATENDEES #####
# Locate the participants button
participantsButton = web.find_element_by_css_selector('inspect elements and copy the css selector and paste it here')
participantsButton.click()
# Locate next button
secondNext = web.find_element_by_css_selector('inspect elements and copy the css selector and paste it here')
secondNext.click()

# Allow the form to load 
time.sleep(2)

##### THIRD PAGE - NAME OF ATENDEES #####
# The names needed to input
name1 = "What is your name that you want to input: \n"
name2 = "Who is your +1?: \n"
# Locate and type the first atendee box
name1Box = web.find_element_by_css_selector('inspect elements and copy the css selector and paste it here')
name1Box.send_keys(name1)
# Locate and type the second atendee box
name2Box = web.find_element_by_css_selector('inspect elements and copy the css selector and paste it here')
name2Box.send_keys(name2)
# Locate the submit button
lastNext = web.find_element_by_xpath('inspect elements and copy the XPATH and paste it here')
lastNext.click()

# Allow the form to load 
time.sleep(2)

##### FOURTH PAGE – Service Time? #####
# Locate 1st Service Button
serviceButton = web.find_element_by_css_selector('inspect elements and copy the css selector and paste it here')
serviceButton.click()
# Locate the submit button
finalButton = web.find_element_by_css_selector('inspect elements and copy the css selector and paste it here')
finalButton.click()








