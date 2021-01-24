import requests as req
from bs4 import BeautifulSoup as BS4
import datetime

def getDt():
    dt_now = datetime.datetime.now()
    return dt_now

def createDate(datetimeArg):
    tmp = str(datetimeArg)
    tmp = tmp.split(' ')
    tmp = tmp[0].split('-')
    return(tmp[0]+tmp[1]+tmp[2])

def myScraping(data):
    URL = 'https://www.boatrace.jp/owpc/pc/race/racelist?rno=1&jcd=01&hd='+'20200603'
    headers = {"User-Agent": "hoge"}

    print(URL)

    resp = req.get(URL, timeout=1, headers=headers)
    r_text = resp.text

    soup = BS4(r_text, 'html.parser')
    soup_tr = soup.find_all('tr')

    soup = BS4(r_text, 'html.parser')
    soup_td = soup.find_all('td')

    racerDict = soup_td
    #for i in range(len(soup_tr)):
        #racerDict[soup_tr[i].text()] = soup_td.text()

    return racerDict
    #for t in soup_titles:
        #print(t.get_text())

#dateArg = (createDate(getDt()))
#data = myScraping(dateArg)
#print(data)
#for k in data:
#    print(k)