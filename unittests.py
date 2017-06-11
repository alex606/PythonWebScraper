import unittest
from BaseDriver import ChromeDriver
from BeautifulSoupScrapper import BeautifulSoupScrapper

class UnitTests(unittest.TestCase):

    def scrapeStockPrices(self):
        soupScrapper = BeautifulSoupScrapper()
        soupScrapper.scrapeSnp500()

    def goToGoogleHomePage(self):
        chromeDriver = ChromeDriver()
        chromeDriver.navigateToUrl("http://www.google.com")

    def scrapeWikipediaLinks(self):
        chromeDriver = ChromeDriver()
        chromeDriver.navigateToUrl("http://www.wikipedia.org/")
        we = chromeDriver.browser.find_element_by_css_selector("#js-link-box-en > strong")
        we.click();

        we = chromeDriver.browser.find_element_by_css_selector("#n-randompage > a")
        we.click()

if __name__ == '__main__':
    unittest.main()