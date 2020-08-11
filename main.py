import bs4
import schedule
from schedule import every
from collect_data import *
from collect_links import *
from collect_sales_data import *
from combined import *
from sale import *
from scrape_page import *
import csv


mode = input("Do you want to append (a) data file or write (w) over existing file? (a/w): ")
if mode == 'w':
	check = input("Are you sure you want to overwrite the data file? (y/n): ")
	if check == 'n':
		mode = 'a'
		print ("mode = a")
	else:
		print ("mode = w") 
file = open('ebay_scraper_beautifulsoup/data.csv', mode)
writer = csv.writer(file, lineterminator = '\n')

if mode == 'w':
    writer.writerow(['Items Scraped','Keyword','Product','EPID','Brand','Category','Seller','Items Sold','Condition',
    'Location','Price','Image','Payment','URL','UPC','EAN','MPN','ISBN'])

keyword=input("Enter a seach key: ")
links = collect_search_links(keyword) #collect list of URLS based off of keywords and pages searched

#Output search keywords to text file to keep track.
txt = open("ebay_scraper_beautifulsoup/keywords.txt","a+")
txt.writelines("\n" + keyword + ":" + str(len(links)))
txt.close()

#print(links[0])

Count = 0
for i in links:
    Count += 1
    soup = get_soup(i, num_retries = 1)
    Product = get_title(soup)
    EPID = get_item_number(soup)
    Brand = get_brand(soup)
    listCategory = get_category(soup)
    category = str(listCategory).strip('[]').replace("'","")
    Seller = get_username(soup)
    Items_Sold = get_items_sold(soup)
    Condition = get_condition(soup)
    Location = get_item_location(soup)
    Price = get_price(soup)
    Image = get_image(soup)
    listPayment = get_payments(soup)
    payment = str(listPayment).strip('[]')
    URL = i
    UPC = get_upc(soup)
    EAN = get_ean(soup)
    MPN = get_mpn(soup)
    ISBN = get_isbn(soup)

    writer.writerow([Count,keyword,Product,EPID,Brand,category,Seller,Items_Sold,Condition,Location,
    Price,Image,payment,URL,UPC,EAN,MPN,ISBN])


file.close()