import pandas as pd    
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




url = "http://www.galway-ireland.ie/business-galway.htm"
list_of_links = []
list_of_emails = []
substrings = ["Dancing","Childcare","Gardai","Lakes"]


response = requests.get(url)
page = response.text
page_soup = soup(page, "html.parser")

divs = page_soup.findAll("a")

for div in divs:

	list_of_links.append(div['href'])

	for sub in substrings:
		if div.getText() == sub:
			list_of_links.remove(div['href'])
			
df = pd.DataFrame(list_of_links)
df.to_csv('Emails.csv', index=False)


