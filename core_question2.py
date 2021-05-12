#sontran.code@gmail.com

# Question 2 (in difficulty):
# https://so.youku.com/search_video/q_love?searchfrom=1

# Youku search page video url capture
# Requirements: Do not use a browser, use a cracking method, grab the url and video title of the video on the Youku search page, turn the page to the last page, and output the search result in json format.
# The data captured on each page must be consistent with the data seen by the actual browser. (Requires a script to automatically obtain COOKIE)

import re
import requests
import cfscrape
from bs4 import BeautifulSoup

def ByPass_capcha(headers,url):
    """Change header for pass capcha"""

    regex = re.compile(f"^(/)")
    scraper = cfscrape.CloudflareScraper()
    html = scraper.get(url,headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    cookies = [
        {
            'name': c.name,
            'value': c.value, 
            'domain': c.domain, 
            'path': c.path,
            'secure':c.secure,
            'expires':c.expires,
            'comment':c.comment}
            for c in scraper.cookies
    ]
    try:
        data= []
        findalldiv = soup.findAll('div',{'data-name':'m_pos'})
        for div in findalldiv:
            for a in div.find_all('a',href=regex):
                if a.attrs['data-spm'] == "dtitle":
                    data.append({'title': a.text,'url': a.attrs['href']})
        divlast = soup.find_all('div',{'class':'label-text_VrGXs'})
        page = int(divlast[-1].text)
        htmllastpage = get_html(page)
        return data,htmllastpage,cookies
    except Exception as e:
        return data,"Capcha !!!",cookies

def get_html(page=None):
    if page!=None:
        headers={"User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            'Content-Type': 'application/json',
            'referer':'https://www.google.com/'}
        url = "https://so.youku.com/search_video/q_love?searchfrom={page}"
        scraper = cfscrape.CloudflareScraper()
        html = scraper.get(url,headers=headers).text # fstrings require Python 3.6+
        return html
    else:
        return "Capcha!!"


headers={"User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.11",
        'Content-Type': 'application/json',
        'referer':'https://www.google.com/',
        'From': 'example@domain.com'}
url = "https://so.youku.com/search_video/q_love?searchfrom=1"

        
data,file,cookies = ByPass_capcha(headers,url)
print(data)
print(file)
print(cookies)