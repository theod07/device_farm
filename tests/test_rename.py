"""
Create a simple test that will open Appium Webdriver and visit www.google.com
"""

# iOS environment
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest
import os

import ipdb as pdb

"""
*** WebDriverException: Message: An unknown server-side error occurred 
while processing the command. Original error: Could not find a device to 
launch. You requested 'iPhone 5s (7.1 Simulator)', but the available 
devices were: [
		"Resizable iPad (8.3 Simulator) [BD70449B-F8DD-4E8B-B38E-3595F28E54F0]",
		"Resizable iPhone (8.3 Simulator) [17AF2275-82E8-4B30-AE28-C36D5725B10F]",
		"iPad 2 (8.3 Simulator) [2E8FA7B9-F32A-44B2-9CA5-0A764A47A4CD]",
		"iPad Air (8.3 Simulator) [F1FCE631-4D10-49BF-85EF-FAECB8C7BCC9]",
		"iPad Retina (8.3 Simulator) [0FF4459F-D39B-40CD-9F84-44D09F226A7D]",
		"iPhone 4s (8.3 Simulator) [B359392B-5B4D-4DFD-B839-B675F6BB4440]",
		"iPhone 5 (8.3 Simulator) [EDDCBDC8-962D-442B-B68B-70DB2712DB22]",
		"iPhone 5s (8.3 Simulator) [8E3B0FF9-DF1E-417C-B0BA-D1755EF614E4]",
		"iPhone 6 (8.3 Simulator) [452532BA-AD63-4312-8288-C107242186A3]",
		"iPhone 6 Plus (8.3 Simulator) [163386AB-E6BE-4DC2-96F0-A9494E34427D]"
	]
"""

class WebViewIOSTests(unittest.TestCase):

	def setUp(self):
		# set up appium
		desired_caps = {}
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '8.3'
		desired_caps['deviceName'] = 'iPhone Simulator'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(3)

	def tearDown(self):
		self.driver.quit()


	def example_test_get_url(self):
		self.driver.get('http://www.google.com')
		# self.driver.switch_to.context('WEBVIEW')

		search = self.driver.find_element_by_class_name('gsfi')
		search.send_keys('sauce labs')
		search.send_keys(Keys.RETURN)

		# allow the page to load
		sleep(1)

		self.assertEquals('sauce labs - Google Search', self.driver.title)



# # python
# # setup the web driver and launch the webview app.
# desired_caps = {}
# desired_caps['platformName'] = 'iOS'
# desired_caps['platformVersion'] = '8.3'
# desired_caps['deviceName'] = 'iPhone Simulator'
# pdb.set_trace()

# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitly_wait(3) # seconds

# # Navigate to the page and interact with the elements on the guinea-pig page using id.
# driver.get('http://saucelabs.com/test/guinea-pig')

# # navigate to solvhealth.com
# driver.get("http://www.solvhealth.com")
# driver.switch_to_alert().accept()

# # enter credentials
# alert = driver.switch_to_alert()
# alert.send_keys('quick' + Keys.RETURN + 'solv' + Keys.RETURN)

# # page 1, click arrow
# # sleep(1.5)
# elem = driver.find_element_by_class_name('_34eC')
# elem.click()

# # page 2, click arrow
# # sleep(1.5)
# elem = driver.find_element_by_class_name('_34eC')
# elem.click()

# # click button "Set my location" 
# # sleep(1.5)
# elem = driver.find_element_by_css_selector('input[value="Set my location"]')
# # elem = driver.find_element_by_class_name('_3y2m')
# elem.click()


# # allow location
# alert = driver.switch_to_alert()
# alert.accept()
# alert = driver.switch_to_alert()
# alert.accept()

# # select text box & enter text
# # sleep(1.5)
# elem = driver.find_element_by_class_name('geosuggest__input')
# elem.send_keys('Dallas, TX' + Keys.ENTER)

# # enter symptoms
# elem = driver.find_element_by_id('symptoms')
# elem.send_keys('back pain' + Keys.ENTER)


# # click "book"
# # sleep(5)
# driver.find_element_by_link_text('Book').click()

# # click "change"

# # click "next"
# # sleep(1.5)
# driver.find_element_by_class_name('_2u1X').click()

# # fill form
# elem = driver.find_element_by_id('firstName')
# elem.send_keys('theo')
# elem = driver.find_element_by_id('lastName')
# elem.send_keys('do')
# elem = driver.find_element_by_id('email')
# elem.send_keys('theo@solvhealth.com')
# elem = driver.find_element_by_id('phone')
# elem.send_keys('7148236827')
# elem = driver.find_element_by_id('notes')
# elem.send_keys('testing')
# # sleep(1.5)
# elem = driver.find_element_by_class_name('_1RVK')
# elem.click()

# # flow branches here for insurance
# # No. I know I'm covered or will check at clinic
# elem = driver.find_element_by_class_name('_2fkl')
# elem.click()

# # click finalize
# # sleep(1.5)
# elem = driver.find_element_by_class_name('_1lJn')
# elem.click()

# pdb.set_trace()

# # div = driver.find_element_by_id('i_am_an_id')
# # check the text retrieved matches expected value
# # assertEqual('I am a div', div.text)

# # populate the comments field by id
# # driver.find_element_by_id('comments').send_keys('My comment')

# # close the driver
# driver.quit()

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(WebViewIOSTests)
	unittest.TextTestRunner(verbosity=2).run(suite)