import webbrowser
from urllib.request import urlopen
def read_image_url(url):
    with urlopen(url) as response, open("img.jpg", "wb") as out_file:
        data = response.read()
        out_file.write(data)

if __name__=='__main__':
    url = "https://img3.icarcdn.com/1773394/gallery_used-car-one2car-lexus-rx450h-suv-thailand_1773394_CpG7mR5tPBio1kROIaPCYT.jpg?smia=xTM"

    #webbrowser.open(url)
    read_image_url(url)
