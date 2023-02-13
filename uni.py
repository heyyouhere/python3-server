from bs4 import BeautifulSoup
import requests
import json


NEWS_LIMIT = 5

def getNewsTPU():
    news__titles = []
    site = requests.get('https://news.tpu.ru/news/').content
    soup = BeautifulSoup(site, features="html.parser")
    for news__title in soup.find_all("h3", {"class": "news__title"}):
        news__titles.append(news__title.get_text())
        if len(news__titles) == NEWS_LIMIT:
            break
    return news__titles
 
def getNewsTSU():
    news__titles = []
    site = requests.get('https://news.tsu.ru/news/').content
    soup = BeautifulSoup(site, features="html.parser")
    for news__title in soup.find_all("a", {"class": "news-item__title link-over-content"}):
        news__titles.append(news__title.get_text()[1:-1])
        if len(news__titles) == NEWS_LIMIT:
            break
    return news__titles
    
def getNewsSSMU():
    news__titles = []
    site =requests.get('https://ssmu.ru/ru/news/archive/', verify=False).content
    soup = BeautifulSoup(site, features="html.parser")
    isTitle = True
    for news__title in soup.find_all("a", {"class": "text-default"}):
        if isTitle:
            news__titles.append(news__title.get_text())
        isTitle = not isTitle
        if len(news__titles) == NEWS_LIMIT:
            break
    return news__titles

def getNewsTUSUR():
    news__titles = []
    site =requests.get('https://tusur.ru/ru/novosti-i-meropriyatiya/novosti', verify=False).content
    soup = BeautifulSoup(site, features="html.parser")

    for news__title in soup.find_all("div", {'class': 'news-page-list-item-since'}):
            news__titles.append(news__title.findPreviousSibling('h1').get_text())
            if len(news__titles) == NEWS_LIMIT:
                break
    return news__titles
    


def getNews():
    news_dir = {
        'TSU' : getNewsTSU(),
        'TPU' : getNewsTPU(),
        'SSMU' : getNewsSSMU(),
        'TUSUR' : getNewsTUSUR()
    }
    result = json.dumps(news_dir, separators=(',', ':'))
    
    return result

from pprint import pprint
pprint(getNews())