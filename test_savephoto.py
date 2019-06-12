import requests
import os
from urllib.request import urlopen

def read_image_url(url,id,order):
    name = "imgID_"+str(id)+"_Order_"+order+".jpg"
    with urlopen(url) as response, open(name, "wb") as out_file:
        data = response.read()
        out_file.write(data)
        out_file.close()
    link='http://127.0.0.1/test/up.php'
    file_up=open(name, 'rb')
    files = {'file':file_up}
    requests.post(link, files=files)
    file_up.close()
    os.remove(name)

url = ('https://img5.icarcdn.com/6245184/gallery_used-car-one2car-ford-ranger-hi-rider-xlt-pickup-thailand_6245184_hcHqikZVX81h4Wgd90Bvgh.jpg?smia=xTM')

num = 1
name = "img"+str(id)+"_"+str(num)+".jpg"

read_image_url(url,num)
