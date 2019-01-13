#!/usr/bin/python

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import string


def getarticle(name):
        url = 'https://newsapi.org/v2/everything?q='+name+'&from=2019-01-11&sortBy=publishedAt&apiKey=5fbb5fe295f64199ae436a70e332e335'
        json_data2 = requests.get(url).json()
        result = json_data2['objects'][0]['text']
        final = [word.strip(string.punctuation) for word in result.split()]
        return final

def getnews(news):
        #Get company news
        finallist = []
        ulturl = "https://api.diffbot.com/v3/article?token=eac77c2dca2a627f47278a19e38506a6&url="
        sub = {}
        url = 'https://newsapi.org/v2/everything?q='+news+'&from=2019-01-11&sortBy=publishedAt&apiKey=5fbb5fe295f64199ae436a70e332e335'
        json_data = requests.get(url).json()
        for i in range(0, 7):
                link = json_data['articles'][i]['url']
                fin = getarticle(ulturl + link)

                if fin!= None:
                        finallist.append(fin)
                
        print(finallist)

        return(finallist)
        
