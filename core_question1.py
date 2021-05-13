#sontran.code@gmail.com

# Question 1 (low difficulty):
# https://rmz.cr/release/chicago-pd-s08e07-webrip-x264-ion10

# On this page, grab the url links of three websites: rapidrar.com, nitroflare.com, and clicknupload.co.
# The output uses a semicolon to separate the above url

import re
import requests
from bs4 import BeautifulSoup

def get_links(url,pattern):
    links = ''
    regex = '/r/n'
    html = requests.get(f"{url}").text 
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("pre", {'class':'links'}):
        for l in link.contents:
            if pattern[0] in l or pattern[1] in l:
               links+= ",".join(l.splitlines()) + ','
    return links[:-1]
