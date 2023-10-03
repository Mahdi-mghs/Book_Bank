import pandas as pd
import numpy as np
import math
import scipy
from scipy.stats import ttest_ind
from scipy import stats

All_books=pd.read_csv('All_books.csv')
Author=pd.read_csv('Author.csv')
Book_languages=pd.read_csv('Book_languages.csv')
Book_Tag=pd.read_csv('Book_Tag.csv')
Book_writer=pd.read_csv('Book_Writer.csv')
Publisher=pd.read_csv('Publiser.csv')
Tags=pd.read_csv('Tags.csv')
Translation=pd.read_csv('Translation.csv')
Writer=pd.read_csv('Writer.csv')
Final_Data=pd.read_csv('Final_Data.csv')
#part1
"""
یک ستون به اسم  is translates درست می‌کنیم که در آن مشخص می‌شود کتاب ترجمه شده است یا خیر
"""
Final_Data['Is Translated'] = (Final_Data['translations'] != '[None]') | (Final_Data['ids_translations'] != '[None]')
Final_Data['relative price']=(Final_Data['current_price']/Final_Data['pages'])
"""
ستون قیمت کتاب‌هایی که ترجمه شده اند و نشده اند را جداگانه داخل لیست می‌کنیم و مقادیر 0 را حذف می‌کنیم
"""

translated_prices = Final_Data[Final_Data['Is Translated'] == True]['current_price'].tolist()

translated_prices = list(filter(lambda x: not math.isnan(x), translated_prices))
non_translated_prices = Final_Data[Final_Data['Is Translated'] == False]['current_price'].tolist()
filtered_list_tp = [x for x in translated_prices if not (math.isnan(x) or x == 0)]

filtered_list_ntp = [x for x in non_translated_prices if not (math.isnan(x) or x == 0)]
"""
ازمون فرض را انجام می‌دهیم
"""
t_stat, p_value = ttest_ind(filtered_list_tp, filtered_list_ntp)
alpha = 0.05

if p_value < alpha:
    print("این ادعا که کتاب ترجمه شده قیمتش بیشتر است پذیرفته می‌شود")
else:
    print("این ادعا که کتاب ترجمه شده قیمتش بیشتر است پذیرفته نمی‌شود")


############part2
"""
قیمت کتاب های نوع شومیز و جلد سخت را جداگانه از دیتا فریم میگیرم
"""
cover_shoomiz_prices = Final_Data[Final_Data['types'] == 'شومیز']['current_price']
cover_sakht_prices = Final_Data[Final_Data['types'] == 'جلد سخت']['current_price']
"""

ازمون تی را انجام میدهیم
"""
t_stat, p_value = stats.ttest_ind(cover_shoomiz_prices, cover_sakht_prices, equal_var=False)
alpha = 0.05

if p_value < alpha:
    print("این ادعا که بین دو نوع جلد تفاوت قیمت قابل توجه وجود دارد پذیرفته می‌شود، ")
else:
    print("این ادعا که بین دو نوع جلد تفاوت قیمت قابل توجه وجود دارد پذیرفته می‌شود")

