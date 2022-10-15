import requests
from bs4 import BeautifulSoup

def extractParent(brand):
    url = "https://www.google.com/search?q="+brand+"+parent+company"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    try:
        target = soup.find("div", {"class": "BNeawe deIvCb AP7Wnd"})
        assert len(target.text) <= 6
        return target.text
    except:
        return brand