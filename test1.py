import requests
from bs4 import BeautifulSoup
url_to_scrape = 'https://th.wikipedia.org/wiki/%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%81'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
data=soup.select("li[id='n-mainpage'] a")
for i in data:
            print(i.text.strip())

print(1)
