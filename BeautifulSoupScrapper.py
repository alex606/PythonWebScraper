import unittest
import urllib
import urllib.request
import csv
from datetime import datetime
from bs4 import BeautifulSoup


class BeautifulSoupScrapper(unittest.TestCase):

    def scrapeSnp500(self):

        data = []

        quote_pages = [
            'http://www.bloomberg.com/quote/SPX:IND',
            'http://www.bloomberg.com/quote/CCMP:IND',
            'https://www.bloomberg.com/quote/MSFT:US',
            'https://www.bloomberg.com/quote/BRK/B:US'
        ]

        for quote_page in quote_pages:

            page = urllib.request.urlopen(quote_page)
            soup = BeautifulSoup(page,'html.parser')

            name_box = soup.find('h1', attrs= {'class':'name'})
            name = name_box.text.strip()

            price_box = soup.find('div', attrs={'class': 'price'})
            price = price_box.text

            data.append((name, price))

        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            for name, price in data:
                writer.writerow([name, price, datetime.now()])

def main():
    unittest.main()
if __name__ == '__main__':
    main()