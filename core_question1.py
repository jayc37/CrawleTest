import re
import requests
from bs4 import BeautifulSoup

def get_links(url,pattern):
    links = ''
    regex = '/r/n'
    # style = "position:relative"
    html = requests.get(f"{url}").text # fstrings require Python 3.6+
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("pre", {'class':'links'}):
        for l in link.contents:
            if pattern[0] in l or pattern[1] in l:
               links+= ",".join(l.splitlines()) + ','
    return links[:-1]
