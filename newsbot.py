#!/usr/bin/python

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import string


def getarticle(url):
    json_data2 = requests.get(url).json()
    result = json_data2['objects'][0]['text']
    final = [word.strip(string.punctuation) for word in result.split()]
    return final

def getnews(news):
        #Get company stock price
        quote_page = 'https://m.nasdaq.com/symbol/' + news
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        price_box = soup.find('div', attrs={'class':'last-sale padded-bottom displayIB paddingR5p'})
        price = price_box.text
        print('Current stock price: ' + price)
        print('\n')

        #Get company news
        finallist = []
        ulturl = "https://api.diffbot.com/v3/article?token=eac77c2dca2a627f47278a19e38506a6&url="
        sub = {}
        url = 'https://newsapi.org/v2/everything?q=MSFT&from=2019-01-11&sortBy=publishedAt&apiKey=5fbb5fe295f64199ae436a70e332e335'
        json_data = requests.get(url).json()
        for i in range(0, 7):
                source = json_data['articles'][i]['source']['name']
                title = json_data['articles'][i]['title']
                desc = json_data['articles'][i]['description']
                link = json_data['articles'][i]['url']
                fin = getarticle(ulturl + link)

                if fin!= None:
                        finallist.append(fin)
                


        # #Get financial data
        # url = 'https://finance.yahoo.com/quote/MSFT/analysis?p=' + news
        # html = requests.get(url).content
        # df_list = pd.read_html(html)
        # for i in range(0, 6):
        #         df = df_list[i]
        #         print(df)

        return(finallist)
        