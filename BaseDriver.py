import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BaseDriver:

    def initDriver(self):
        chromeDriver= "C:\SeleniumDrivers\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromeDriver
        self.browser = webdriver.Chrome(chromeDriver)
        #self.browser.get("http://www.google.com")

    def navigateToUrl(self, url):
        self.browser.get(url)