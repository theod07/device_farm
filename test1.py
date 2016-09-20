"""
Create a simple test that will open Appium Webdriver and visit www.google.com
"""

# iOS environment
from appium import webdriver
from unittest.TestCase import assertEqual
import time
import os

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
driver.get('http://saucelabs.com/test/guinea-pig');
div = driver.find_element_by_id('i_am_an_id')
# check the text retrieved matches expected value
assertEqual('I am a div', div.text)

# populate the comments field by id
driver.find_element_by_id('comments').send_keys('My comment')

# close the driver
driver.quit()

