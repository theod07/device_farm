"""
Create a simple test that will open Appium Webdriver and visit www.google.com
"""

# iOS environment
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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

screenshot_folder = os.getenv('SCREENSHOT_PATH', '')
AWS_SLEEP_TIME = 10
LOCAL_SLEEP_TIME = 5


if os.getenv('SCREENSHOT_PATH', '') == '/tmp':
	SLEEP_TIME = LOCAL_SLEEP_TIME
else:
	SLEEP_TIME = AWS_SLEEP_TIME


class WebViewIOSTests(unittest.TestCase):

	screenshot_count = 0

	def setUp(self):
		# # set up appium
		sleep(10)
		desired_caps = {}
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '8.3'
		desired_caps['deviceName'] = 'iPhone 5'
		desired_caps['autoAcceptAlerts'] = 'True'
		# desired_caps['deviceName'] = 'iPhone Simulator'

		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(3)
		sleep(SLEEP_TIME)

	def tearDown(self):
		self.driver.quit()

	def test_0_google(self):
		screenshot_count = 0
		screenshot_folder = os.getenv('SCREENSHOT_PATH', '')

		print self.driver.__dict__
		self.driver.delete_all_cookies()
		self.driver.get('http://www.google.com')
		# self.driver.switch_to.context('WEBVIEW')

		sleep(SLEEP_TIME)

		search = self.driver.find_element_by_class_name('gsfi')
		sleep(SLEEP_TIME)
		self.driver.save_screenshot(screenshot_folder + '/0_google_{}.png'.format(screenshot_count))
		screenshot_count += 1
		search.send_keys('sauce labs')
		search.send_keys(Keys.RETURN)
		sleep(SLEEP_TIME)
		self.driver.save_screenshot(screenshot_folder + '/0_google_{}.png'.format(screenshot_count))
		screenshot_count += 1
		self.driver.switch_to.alert.accept()
		sleep(SLEEP_TIME)
		self.driver.save_screenshot(screenshot_folder + '/0_google_{}.png'.format(screenshot_count))
		screenshot_count += 1
		self.driver.switch_to.alert.accept()

		# allow the page to load
		sleep(SLEEP_TIME)
		self.driver.save_screenshot(screenshot_folder + '/0_google_{}.png'.format(screenshot_count))
		screenshot_count += 1
		self.assertEquals('sauce labs - Google Search', self.driver.title)


	def test_1_solvhealth(self):

		screenshot_count = 0
		screenshot_folder = os.getenv('SCREENSHOT_PATH', '')

		print self.driver.__dict__
		self.driver.delete_all_cookies()
		self.driver.get('http://www.solvhealth.com')
		sleep(10)
		self.driver.save_screenshot(screenshot_folder + '/1_solvhealth_{}.png'.format(screenshot_count))
		screenshot_count += 1
		self.assertEquals('Solv Health', self.driver.title)
		self.assertEquals('https://www.solvhealth.com/welcome', self.driver.current_url)


	def test_2_solvhealth(self):
		screenshot_count = 0
		screenshot_folder = os.getenv('SCREENSHOT_PATH', '')

		print self.driver.__dict__
		self.driver.delete_all_cookies()
		self.driver.get('http://www.solvhealth.com')
		sleep(10)
		self.driver.save_screenshot(screenshot_folder + '/2_solvhealth_{}.png'.format(screenshot_count))
		screenshot_count += 1


		# flip through welcome pages
		while 'welcome' in self.driver.current_url:
			self.driver.find_element_by_class_name('_34eC').click()
			sleep(10)
			self.driver.save_screenshot(screenshot_folder + '/2_solvhealth_{}.png'.format(screenshot_count))
			screenshot_count += 1

		assert 'Set my location' in self.driver.page_source



	def test_3_solvhealth(self):
		screenshot_count = 0
		screenshot_folder = os.getenv('SCREENSHOT_PATH', '')

		print self.driver.__dict__
		self.driver.delete_all_cookies()
		self.driver.get('http://www.solvhealth.com')
		sleep(10)
		self.driver.save_screenshot(screenshot_folder + '/3_solvhealth_{}.png'.format(screenshot_count))
		screenshot_count += 1

		# flip through welcome pages
		while 'welcome' in self.driver.current_url:
			self.driver.find_element_by_class_name('_34eC').click()
			sleep(10)
			self.driver.save_screenshot(screenshot_folder + '/3_solvhealth_{}.png'.format(screenshot_count))
			screenshot_count += 1

		# click "Set my location"
		# self.driver.find_element_by_css_selector('input[value="Set my location"]').click()
		self.driver.find_element_by_class_name('_3y2m').click()
		

		try:
			WebDriverWait(self.driver, 10).until(EC.alert_is_present(),
									'Timed out waiting for PA creation ' +
									'confirmation popup to appear.')

			self.driver.switch_to.alert.accept()

			self.driver.save_screenshot(screenshot_folder + '/3_solvhealth_{}.png'.format(screenshot_count))
			screenshot_count += 1

			print "alert accepted"

		except TimeoutException:
			print "no alert"


		try:
			WebDriverWait(self.driver, 10).until(EC.alert_is_present(),
									'Timed out waiting for PA creation ' +
									'confirmation popup to appear.')

			self.driver.switch_to.alert.accept()

			self.driver.save_screenshot(screenshot_folder + '/3_solvhealth_{}.png'.format(screenshot_count))
			screenshot_count += 1

			print "alert accepted"

		except TimeoutException:
			print "no alert"


		# allow location
		# self.driver.switch_to.alert.accept()
		# sleep(SLEEP_TIME)
		# self.driver.switch_to.alert.accept()
		# sleep(15)
		# location 
		self.driver.find_element_by_class_name('geosuggest__input')\
								.send_keys('Dallas, TX' + Keys.ENTER)
		
		sleep(15)
		self.driver.save_screenshot(screenshot_folder + '/solvhealth_{}.png'.format(screenshot_count))
		screenshot_count += 1
		
		# symptoms 
		self.driver.find_element_by_id('symptoms')\
								.send_keys('EXPLOSIVE DIARRHEA' + Keys.ENTER)
		
		sleep(15)
		self.driver.save_screenshot(screenshot_folder + '/solvhealth_{}.png'.format(screenshot_count))
		screenshot_count += 1
		
		# screenshot
		self.driver.save_screenshot(screenshot_folder + '/solvhealth_{}.png'.format(screenshot_count))
		screenshot_count += 1
		# 

		assert 'CommunityMed Urgent Care' in self.driver.page_source



