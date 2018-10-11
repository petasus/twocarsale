import requests
from bs4 import BeautifulSoup
import img_car
def sendlinks(links):
    data_incar=[]
    url_to_scrape = links
    r = requests.get(url_to_scrape).content
    soup = BeautifulSoup(r, "lxml")
    image_tags = soup.select("div img.gallery__item")
    number_name=1
    for i in image_tags:
        img_car.read_image_url(i.get('data-src'), number_name)
        number_name=number_name+1


links="https://www.one2car.com/for-sale/toyota-camry-g-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%93%E0%B8%91%E0%B8%A5-%E0%B8%A3%E0%B8%B1%E0%B8%8A%E0%B8%94%E0%B8%B2%E0%B8%AF-%E0%B8%AB%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%82%E0%B8%A7%E0%B8%B2%E0%B8%87-%E0%B8%A5%E0%B8%B2%E0%B8%94%E0%B8%9E%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%A7-%E0%B9%80%E0%B8%9E%E0%B8%8A%E0%B8%A3%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5%E0%B8%95%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%AB%E0%B8%A1%E0%B9%88/5285809"
sendlinks(links)
