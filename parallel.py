#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""This test assumes SAUCE_USERNAME and SAUCE_ACCESS_KEY are environment variables
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
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

#Credentials for SauceClient
test_result = sauceclient.SauceClient(SAUCE_USERNAME, SAUCE_ACCESS_KEY)
# Setting the desired_capabilities as indicated in https://saucelabs.com/platform

browsers =[{"platform": "Windows 8", "browserName": "chrome", "version": "44.0"},
           {"platform": "Windows 7", "browserName": "chrome", "version": "42.0"},
           {"platform": "OS X 10.10", "browserName": "firefox", "version": "37.0"},
           {"platform": "OS X 10.10", "browserName": "chrome", "version": "43.0"},
           {"platform": "Linux", "browserName": "chrome", "version": "43.0"},
           {"platform": "Linux", "browserName": "chrome", "version": "40.0"},
           {"platform": "Windows 8.1", "browserName": "chrome", "version": "43.0"},
           {"platform": "Windows 8.1", "browserName": "firefox", "version": "33.0"}]       

# browsers = [{"platformName": "iOS","browserName": "safari","platformVersion": "8.2","deviceName":"iPhone Simulator","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 8.2 iPhone"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.1","deviceName":"iPhone Simulator","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 8.1 iPhone"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.0","deviceName":"iPhone Simulator","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 8.0 iPhone"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.1","deviceName":"iPhone Simulator","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 7.1 iPhone"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.0","deviceName":"iPhone Simulator","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 7.0 iPhone"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "6.1","deviceName":"iPhone Simulator","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 7.0 iPhone"}]  

# browsers = [{"platformName": "iOS","browserName": "safari","platformVersion": "8.2","deviceName":"iPhone 4s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 8.2 iPhone 4s"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.1","deviceName":"iPhone 4s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.1 iPhone 4s"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.0","deviceName":"iPhone 4s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.0 iPhone 4s"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.1","deviceName":"iPhone 4s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.1 iPhone 4s"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.0","deviceName":"iPhone 4s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 4s"}
#             {"platformName": "iOS","browserName": "safari","platformVersion": "6.1","deviceName":"iPhone 4s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 4s"}]

# browsers = [{"platformName": "iOS","browserName": "safari","platformVersion": "8.2","deviceName":"iPhone 5","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 8.2 iPhone 5"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.1","deviceName":"iPhone 5","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.1 iPhone 5"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.0","deviceName":"iPhone 5","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.0 iPhone 5"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.1","deviceName":"iPhone 5","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.1 iPhone 5"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.0","deviceName":"iPhone 5","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 5"}
#             {"platformName": "iOS","browserName": "safari","platformVersion": "6.1","deviceName":"iPhone 5","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 5"}]

# browsers = [{"platformName": "iOS","browserName": "safari","platformVersion": "8.2","deviceName":"iPhone 5s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 8.2 iPhone 5s"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.1","deviceName":"iPhone 5s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.1 iPhone 5s"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.0","deviceName":"iPhone 5s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.0 iPhone 5s"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.1","deviceName":"iPhone 5s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.1 iPhone 5s"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.0","deviceName":"iPhone 5s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 5s"}
#             {"platformName": "iOS","browserName": "safari","platformVersion": "6.1","deviceName":"iPhone 5s","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 5s"}]

# browsers = [{"platformName": "iOS","browserName": "safari","platformVersion": "8.2","deviceName":"iPhone 6","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 8.2 iPhone 6"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.1","deviceName":"iPhone 6","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.1 iPhone 6"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.0","deviceName":"iPhone 6","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.0 iPhone 6"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.1","deviceName":"iPhone 6","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.1 iPhone 6"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.0","deviceName":"iPhone 6","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 6"}
#             {"platformName": "iOS","browserName": "safari","platformVersion": "6.1","deviceName":"iPhone 6","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 6"}]

# browsers = [{"platformName": "iOS","browserName": "safari","platformVersion": "8.2","deviceName":"iPhone 6 Plus","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 140 WebApp iOS 8.2 iPhone 6 Plus"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.1","deviceName":"iPhone 6 Plus","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.1 iPhone 6 Plus"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "8.0","deviceName":"iPhone 6 Plus","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 8.0 iPhone 6 Plus"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.1","deviceName":"iPhone 6 Plus","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.1 iPhone 6 Plus"},
#             {"platformName": "iOS","browserName": "safari","platformVersion": "7.0","deviceName":"iPhone 6 Plus","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 6 Plus"}
#             {"platformName": "iOS","browserName": "safari","platformVersion": "6.1","deviceName":"iPhone 6 Plus","appium-version": "1.4.0","device-orientation": "portrait", "name":"Appium 134 WebApp iOS 7.0 iPhone 6 Plus"}]                                 

#What exactly is going on here?
def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator

@on_platforms(browsers)
class AppiumMobileWebAppTest(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = self.desired_capabilities) 
        self.driver.implicitly_wait(30)    

    def test_https(self):
        self.driver.get('https://www.saucelabs.com')
        time.sleep(10)
        # title = self.driver.title
        # self.assertEquals("Sauce Labs: Selenium Testing, Mobile Testing, JS Unit Testing and More", title) 
        # time.sleep(10)
        # self.driver.get('http://www.theuselessweb.com/')
        # time.sleep(10) 
        # title = self.driver.title
        # time.sleep(10) 
        # self.assertEquals("The Useless Web", title) 
        # time.sleep(10)  


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