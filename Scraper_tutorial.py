# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:12:01 2017

@author: Arjun
"""
#tutorial from http://python-guide-pt-br.readthedocs.io/en/latest/scenarios/scrape/
import requests
from lxml import html
#simple page with just names and numbers, easy to scrape
page=requests.get('http://econpy.pythonanywhere.com/ex/001.html')
print(page.status_code) #determine if the page was found
if( not page.status_code==404): 
    tree = html.fromstring(page.content) #parse the webpage into an html tree
    buyers= tree.xpath('//div[@title="buyer-name"]/text()') #get data under this tag
    prices= tree.xpath('//span[@class="item-price"]/text()') 
    print(buyers)
    print(prices)
else:
    print("Error: Site not found")