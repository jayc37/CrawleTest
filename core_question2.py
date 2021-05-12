import re
import requests
import cfscrape
from bs4 import BeautifulSoup

def get_question3():
    headers={"User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.11",
            'Content-Type': 'application/json',
            'referer':'https://www.google.com/',
            'From': 'example@domain.com'}
    url = "https://so.youku.com/search_video/q_love?searchfrom=1"
    regex = re.compile(f"^(/)")
    scraper = cfscrape.CloudflareScraper()
    html = scraper.get(url,headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
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
        return data,htmllastpage
    except Exception as e:
        return data,"Capcha !!!"
data,file = get_question3()
print(data)
print(file)
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
