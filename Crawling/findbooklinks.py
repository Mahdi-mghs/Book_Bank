import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
from http.client import responses
def find_book_lists(source_url):
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
 """
برای هر موضوع، تعداد صفحع مربوط به آن را از طریق تقسیم تعداد کتاب بر page size که مقدار ان 20 است بدست می‍اوریم 
 """
 count_of_pages=[]  # count of pages for each tag append to this list
 for n in range(len(tags)):
     if(int((tags[n].find('span')).text[2:-7]))%20==0:
         count=(int((tags[n].find('span')).text[2:-7]))/20
     else:
         count=(int((tags[n].find('span')).text[2:-7]))//20
     count_of_pages.append(count) 
    
 """
در یک حلقه با استفاده از کد مربوط به تگ یا موضوع و همچنین تعداد صفحه ای که برای آن محاسبه کردیم، لینک هر صفحه که در ان لیست کتاب وجود دارد را میسازیم
 """   

 
 book_links=[]  #  all of book links append to this list
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
      bookname=soup.find_all('h4', attrs={'class':'product-name-title'})
      """
     در این حلقه از هر صفحه که لینکش را درست کردیم، لینک کتاب ها را استخراج میکنیم
 

      """     
      for i in range(len(bookname)):
        booklink=bookname[i].find('a',attrs={'class':'product-item-link'})
        book_url='https://www.iranketab.ir'+booklink.get('href')
        book_links.append(book_url)
 """
دیتا فریم کلی و جامع خود را درست کرده و تبدیل به csv میکنیم

 """
 dt=pd.DataFrame(book_links,columns=['book_link'])
 dt_filtered=dt.drop_duplicates()
 return(dt_filtered)

