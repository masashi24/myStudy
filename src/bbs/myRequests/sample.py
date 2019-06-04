import requests
from bs4 import BeautifulSoup

def myScraping():
    URL = 'http://google.com'
    headers = {"User-Agent": "hoge"}

    resp = requests.get(URL, timeout=1, headers=headers)
    r_text = resp.text

    soup = BeautifulSoup(r_text, 'html.parser')
    soup_titles = soup.find_all('title')

    return soup_titles
    #for t in soup_titles:
        #print(t.get_text())