#!/usr/bin/python

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import string

def getnews(news):
        #Get company stock price
        quote_page = 'https://m.nasdaq.com/symbol/' + news
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        price_box = soup.find('div', attrs={'class':'last-sale padded-bottom displayIB paddingR5p'})
        price = price_box.text
        sub = ""
        sub += ('Current stock price: ' + price)
        sub += ('\n')
        sub += '\n'

        #Get company news

        url = 'https://newsapi.org/v2/everything?q=MSFT&from=2019-01-11&sortBy=publishedAt&apiKey=5fbb5fe295f64199ae436a70e332e335'
        json_data = requests.get(url).json()
        for i in range(0, 7):
                source = json_data['articles'][i]['source']['name']
                title = json_data['articles'][i]['title']
                desc = json_data['articles'][i]['description']
                link = json_data['articles'][i]['url']
                
                sub += ('Source: ' + source)
                sub += '\n'
                sub += ('Title: ' + str(title))
                sub += '\n'
                sub += ('Description: ' + desc)
                sub += '\n'
                sub += ('Link: ' + str(link))
                sub += '\n'
                sub += '\n'


        # #Get financial data
        # url = 'https://finance.yahoo.com/quote/MSFT/analysis?p=' + news
        # html = requests.get(url).content
        # df_list = pd.read_html(html)
        # for i in range(0, 6):
        #         df = df_list[i]
        #         print(df)
        print(sub)
        return(sub)
        
getnews('MSFT')
