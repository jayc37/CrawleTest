import cfscrape
import requests
def Bypass_Cloudflare(url):
    """Enter url Cloudflare's anti-bot page, return cookies []"""
    # url = "https://www.gnula.cc/ver-episode/big-sky-2020-1x9/"  # => "<!DOCTYPE html><html><head>..."

    scraper = cfscrape.CloudflareScraper()
    scraper.post(url,data = {'key':'value'})
    data = [
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
    return data