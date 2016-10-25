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
import requests
from bs4 import BeautifulSoup

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

SCREENSHOT_FOLDER = os.getenv('SCREENSHOT_PATH', '')
AWS_SLEEP_TIME = 10
LOCAL_SLEEP_TIME = 5

SOLVHEALTH_URL = 'http://www.solvhealth.com'
STAGE_SOLVHEALTH_URL = 'https://stage.solvhealth.com'
QUICKCARE_WELCOME_URL = 'https://facility-manage-stage.herokuapp.com/welcome/g1a41z'
KIOSK_URL = 'https://facility-manage-stage.herokuapp.com/book/g1a41z'
QUICKCARE_DALLAS_URL = 'https://stage.solvhealth.com/-g1a41z'
WAITLIST_URL = 'https://stage.solvhealth.com/b'
DAPI_QA_HOST = 'https://facility-dapi-qa.herokuapp.com'
STAGE_QUICKCARE_WAITLIST = 'https://stage.solvhealth.com/l/100000'
STAGE_OUTSIDE_SERVICE_AREA = 'https://stage.solvhealth.com/outsideServiceArea'

if SCREENSHOT_FOLDER == '/tmp':
    SLEEP_TIME = LOCAL_SLEEP_TIME
else:
    SLEEP_TIME = AWS_SLEEP_TIME


