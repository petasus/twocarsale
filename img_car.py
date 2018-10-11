import webbrowser
from urllib.request import urlopen
def read_image_url(url,num):
    with urlopen(url) as response, open("img"+str(num)+".jpg", "wb") as out_file:
        data = response.read()
        out_file.write(data)
