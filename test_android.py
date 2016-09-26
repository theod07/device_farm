"""
Create a simple test that will open Appium Webdriver and visit www.google.com
"""

# Android environment
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import unittest
import os

import ipdb as pdb

PLATFORM_VERSION = '4.4'

class AndroidWebViewTests(unittest.TestCase):

	def setUp(self):
		# # set up appium
		desired_caps = {}
		desired_caps['browserName'] = 'Chrome'
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = PLATFORM_VERSION
		desired_caps['deviceName'] = 'Android Emulator'

		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		# self.driver = webdriver.Remote('http://localhost:4723/wd/hub')
		self.driver.implicitly_wait(3)
		sleep(15)

	def tearDown(self):
		self.driver.quit()


	def test_get_url_example_inside(self):
		print self.driver.__dict__
		self.driver.delete_all_cookies()
		self.driver.get('http://www.google.com')
		# self.driver.switch_to.context('WEBVIEW')
		sleep(15)
		search = self.driver.find_element_by_class_name('gsfi')
		sleep(15)
		search.send_keys('sauce labs')
		search.send_keys(Keys.RETURN)
		sleep(15)
		self.driver.switch_to.alert.accept()
		sleep(15)
		self.driver.switch_to.alert.accept()

		# allow the page to load
		sleep(15)

		self.assertEquals('sauce labs - Google Search', self.driver.title)

	def test_get_solvhealth(self):

		print self.driver.__dict__
		self.driver.delete_all_cookies()
		self.driver.get('http://www.solvhealth.com')
		sleep(15)
		# flip through welcome pages
		self.driver.find_element_by_class_name('_34eC').click()
		sleep(15)
		self.driver.find_element_by_class_name('_34eC').click()
		sleep(15)
		# click "Set my location"
		# self.driver.find_element_by_css_selector('input[value="Set my location"]').click()
		self.driver.find_element_by_class_name('_3y2m').click()
		sleep(15)
		# allow location
		self.driver.switch_to.alert.accept()
		sleep(15)
		self.driver.switch_to.alert.accept()
		sleep(15)
		# location 
		self.driver.find_element_by_class_name('geosuggest__input')\
								.send_keys('Dallas, TX' + Keys.ENTER)
		sleep(15)
		# symptoms 
		self.driver.find_element_by_id('symptoms')\
								.send_keys('EXPLOSIVE DIARRHEA' + Keys.ENTER)
		sleep(15)
		# screenshot
		self.driver.save_screenshot('/tmp/test_screenshot.png')
		# 
		assert 'CommunityMed Urgent Care' in self.driver.page_source



if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
	unittest.TextTestRunner(verbosity=2).run(suite)