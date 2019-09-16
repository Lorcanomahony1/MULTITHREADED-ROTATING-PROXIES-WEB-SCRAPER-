

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




link_list = ['https://lorcanomahony1.github.io/Bolo-Website/index.html', 'https://lorcanomahony1.github.io/Bolo-Website/', 'https://lorcanomahony1.github.io/Bolo-Website/Development.html', 'https://lorcanomahony1.github.io/Bolo-Website/', 'https://lorcanomahony1.github.io/Bolo-Website/', 'https://lorcanomahony1.github.io/Bolo-Website/', 'https://lorcanomahony1.github.io/Bolo-Website/index.html', 'https://lorcanomahony1.github.io/Bolo-Website/Development.html', 'https://lorcanomahony1.github.io/Bolo-Website/Marketing.html', 'https://lorcanomahony1.github.io/Bolo-Website/Management.html', 'https://lorcanomahony1.github.io/Bolo-Website/Data.html', 'https://lorcanomahony1.github.io/Bolo-Website/Sales.html', 'https://lorcanomahony1.github.io/Bolo-Website/Development.html', 'https://lorcanomahony1.github.io/Bolo-Website/Development.html', 'https://lorcanomahony1.github.io/Bolo-Website/Marketing.html', 'https://lorcanomahony1.github.io/Bolo-Website/Marketing.html', 'https://lorcanomahony1.github.io/Bolo-Website/Management.html', 'https://lorcanomahony1.github.io/Bolo-Website/Management.html', 'https://lorcanomahony1.github.io/Bolo-Website/Data.html', 'https://lorcanomahony1.github.io/Bolo-Website/Data.html', 'https://lorcanomahony1.github.io/Bolo-Website/Sales.html', 'https://lorcanomahony1.github.io/Bolo-Website/Sales.html', 'https://lorcanomahony1.github.io/Bolo-Website/ContactUs.html']
list_of_emails = []


def proxy_request():

    for link in link_list:
        while True:
            try:
                response = requests.get(link)
                page = response.text
                page_soup = soup(page, "html.parser")
                divtext = page_soup.findAll("div")
                emails = divtext
                list_of_emails.append(emails)
                print(emails)
            except:
                continue
            break
           
            




proxy_request()

