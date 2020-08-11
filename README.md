# eBay Scraper
Source: https://github.com/fgscivittaro/ebay
A tool for scraping information from eBay product pages.


Run main.py

Outputs to file ebay_scraper_beautifulsoup/data.csv
There is an option to overwrite the existing file or append to it.

Uses BeautifulSoup to scrape buyer, seller, and product information from eBay product pages. Also includes capabilities for collecting all the links from eBay's featured collections and scraping each of those links. Lastly, includes several options for writing and appending the collected data to files to store and use for data analyses.

pip install requitements
wheel
request
regex
lxml
schedule
beautifulsou4