import requests as req
from bs4 import BeautifulSoup as BS4

def myScraping():
    URL = 'https://www.boatrace.jp/owpc/pc/data/racersearch/season?toban=4019'
    headers = {"User-Agent": "hoge"}

    resp = req.get(URL, timeout=1, headers=headers)
    r_text = resp.text

    soup = BS4(r_text, 'html.parser')
    soup_th = soup.find_all('th')

    soup = BS4(r_text, 'html.parser')
    soup_td = soup.find_all('td')

    racerDict = {}
    for i in range(len(soup_th)):
        racerDict[soup_th[i].text] = soup_td[i].text

    return racerDict
    #for t in soup_titles:
        #print(t.get_text())