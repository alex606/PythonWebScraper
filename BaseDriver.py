import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BaseDriver:
    def __init__(self, driverPath, property):
        self.driverPath = driverPath
        self.property = property
        os.environ[property] = driverPath
        self.browser = webdriver.Chrome(driverPath)

    def navigateToUrl(self, url):
        self.browser.get(url)


class ChromeDriver(BaseDriver):
    def __init__(self):
        super().__init__("C:\SeleniumDrivers\chromedriver.exe", "webdriver.chrome.driver")
