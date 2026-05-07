import urllib

import pygyak

import requests

def main():
    print(pygyak.get_page("https://index.hu"))

    url = "https://www.adobe.com/hu/creativecloud/file-types/image/raster/media_190563911f4a579a9d6f1f9d5b499b44d6413088b.jpg?width=750&format=jpg&optimize=medium"
    urllib.request.urlretrieve(url, "png.png")

    cmd = f"wget {url} -O png.png"



if __name__ == "__main__":
    main()