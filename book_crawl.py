import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
from http.client import responses

source_url = 'https://www.iranketab.ir/tag/284-browse-books-by-subject'
headers = {
    'Accept-Language': 'en-US',
    'User-Agent': 'director123456'
}
first_page = requests.get(source_url, headers=headers)
first_page.status_code
responses[first_page.status_code]
first_page.content.decode()
soup = BeautifulSoup(first_page.content, 'html.parser')
dive_tags = soup.find('div', attrs={'class': 'row'})
tags = soup.find_all('a', attrs={'class': 'product-tags-item ParentTag'})
count_of_pages = []
all_books_links = []
for n in range(len(tags)):
    if (int((tags[n].find('span')).text[2:-7])) % 20 == 0:
        count = (int((tags[n].find('span')).text[2:-7])) / 20
    else:
        count = (int((tags[n].find('span')).text[2:-7])) // 20
    count_of_pages.append(count)
# link_of_book_tags=[]
for i in range(len(tags)):
    # create link of tags

    url_tag = ('https://www.iranketab.ir' + (tags[i].get('href')))
    for y in range(count_of_pages[i]):

        url_page = url_tag + '?Page=' + str(y + 1)
        # try:
        page_tag = requests.get(url_page, headers=headers)
        page_tag.raise_for_status()
        page_tag.content.decode()
        soup_tag = BeautifulSoup(page_tag.content, 'html.parser')
        e = soup_tag.find('div', attrs={'id': 'Booklist'})
        # e2--> a : name of books in the first page of the tag
        e2 = e.find_all('h4', attrs={'class': 'product-name-title'})
        # create link of books of firs page  of a tag
        for j in range(len(e2)):
            # create link of books of a tag
            all_books_links.append(
                'https://www.iranketab.ir' + (e2[j].find('a', attrs={'class': 'product-item-link'})).get('href'))
    # except ConnectionError :
    # print("connection error")
    # print("Skipping to the next page...")
    # continue

all_books_links
book_id_dataframe = pd.DataFrame(all_books_links, columns=['book_links'])
df_no_duplicates = book_id_dataframe.drop_duplicates()
book_id_dataframe.to_csv('book_links.csv', index=True)
result = book_id_dataframe.groupby('book_links').count()

'''   
url='https://www.iranketab.ir/tag/103-fiction' 
pagex=requests.get(url,headers=headers)
pagex.content.decode()
soupx=BeautifulSoup(pagex.content,'html.parser')
pn1=soupx.find('ul',attrs={'class':'pagination'})
lis=pn1.find_all('a')
lis[0].text
len(lis)



e=soupx.find('div',attrs={'id':'Booklist'})
e2=e.find_all('h4',attrs={'class':'product-name-title'})   
(e2[0].find('a',attrs={'class':'product-item-link'})).get('href')


https://www.iranketab.ir/tag/103-fiction
https://www.iranketab.ir/tag/103-fiction?Page=2
https://www.iranketab.ir/tag/103-fiction?Page=1
'''
