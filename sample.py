from bs4 import BeautifulSoup
import requests

url_to_scrape = 'http://reg.buu.ac.th/registrar/home.asp'
r = requests.get(url_to_scrape)
r.encoding = 'TIS-620'
soup = BeautifulSoup(r.text, "lxml")
data=soup.select("a")
for i in data:
    print(i.text.strip())

