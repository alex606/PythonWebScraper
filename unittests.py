import unittest
from BaseDriver import ChromeDriver

class UnitTests(unittest.TestCase):

    def goToGoogleHomePage(self):
        chromeDriver = ChromeDriver()
        chromeDriver.navigateToUrl("http://www.google.com")


if __name__ == '__main__':
    unittest.main()