#sontran.code@gmail.com

# Question 2 (in difficulty):
# https://so.youku.com/search_video/q_love?searchfrom=1

# Youku search page video url capture
# Requirements: Do not use a browser, use a cracking method, grab the url and video title of the video on the Youku search page, turn the page to the last page, and output the search result in json format.
# The data captured on each page must be consistent with the data seen by the actual browser. (Requires a script to automatically obtain COOKIE)

import re
import requests
from bs4 import BeautifulSoup



def ByPass_capcha(headers=dict,url=str):
    """Change header for pass capcha"""
    data                = []
    regex               = re.compile(f"^(/)")
    spm                 = "dtitle"

    cookies,datcookies  = get_cookies(url,headers)

    html                = requests.get(url,headers=headers,
                                        cookies=cookies).text
    soup                = BeautifulSoup(html, "html.parser")
    try:
        for div in soup.findAll('div',{'data-name':'m_pos'}):
            for a in div.find_all('a',href=regex):
                if a.attrs['data-spm'] == spm:
                    data.append({'title': a.text,'url': a.attrs['href']})
        divlast         = soup.find_all('div',{'class':'label-text_VrGXs'})
        page            = int(divlast[-1].text)
        htmllastpage    = get_html(page,cookies)

        return data,htmllastpage,datcookies
        
    except Exception as e:
        return ["Capcha Found"],"Capcha Found !!!",["Capcha Found"]

def get_cookies(url=str,head= dict):
    sess                = requests.Session()
    cookies             = sess.get(url,headers=head).cookies

    return cookies, sess.cookies.get_dict()


def get_html(page=None,cookies=None):
    if page!=None:
        headers={"User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            'Content-Type': 'application/json',
            'referer':'https://www.google.com/'}
            
        url = "https://so.youku.com/search_video/q_love?searchfrom={}".format(page)
        html = requests.get(url,headers=headers,cookies=cookies).text 
        return html
    else:
        return "Capcha!!"


headers={"User_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.11",
        'Content-Type': 'application/json',
        'referer':'https://www.google.com/',
        'From': 'example@domain.com'}
url = "https://so.youku.com/search_video/q_love?searchfrom=1"
# url = "https://rmz.cr/release/chicago-pd-s08e07-webrip-x264-ion10"

        
data,file,cookies = ByPass_capcha(headers,url)
