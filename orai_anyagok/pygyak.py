import urllib.request

def get_page(url: str) -> str:
    source = urllib.request.urlopen(url).read()
    return source.decode('utf-8')