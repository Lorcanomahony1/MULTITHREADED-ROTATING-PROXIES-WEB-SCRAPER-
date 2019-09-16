from proxy_requests import ProxyRequests
from proxy_requests import ProxyRequests, ProxyRequestsBasicAuth 
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








list_of_links2 = []

h = {"User-Agent": "NCSA Mosaic/3.0 (Windows 95)"}
r = ProxyRequests("http://toscrape.com/")
r.set_headers(h)
r.get_with_headers()
page = r.text
page_soup = soup(page, "html.parser")
divs = page_soup.findAll("div")
list_of_links2.append(divs)


print(list_of_links2)