if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(WebViewIOSTests)
	unittest.TextTestRunner(verbosity=2).run(suite)


# def test_get_url_example_outside():
# 	print('---THIS IS OUTSIDE OF THE CLASS---')
# 	driver = webdriver.Remote('http://localhost:4723/wd/hub')
# 	driver.implicitly_wait(3)

# 	search = driver.find_element_by_class_name('gsfi')
# 	search.send_keys('sauce labs')
# 	search.send_keys(Keys.RETURN)

# 	# allow the page to load
# 	sleep(1)

# 	assert 'sauce labs - Google Search' ==  driver.title

# # python
# # setup the web driver and launch the webview app.
# desired_caps = {}
# desired_caps['platformName'] = 'iOS'
# desired_caps['platformVersion'] = '8.3'
# desired_caps['deviceName'] = 'iPhone Simulator'

# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitly_wait(3) # seconds

# # Navigate to the page and interact with the elements on the guinea-pig page using id.
# # driver.get('http://saucelabs.com/test/guinea-pig')
# driver.get('https://github.com/theod07')

# screen_size = driver.get_window_size()
# width, height = screen_size['width'], screen_size['height']

# # navigate to solvhealth.com
# driver.get("http://www.solvhealth.com")
# # driver.switch_to_alert().accept()

# # enter credentials
# # alert = driver.switch_to_alert()
# # alert.send_keys('quick' + Keys.RETURN + 'solv' + Keys.RETURN)

# # page 1, click arrow
# # sleep(1.5)
# driver.find_element_by_class_name('_34eC').click()

# # page 2, click arrow
# # sleep(1.5)
# driver.find_element_by_class_name('_34eC').click()

# # click button "Set my location" 
# # sleep(1.5)
# driver.find_element_by_css_selector('input[value="Set my location"]').click()
# # elem = driver.find_element_by_class_name('_3y2m')


# # allow location
# driver.switch_to_alert().accept()
# driver.switch_to_alert().accept()

# # select text box & enter text
# # sleep(1.5)
# elem = driver.find_element_by_class_name('geosuggest__input')
# elem.send_keys('Dallas, TX' + Keys.ENTER)

# # enter symptoms
# elem = driver.find_element_by_id('symptoms')
# elem.send_keys('EXPLOSIVE DIARRHEA' + Keys.ENTER)


# # click "book"
# # sleep(5)

# start_x = width - 40
# start_y = height - 200
# end_x = 40
# end_y = height - 200


# pdb.set_trace()
# driver.save_screenshot('/tmp/appium_screenshot.png')

# action = TouchAction().press(start_x, start_y).move_to(-30, 0).release()
# driver.swipe(start_x, start_y, end_x, end_y, duration=500)

# sleep(3)
# driver.find_element_by_class_name('_2ZwF').click()
# sleep(3)
# driver.find_element_by_class_name('_2ZwF').click()
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