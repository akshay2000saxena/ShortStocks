#!/usr/bin/python

import requests
from urllib.request import urlopen
import string

def getnews(news):
        #Get company news
        sub = {}

        url = 'https://newsapi.org/v2/everything?q='+news+'&from=2019-01-11&sortBy=publishedAt&apiKey=5fbb5fe295f64199ae436a70e332e335'
        json_data = requests.get(url).json()
        for i in range(0, 2):
                source = json_data['articles'][i]['source']['name']
                title = json_data['articles'][i]['title']
                desc = json_data['articles'][i]['description']
                link = json_data['articles'][i]['url']

                article = {
                    'source': source,
                    'title': title,
                    'desc': desc,
                    'link' : link
                }
                
                sub[i] = article

        print(sub)
        return(sub)

