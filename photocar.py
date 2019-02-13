import webbrowser
from urllib.request import urlopen

url = ('https://img5.icarcdn.com/6245184/gallery_used-car-one2car-ford-ranger-hi-rider-xlt-pickup-thailand_6245184_hcHqikZVX81h4Wgd90Bvgh.jpg?smia=xTM')

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

read_image_url(url,1)
