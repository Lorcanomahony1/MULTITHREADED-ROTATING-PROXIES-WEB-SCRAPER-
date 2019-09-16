import random
import threading
import time

import requests


def load_user_agents():
    """Returns a list of user agents from a file named useragents.csv
    This file must contain a user agent per line.
    """

    with open("useragents.csv", "r", encoding="utf-8") as temp_file:
        return temp_file.read().splitlines()


def load_urls():
    """Returns a list of urls to scrape from a file named urls.csv
    This file must contain a url per line.
    """

    with open("urls.csv", "r", encoding="utf-8") as temp_file:
        return temp_file.read().splitlines()

def init_proxy_retrieval():
    """This function will update your global proxies list every 60 seconds."""

    while True:

        # You will first need to acquire the proxies, once you have them.
        # clear the PROXIES list and then append them.

        PROXIES.clear()

        for item in range(10):

            # We just make random proxies for demo purposes.
            r1 = random.randint(0, 255)
            r2 = random.randint(0, 255)
            r3 = random.randint(0, 255)
            r4 = random.randint(0, 255)

            PROXIES.append(f"http://{r1}.{r2}.{r3}.{r4}:1080")

        time.sleep(60)

def init_scraper(url):
    """Loads the site html."""


    with MAIN_LOCK:

        headers = {"User-Agent": random.choice(USER_AGENTS)}
        proxy = {"http": random.choice(PROXIES)}

        print("Scraping:", url)
        print("Proxy:", proxy["http"])
        print("User-Agent:", headers["User-Agent"])
        print("-------------------")

        with requests.get(url, headers=headers, proxy=proxy) as response:

            html = response.text
            print(html)

if __name__ == "__main__":

    PROXIES = list()
    USER_AGENTS = load_user_agents()
    URLS = load_urls()

    MAIN_LOCK = threading.RLock()

    threading.Thread(target=init_proxy_retrieval, daemon=True).start()

    # Give it some seconds for it to get the first batch of proxies.
    time.sleep(3)

    while True:

        # Here you will implement your scraper.

        for url in URLS:
            threading.Thread(target=init_scraper, args=(url,), daemon=True).start()

        time.sleep(5)