
from selenium import webdriver
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import time
import re
from random import randint
from time import sleep
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
import pandas as pd  
import random
import requests



proxy = {"http" "103.216.82.213:6667"} 

list_of_links = []
list_of_emails = []
substrings = ["Dancing","Childcare","Gardai","Lakes"]


url = "http://www.galway-ireland.ie/business-galway.htm"
my_user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"}
response = requests.get(url, headers=my_user_agent)
page = response.text
page_soup = soup(page, "html.parser")

divs = page_soup.findAll("a")

for div in divs:

	list_of_links.append(div['href'])

	for sub in substrings:
		if div.getText() == sub:
			list_of_links.remove(div['href'])




for link in list_of_links:

	url = link
	response = requests.get(url)
	page = response.text
	page_soup = soup(page, "html.parser")

	divtext = page_soup.getText()

	emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", divtext)

	list_of_emails.append(emails)
	print(emails)

	sleep(randint(1,5))


df = pd.DataFrame(list_of_emails)
df.to_csv('Emails.csv', index=False)




	















