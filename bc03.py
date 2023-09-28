import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
from http.client import responses
source_url='https://www.iranketab.ir/tag/284-browse-books-by-subject'
headers = {
    'Accept-Language': 'en-US' ,     
    'User-Agent': 'director123456'
 }
first_page=requests.get(source_url, headers=headers)
first_page.status_code
responses[first_page.status_code]
first_page.content.decode()
soup = BeautifulSoup(first_page.content, 'html.parser')
dive_tags=soup.find('div',attrs={'class':'row'})
tags=soup.find_all('a',attrs={'class':'product-tags-item ParentTag'})
count_of_pages=[]
for n in range(len(tags)):
    if(int((tags[n].find('span')).text[2:-7]))%20==0:
        count=(int((tags[n].find('span')).text[2:-7]))/20
    else:
        count=(int((tags[n].find('span')).text[2:-7]))//20
    count_of_pages.append(count) 
all_books_links=[]
book_links=[]
for n in range(len(tags)):
    number_of_book_of_the_tag=str(int((tags[n].find('span')).text[2:-7])-1)
    tag_code = re.findall(r'/tag/(\d+)-', tags[n].get('href'))
    for i in range(count_of_pages[n]):
     url_tag_book='https://www.iranketab.ir/book?pagenumber='+str(i)+'&pagesize=20&sortOrder=date_desc&tagid='+tag_code[0]
     webpage=requests.get(url_tag_book, headers)
     webpage.status_code
     responses[webpage.status_code]
     webpage.content.decode()
     soup = BeautifulSoup(webpage.content, 'html.parser')
     gg1=soup.find_all('h4', attrs={'class':'product-name-title'})
     for i in range(len(gg1)):
       gg2=gg1[i].find('a',attrs={'class':'product-item-link'})
       book_url='https://www.iranketab.ir'+gg2.get('href')
       book_links.append(book_url)
book_links
dt=pd.DataFrame(book_links,columns=['book_link'])
dt_filtered=dt.drop_duplicates()
dt_filtered.to_csv('link_book_filtered.csv',index=True)
