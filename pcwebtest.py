#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""This test assumes SAUCE_USER_NAME and SAUCE_API_KEY are environment variables
set to your Sauce Labs username and access key."""

#importing the unittest python module that provides classes for test automation. 
import unittest 
#importing the time python module that supports time related functions.
import time
#importing the os module which provides a portable way of using operating system dependent functionality.
import os
#importing the sys module which provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys
#importing the Appium Python bindings for Selenium Webdriver from the python Appium module.
from appium import webdriver
#importing the Selenium Python bindings for Selenium Webdriver from the python Selenium module.
from selenium import webdriver
#importing  the sauceclient which is a Python client library, used for accessing the Sauce Labs REST API to retrieve and update information about resources. 
import sauceclient
import json
import new

#Retreiving enviroment variables
SAUCE_USER_NAME = os.environ.get('SAUCE_USER_NAME')
SAUCE_API_KEY = os.environ.get('SAUCE_API_KEY')

#Credentials for SauceClient
test_result = sauceclient.SauceClient(SAUCE_USER_NAME, SAUCE_API_KEY)

class AppiumMobileWebAppTest(unittest.TestCase):
    def setUp(self):

        self.desired_capabilities = {}
        self.desired_capabilities['name'] = 'Chrome 44 Test'
        # self.desired_capabilities['platformName'] = 'Android'
        self.desired_capabilities['platform'] = 'Windows 8.1'
        self.desired_capabilities['browserName'] = 'chrome'
        # self.desired_capabilities['deviceName'] = 'iPad Air'
        # # self.desired_capabilities['appiumVersion'] = '1.3.7'
        # # self.desired_capabilities['automationName'] = "Selendroid"
        # self.desired_capabilities['deviceOrientation'] = 'portrait'
        self.desired_capabilities['version'] = "44"
        # self.desired_capabilities['chromedriverVersion'] = "2.16"
        # self.desired_capabilities['screenResolution'] = "1600x1200"
        # self.desired_capabilities['app'] = "http://screendymac.cloudapp.net/com.screendy.previewer[1].apk"
        # self.desired_capabilities['app'] = 'sauce-storage:jhon2_file.apk'

        self.driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USER_NAME + ':' + SAUCE_API_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = self.desired_capabilities) 
        # self.driver.implicitly_wait(30)    

    def test_https(self):
        self.driver.get('http://www.google.com')
        # title = self.driver.title
        # self.assertEquals("Sauce Labs: Selenium Testing, Mobile Testing, JS Unit Testing and More", title) 
        # time.sleep(10)
        # self.driver.get('http://www.theuselessweb.com/')
        # title = self.driver.title
        # self.assertEquals("The Useless Web", title) 
        time.sleep(10)  

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        #using the sauce client to set the pass or fail flags for this test according to the assertions results.
        try:
            if sys.exc_info() == (None, None, None):
                test_result.jobs.update_job(self.driver.session_id, passed=True)
            else:
                test_result.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

if __name__ == '__main__':
        unittest.main()

