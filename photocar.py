import webbrowser
from urllib.request import urlopen

url = ('https://www.one2car.com/for-sale/ford-ranger-hi-rider-xlt-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%93%E0%B8%91%E0%B8%A5-%E0%B8%81%E0%B8%B2%E0%B8%8D%E0%B8%88%E0%B8%99%E0%B8%B2%E0%B8%A0%E0%B8%B4%E0%B9%80%E0%B8%A9%E0%B8%81/4815426')

def read_image_url(url,num):
    with urlopen(url) as response, open("img"+str(num)+".jpg", "wb") as out_file:
        data = response.read()
        out_file.write(data)



#r = requests.get(url_to_scrape).content
#soup = BeautifulSoup(r, "lxml")
#    image_tags = soup.select("div img.gallery__item")
#    number_name=1
#    for i in image_tags:
#        img_car.read_image_url(i.get('data-src'), number_name)
#        number_name=number_name+1
