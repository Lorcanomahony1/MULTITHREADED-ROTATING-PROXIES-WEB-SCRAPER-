

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
import random
import threading
import math
from threading import Thread




list_of_links = []
list_of_emails = []



url = "https://lorcanomahony1.github.io/Bolo-Website/index.html"
my_user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"}
response = requests.get(url, headers=my_user_agent)
page = response.text
page_soup = soup(page, "html.parser")

divs = page_soup.findAll("a")

for div in divs:

    list_of_links.append("https://lorcanomahony1.github.io/Bolo-Website/" + div['href'])


print(list_of_links)