class WebViewIOSTests(unittest.TestCase):

    def setUp(self):
        # # set up appium
        sleep(10)
        desired_caps = {}

        # iOS Capabilities
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '8.3'
        desired_caps['deviceName'] = 'iPhone 5'

        # for Android Capabilities
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4'
        # desired_caps['deviceName'] = 'Android Emulator'

        # desired_caps['autoAcceptAlerts'] = 'True'
        desired_caps['newCommandTimeout'] = 0
        # desired_caps['deviceName'] = 'iPhone Simulator'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        # sleep(2
        self.driver.implicitly_wait(30)
        # sleep(2)
        self.driver.delete_all_cookies()
        sleep(10)

    def tearDown(self):
        self.driver.quit()


    def save_screen(self, testname, screenshot_count):

        fname = '{}_{}'.format(testname, screenshot_count)

        # with open(SCREENSHOT_FOLDER + '/{}.html'.format(fname), 'w') as f:
        #     f.write(self.driver.page_source)

        self.driver.save_screenshot(SCREENSHOT_FOLDER + '/{}.png'.format(fname))

        new_count = screenshot_count + 1
        return new_count


    def t_1_solvhealth(self):
        TEST_NAME = '1_solvhealth'
        screenshot_count = 0

        print self.driver.__dict__
        print self.driver.get_cookies()

        self.driver.get(SOLVHEALTH_URL)

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # landing page does not always route directly to www.solvhealth.com/welcome
        # this happens when device has previously seen the landing page
        if '/welcome' in self.driver.current_url:
            # click 'Next' button
            self.driver.find_element_by_class_name('eNzk').click()

            screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

            # click 'Next' button
            self.driver.find_element_by_class_name('_382N').click()

            screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_id('symptoms').send_keys('carpal tunnel')
        sleep(1)
        self.driver.find_element_by_class_name('_25eB').click()

        # wait for search results to load
        sleep(10)

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # assert 'Want another option?' in self.driver.page_source

        self.driver.find_element_by_class_name('OML6').click()
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
        self.driver.find_element_by_class_name('_2u1X').click()
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_id('firstName').send_keys('Theo')
        self.driver.find_element_by_id('lastName').send_keys('Do')
        self.driver.find_element_by_id('birthDate').send_keys('06/03/1989')
        self.driver.find_element_by_id('phone').send_keys('7148236827')
        self.driver.find_element_by_id('email').send_keys('theo@solvhealth.com')
        self.driver.find_element_by_id('notes').send_keys('testing')
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_1RVK').click()

        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
        self.driver.find_element_by_class_name('QgRI').click()
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        assert 'Finalize' in self.driver.page_source

    def test_2_kiosk_badnumber(self):
        TEST_NAME = '2_kiosk_badnumber'
        screenshot_count = 0

        self.driver.get(QUICKCARE_WELCOME_URL)
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_1Xy-').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_id('phone').send_keys('4150000000')
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_3L9J').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        assert 'Uh-oh!' in self.driver.page_source

        self.driver.find_element_by_id('phone').send_keys('4150000000')
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_3L9J').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        assert "Third time's a charm." in self.driver.page_source

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_3L9J').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        assert "Seems like there's a problem" in self.driver.page_source

        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)


    def t_2_kiosk(self):
        TEST_NAME = '2_kiosk'
        screenshot_count = 0

        self.driver.get(KIOSK_URL)
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_id('firstName').send_keys('Theo')
        self.driver.find_element_by_id('lastName').send_keys('Do')
        self.driver.find_element_by_id('birthDate').send_keys('06/03/1989')
        self.driver.find_element_by_id('phone').send_keys('7148236827')
        self.driver.find_element_by_id('reason').send_keys('carpal tunnel')

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_324y').click()
        sleep(3)

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        while self.driver.title == 'Sign in':

            screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
            sleep(.2)

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        assert 'Success' in self.driver.title


    def test_4_waitlist(self):
        TEST_NAME = '4_waitlist'
        screenshot_count = 0

        self.driver.get(STAGE_QUICKCARE_WAITLIST)
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
        assert 'Live Waitlist by' in self.driver.page_source



    def test_3_solvhealth(self):
        TEST_NAME = '3_solvhealth'
        screenshot_count = 0

        self.driver.get(STAGE_SOLVHEALTH_URL)
        sleep(3)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # landing page does not always route directly to www.solvhealth.com/welcome
        # this happens when device has previously seen the landing page
        if '/welcome' in self.driver.current_url:
            # click 'Next' button
            self.driver.find_element_by_class_name('eNzk').click()
            sleep(1)
            screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # enter symptoms
        self.driver.find_element_by_id('symptoms').send_keys('carpal tunnel')
        sleep(3)
        self.driver.find_element_by_class_name('_25eB').click()

        accept system & browser location notifications
        try:
            for alert in ['first', 'second']:
                WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                                    'Timed out waiting for PA creation ' +
                                                    'confirmation popup to appear.')

                self.driver.switch_to.alert.accept()
        except:
            pass
        self.driver.get(STAGE_OUTSIDE_SERVICE_AREA)


        # wait for search results to load
        sleep(10)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # self.driver.get(STAGE_OUTSIDE_SERVICE_AREA)

        # Currently serving Dallas-Fort Worth.
        # Same-day appointments coming soon near you!
        # Click Dallas-Fort Worth
        self.driver.find_element_by_class_name('_1u5O').click()
        sleep(2)

        # click adult/kid filter
        self.driver.find_elements_by_class_name('_20Mk')[0]\
                    .find_element_by_tag_name('a').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
        assert 'For kids and adults' in self.driver.page_source

        # click chevron to go back to SRP
        self.driver.find_element_by_class_name('_1IRY').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # click location filter
        self.driver.find_elements_by_class_name('_20Mk')[1]\
                    .find_element_by_tag_name('a').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
        assert 'City or ZIP code' in self.driver.page_source


        # go directly to Stage QuickCare CDP
        self.driver.get(QUICKCARE_DALLAS_URL)
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_2jtT').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_2u1X').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_id('firstName').send_keys('Theo')
        self.driver.find_element_by_id('lastName').send_keys('Do')
        self.driver.find_element_by_id('birthDate').send_keys('06/03/1989')
        self.driver.find_element_by_id('phone').send_keys('7148236827')
        self.driver.find_element_by_id('email').send_keys('theo@solvhealth.com')
        self.driver.find_element_by_id('notes').send_keys('testing')
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_1RVK').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('QgRI').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_1lJn').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        book_id = self.driver.find_element_by_class_name('_3Gu-').text.split(' # ')[-1]

        if 'See my place in line' in self.driver.page_source:
            self.driver.find_element_by_link_text('See my place in line').click()
            sleep(1)
            screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        #
        DAPI_BOOKING_URL = DAPI_QA_HOST + '/v1/bookings/' + book_id
        r = requests.get(DAPI_BOOKING_URL)
        print book_id
        print r.json().get('data', {}).get('status')
        assert r.json().get('data', {}).get('status', {'Not found. Full response ' : r.json()}) in ['reserved', 'pending']

        self.driver.get(QUICKCARE_WELCOME_URL)
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # "I booked online" button
        self.driver.find_element_by_class_name('_1Xy-').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # enter phone number
        self.driver.find_element_by_id('phone').send_keys('7148236827')
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_3L9J').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # make sure that the booking exists in with phone number

        # "Not me. Go back."
        self.driver.find_element_by_class_name('_1Xm-').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
        # leads back to welcome page
        # "I booked online" button
        self.driver.find_element_by_class_name('_1Xy-').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # enter phone number
        self.driver.find_element_by_id('phone').send_keys('7148236827')
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_3L9J').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        # "Yes, that's me"
        self.driver.find_element_by_class_name('_2O4n').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        while self.driver.title == 'Sign in':

            screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
            sleep(.2)

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        assert 'Success' in self.driver.title

        self.driver.get(QUICKCARE_WELCOME_URL)
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('fd5g').click()
        sleep(1)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_id('firstName').send_keys('Theo')
        self.driver.find_element_by_id('lastName').send_keys('Do')
        self.driver.find_element_by_id('birthDate').send_keys('06/03/1989')
        self.driver.find_element_by_id('phone').send_keys('7148236827')
        self.driver.find_element_by_id('reason').send_keys('carpal tunnel')

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        self.driver.find_element_by_class_name('_324y').click()
        sleep(3)
        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        while self.driver.title == 'Sign in':
            screenshot_count = self.save_screen(TEST_NAME, screenshot_count)
            sleep(.2)

        screenshot_count = self.save_screen(TEST_NAME, screenshot_count)

        assert 'Success' in self.driver.title


        # change booking status to 'cancelled'
        r = requests.patch(DAPI_BOOKING_URL, data={'status':'cancelled'})
        r = requests.get(DAPI_BOOKING_URL)
        assert r.json().get('data', {}).get('status', {'Not found. Full response ': r.json()}) == 'cancelled'



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebViewIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
