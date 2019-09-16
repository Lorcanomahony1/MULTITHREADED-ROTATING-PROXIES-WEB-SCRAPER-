
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


user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]') and i.xpath('.//td[5][contains(text(),"elite proxy")]') or i.xpath('.//td[5][contains(text(),"anonymous")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


#If you are copy pasting proxy ips, put in the list below
#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
proxies = get_proxies()
proxy_pool = cycle(proxies)

   

def proxy_request(start, end):


    for i in range(start, end):
    	while(end < len(link_list)):
            try:
            	link = link_list[i]
            	user_agent = random.choice(user_agent_list)
            	proxy = next(proxy_pool)
            	headers = {'Users-Agent': user_agent}
            	response = requests.get(link,proxies={"http" :proxy, "https": proxy},headers=headers)
            	page = response.text
            	page_soup = soup(page, "html.parser")
            	divtext = page_soup.findAll("div")
            	emails = divtext
            	list_of_emails.append(emails)
            	print(emails)
            	time.sleep(10)
            except:
                continue
            break
    print(proxy)

thread_count = 16
image_count = len(link_list)
thread_list = []


for i in range(thread_count): 

	start = math.floor(i * image_count / thread_count) + 1
	end = math.floor((i + 1) * image_count / thread_count) + 1
	thread_list.append(threading.Thread(target=proxy_request, args=(start, end)))

for thread in thread_list:
	thread.start()

for thread in thread_list:
	thread.join()


