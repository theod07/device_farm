"""
Create a simple test that will open Appium Webdriver and visit www.google.com
"""

# iOS environment
# from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from unittest.Testcase import assertEqual
import time
import os
import ipdb as pdb

# class LoginTests(unittest.TestCase):
#     def setUp(self):
#         desired_caps = {}
#         # desired_caps['appium-version'] = '1.0'
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '5.1'
#         # desired_caps['app'] = os.path.abspath('/Users/mkim/Documents/AUT/app/build/outputs/apk/app-debug-unaligned.apk')
 
#         self.wd = webdriver.Remote('www.google.com', desired_caps)
#         self.wd.implicitly_wait(60)

{
  'platformName': 'iOS',
  'platformVersion': '7.1',
  'browserName': 'Safari',
  'deviceName': 'iPhone Simulator'
}

# python
# setup the web driver and launch the webview app.
capabilities = { 'browserName': 'Safari' }
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

# Navigate to the page and interact with the elements on the guinea-pig page using id.
driver.get('http://saucelabs.com/test/guinea-pig')

# navigate to solvhealth.com
driver.get("http://www.solvhealth.com")
driver.switch_to_alert().accept()

# enter credentials
alert = driver.switch_to_alert()
alert.send_keys('quick' + Keys.RETURN + 'solv' + Keys.RETURN)

# page 1, click arrow
time.sleep(1.5)
elem = driver.find_element_by_class_name('_34eC')
elem.click()

# page 2, click arrow
time.sleep(1.5)
elem = driver.find_element_by_class_name('_34eC')
elem.click()

# click button "Set my location" 
time.sleep(1.5)
elem = driver.find_element_by_css_selector('input[value="Set my location"]')
# elem = driver.find_element_by_class_name('_3y2m')
elem.click()


# allow location
alert = driver.switch_to_alert()
alert.accept()
alert = driver.switch_to_alert()
alert.accept()

# select text box & enter text
time.sleep(1.5)
elem = driver.find_element_by_class_name('geosuggest__input')
elem.send_keys('Dallas, TX' + Keys.ENTER)

# enter symptoms
elem = driver.find_element_by_id('symptoms')
elem.send_keys('back pain' + Keys.ENTER)


# click "book"
time.sleep(5)
driver.find_element_by_link_text('Book').click()

# click "change"

# click "next"
time.sleep(1.5)
driver.find_element_by_class_name('_2u1X').click()

# fill form
elem = driver.find_element_by_id('firstName')
elem.send_keys('theo')
elem = driver.find_element_by_id('lastName')
elem.send_keys('do')
elem = driver.find_element_by_id('email')
elem.send_keys('theo@solvhealth.com')
elem = driver.find_element_by_id('phone')
elem.send_keys('7148236827')
elem = driver.find_element_by_id('notes')
elem.send_keys('testing')
time.sleep(1.5)
elem = driver.find_element_by_class_name('_1RVK')
elem.click()

# flow branches here for insurance
# No. I know I'm covered or will check at clinic
elem = driver.find_element_by_class_name('_2fkl')
elem.click()

# click finalize
time.sleep(1.5)
elem = driver.find_element_by_class_name('_1lJn')
elem.click()

pdb.set_trace()

# div = driver.find_element_by_id('i_am_an_id')
# check the text retrieved matches expected value
# assertEqual('I am a div', div.text)

# populate the comments field by id
# driver.find_element_by_id('comments').send_keys('My comment')

# close the driver
driver.quit()

