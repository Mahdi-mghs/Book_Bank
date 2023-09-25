#Import necessary library
import re
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# url = 'https://www.iranketab.ir/book/1017-the-compound-effect'
# url = 'https://www.iranketab.ir/book/116021-a-hundred-years-beyond-the-pleasure-principle'
# url = 'https://www.iranketab.ir/book/12760-heat-up-all-my-winter'

def append_dup(main_list, child_list, counts):
    for i in range(counts):
        main_list.append(child_list)

def find_a(a_sample, list1, list2, list3, patt):
    wr_li = a_sample['href']
    match = re.search(patt, wr_li)
    if match:
        pub_id = match.group(1)
        list1.append(pub_id)
    list2.append(wr_li)
    list3.append(a_sample.text.strip())

def tra_wri(span_samp, pattern, tar_li, tar_li1, tar_li2, checker):
    wri_na = []
    wri_id = []
    wri_link = []
    length = len(span_samp)
    for i_counter in range(length):
        if i_counter == 1 - checker:
            if span_samp[1 - checker].find_parent('a'):
                samp_a = span_samp[1 - checker].find_parent('a', href=True)
                find_a(samp_a, wri_id, wri_link, wri_na, pattern)
            else:
                wri_id.append(None)
                wri_link.append(None)
                wri_na.append(span_samp[1 - checker].text.strip())
        elif i_counter == 2 - checker:
            if span_samp[2 - checker].find_parent('a'):
                samp_a = span_samp[2 - checker].find_parent('a', href=True)
                find_a(samp_a, wri_id, wri_link, wri_na, pattern)
            else:
                wri_id.append(None)
                wri_link.append(None)
                wri_na.append(span_samp[2 - checker].text.strip())
        elif i_counter == 3:
            if span_samp[3 - checker].find_parent('a'):
                samp_a = span_samp[3 - checker].find_parent('a', href=True)
                find_a(samp_a, wri_id, wri_link, wri_na, pattern)
            else:
                wri_id.append(None)
                wri_link.append(None)
                wri_na.append(span_samp[3 - checker].text.strip())

    tar_li.append(wri_na)
    tar_li1.append(wri_id)
    tar_li2.append(wri_link)

def today_info(tsoup):

    stt = False
    percent = 0
    p_r_p_w = tsoup.find_all('ul', {'class': 'clearfix'})
    for i in p_r_p_w:
        # print(i.text)
        stylee = 'float: left;font-size: 12px;line-height: 1.375;background-color: #fb3449;color: #fff;padding: 5px 30px 3px;-webkit-border-radius: 0 16px 16px 16px;border-radius: 0 16px 16px 16px;'
        if i.find('div', {'style': stylee}) != None:
            percent = int(i.find('div').text.replace(' % تخفیف', ''))
            off_percent.append(percent)
        else:
            off_percent.append(None)

        price = int(i.find('span', {'class': 'price'}).text.replace(',', ''))
        if percent != 0:
            fi_price = price - ((price * percent)/100)
            current_price.append(fi_price)
        else:
            current_price.append(price)

        if i.find('div', {'class': 'my-rating'}) != None:
            rating = float(i.find('div', {'class': 'my-rating'})['data-rating'])
            rate.append(rating)

        if i.find('i', {'class': 'icon-tick'}) != None:
            stt = True
        else:
            stt = False


        if i.find('div', {'class': 'col-xs-12 prodoct-attribute-items'}):
            w_p = i.find_all('div', {'class': 'col-xs-12 prodoct-attribute-items'})
            for wp in w_p:
                test_id = wp.find('span', {'class': 'prodoct-attribute-item'}).text
                if test_id[0] == 'ا':
                    pub = wp.find('a', href=True)
                    pattern = r'/publisher/(\d+)-'
                    match = re.search(pattern, pub['href'])
                    if match:
                        pub_id = match.group(1)
                        publisher_id.append(pub_id)
                    publisher_link.append(pub['href'])
                    publisher_name.append(pub.text.strip())
                else:
                    samp = wp.find_all('span', {'class': 'prodoct-attribute-item'})
                    pattern = r'/profile/(\d+)-'
                    tra_wri(samp, pattern, writer_name, writer_id, writer_link, 0)



    if stt:
        status.append(1)
    else:
        status.append(0)

def imp_details(tsoup):
    rows = tsoup.find_all('tr')
    trr= True
    dp = True
    shab_b = True
    for row in rows:
        content = row.text.replace('  ', '').strip()
        if 'مترجم' in content:
            trr = False
        if 'میلادی' in content:
            dp = False
        if 'شابک' in content:
            shab_b = False

        if 'کد کتاب :' in content:
            book_id = content.replace('کد کتاب :', '').replace('\n', '')
            ids_book.append(int(book_id))
        elif 'مترجم' in content:
            samp = row.find_all('span', {'class': 'prodoct-attribute-item'})
            pattern = r'/profile/(\d+)-'
            tra_wri(samp, pattern, translations, ids_translations, link_translations, 1)
        elif 'شابک' in content:
            shab = row.find('td', {'class': 'ltr'}).text.replace('\n\r', '').strip()
            shabak.append(shab)
        elif 'قطع' in content:
            pice = row.find('td', {'class': 'rtl'}).text.replace('\n\r', '').strip()
            pices.append(pice)
        elif 'تعداد' in content:
            num_pg = row.find('td', {'class': 'rtl'}).text
            pages.append(int(num_pg))
        elif 'شمسی' in content:
            sunned = row.find('td', {'class': 'rtl'}).text
            sunny_date.append(int(sunned))
        elif 'میلادی' in content:
            monthed = row.find('td', {'class': 'rtl'}).text
            monthy_date.append(int(monthed))
        elif 'نوع' in content:
            typee = row.find('td', {'class': 'rtl'}).text.replace('\n\r', '').strip()
            types.append(typee)
        elif 'سری' in content:
            ser = row.find('td', {'class': 'rtl'}).text
            seriess.append(int(ser))
        elif 'زودترین' in content:
            rec_time = row.find('td', {'class': 'rtl'}).text.replace('\n\r', '').strip()
            if rec_time in '---':
                reciving_time.append(None)
            else:
                reciving_time.append(rec_time)

    if trr:
        translations.append(None)
        link_translations.append(None)
        ids_translations.append(None)
    if dp:
        monthy_date.append(None)
    if shab_b:
        shabak.append(None)

title_english = []
title_persian = []
book_bio = []
off_percent = []
current_price = []
rate = []
status = []
publisher_name = []
publisher_id = []
publisher_link = []
writer_name = []
writer_id = []
writer_link = []

ids_book = []
ids_translations = []
link_translations = []
translations = []
shabak = []
pices = []
pages = []
sunny_date = []
monthy_date = []
types = []
seriess = []
reciving_time = []

descriptions = []
book_tags = []
ids_tags = []
english_dialogs = []
persian_dialogs = []
athurs = []
pleasure_text = []
miane_tags = []

url_list = ['https://www.iranketab.ir/book/86608-self-efficacy-in-nursing', 'https://www.iranketab.ir/book/1017-the-compound-effect', 'https://www.iranketab.ir/book/12760-heat-up-all-my-winter', 'https://www.iranketab.ir/book/116021-a-hundred-years-beyond-the-pleasure-principle', 'https://www.iranketab.ir/book/1601-oversubscribed-how-to-get-people-lining-up-to-do-business-with-you', 'https://www.iranketab.ir/book/120069-animals-atlas']
headerss = {
            # "Accept-Encoding": "en-US,en;q=0.9,fa;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; moto g power (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'}
for url in url_list:
    response = requests.get(url, headers=headerss)

    soup = BeautifulSoup(response.text, 'html.parser')
    div_tags = soup.find('div', {'class': 'product-container well clearfix'})
    books = div_tags.find_all('div', {'class': 'col-md-9 col-sm-9'})
    count = 0
    print(len(books))
    for book in books:
        # Getting bio book and header
        # print(count)
        totality = book.find('div', {'class': 'row'})

        bolded = totality.find('div', {'class': 'col-md-7'})
        try:
            title_per = bolded.find('h1').text.replace('\n', '').replace('  ', '').strip()
        except AttributeError:
            title_per = bolded.find('div', {'class': 'product-name'}).text.replace('\n', '').replace('  ', '').strip()

        title_en = bolded.find('div', {'class': 'product-name-englishname ltr'}).text.replace('\n', '').replace('  ', '').strip()
        title_english.append(title_en)
        title_persian.append(title_per)
        min_det = bolded.find('div', {'class': ''}).text.replace('\n', '').replace('\r', '').replace('  ', '').strip()
        if min_det == '':
            book_bio.append(None)
        else:
            book_bio.append(min_det)

        today_info(bolded)
        # Getting Important Information
        details = totality.find('div', {'class': 'col-md-5'})
        imp_details(details)
        # count += 1

    # Description of the book

    des_tag = soup.find_all('div', {'class': 'container-fluid well'})
    booliance = [True, True, True, True]
    for i in des_tag:
        checker = i.text.strip()
        if checker[0] == 'م':
            booliance[0] = False
            descrip = i.find('div', {'class': 'review-container'})
            descrip = descrip.find('div', {'class': 'product-description'}).text.strip()
            append_dup(descriptions, descrip, len(books))
        elif checker[:9] == 'دسته بندی':
            booliance[1] = False
            # tag_panels = i.find('div', {'class': 'product-container'})
            tag_panel = i.find('div', {'class': 'clearfix'})
            tags = tag_panel.find_all('a', {'class': 'product-tags-item'}, href=True)
            total_tag = []
            total_tagid = []
            for tag in tags:
                pattern = r'/tag/(\d+)-'
                link_tag = tag['href']
                match = re.search(pattern, link_tag)
                tag_id = int(match.group(1))
                str_tag = tag.text.strip()
                total_tagid.append(tag_id)
                total_tag.append(str_tag)
            append_dup(book_tags, total_tag, len(books))
            append_dup(ids_tags, total_tagid, len(books))
        elif checker[:7] == 'نکوداشت' or checker[:7] == 'قسمت ها':
            chck = True
            chek_t = False
            chck1 = 2
            if checker[:7] == 'قسمت ها':
                booliance[3] = False
                chck = False
            if checker[:7] == 'نکوداشت':
                booliance[2] = False
                chek_t = True
                chck1 = len(i.find_all('div', {'class': 'col-md-6 col-xs-12'}))

            en_dialog = []
            pr_dialog = []
            ath_dialog = []
            ple_book = []

            if chck:
                if chek_t & chck1 == 1:
                    dialog_book_panel = i.find('div', {'class': 'col-md-12 col-xs-12'})
                else:
                    booliance[3] = False
                    dialog_book_panel = i.find('div', {'class': 'col-md-6 col-xs-12'})
                en_dialogs = dialog_book_panel.find_all('div', {'class': 'english-bar ltr'})
                pr_dialogs = dialog_book_panel.find_all('div', {'class': 'persian-bar'})
                ath_dialogs = dialog_book_panel.find_all('div', {'class': 'prise-writer ltr'})
                for dialog in en_dialogs:
                    en_dialog.append(dialog.text.strip())
                for dialog in pr_dialogs:
                    pr_dialog.append(dialog.text.strip())
                for dialog in ath_dialogs:
                    ath_dialog.append(dialog.text.strip())

                append_dup(english_dialogs, en_dialog, len(books))
                append_dup(persian_dialogs, pr_dialog, len(books))
                append_dup(athurs, ath_dialog, len(books))
            else:
                append_dup(english_dialogs, None, len(books))
                append_dup(persian_dialogs, None, len(books))
                append_dup(athurs, None, len(books))

            if chck1 == 2:
                if chek_t:
                    pleasure_book_panel = dialog_book_panel.find_next('div', {'class': 'col-md-6 col-xs-12'})
                else:
                    pleasure_book_panel = i.find('div', {'class': 'col-md-12 col-xs-12'})
                pr_pleasure = pleasure_book_panel.find_all('div', {'class': 'persian-bar'})

                for pleasure in pr_pleasure:
                    ple_book.append(pleasure.text.strip())
                append_dup(pleasure_text, ple_book, len(books))
            else:
                append_dup(pleasure_text, None, len(books))

    for i in range(4):
        if i == 0:
            if booliance[i]:
                append_dup(descriptions, None, len(books))
        elif i == 1:
            if booliance[i]:
                append_dup(book_tags, None, len(books))
                append_dup(ids_tags, None, len(books))
        elif i == 2:
            if booliance[i]:
                append_dup(english_dialogs, None, len(books))
                append_dup(persian_dialogs, None, len(books))
                append_dup(athurs, None, len(books))
        elif i == 3:
            if booliance[i]:
                append_dup(pleasure_text, None, len(books))

# test_data = {
#   'title_english': title_english,
#   'title_persian': title_persian,
#   'book_bio': book_bio,
#   'off_percent': off_percent,
#   'current_price': current_price,
#   'rate': rate,
#   'status': status,
#   'publisher_name': publisher_name,
#   'publisher_id': publisher_id,
#   'publisher_link': publisher_link,
#   'writer_name': writer_name,
#   'writer_id': writer_id,
#   'writer_link': writer_link,
#   'ids_book': ids_book,
#   'ids_translations': ids_translations,
#   'link_translations': link_translations,
#   'translations': translations,
#   'shabak': shabak,
#   'pices': pices,
#   'pages': pages,
#   'sunny_date': sunny_date,
#   'monthy_date': monthy_date,
#   'types': types,
#   'seriess': seriess,
#   'reciving_time': reciving_time,
#   'descriptions': descriptions,
#   'book_tags': book_tags,
#   'ids_tags': ids_tags,
#   'english_dialogs': english_dialogs[:-1],
#   'persian_dialogs': persian_dialogs[:-1],
#   'authors': athurs[:-1],
#   'pleasure_text': pleasure_text
# }

# for key, value in test_data.items():
#     print(key, ': ', len(value))
    # print(value if len(value) != 31 else None)
    # print(value if key == 'shabak' else None)

book_df = pd.DataFrame({
  'title_english': title_english,
  'title_persian': title_persian,
  'book_bio': book_bio,
  'off_percent': off_percent,
  'current_price': current_price,
  'rate': rate,
  'status': status,
  'publisher_name': publisher_name,
  'publisher_id': publisher_id,
  'publisher_link': publisher_link,
  'writer_name': writer_name,
  'writer_id': writer_id,
  'writer_link': writer_link,
  'ids_book': ids_book,
  'ids_translations': ids_translations,
  'link_translations': link_translations,
  'translations': translations,
  'shabak': shabak,
  'pices': pices,
  'pages': pages,
  'sunny_date': sunny_date,
  'monthy_date': monthy_date,
  'types': types,
  'seriess': seriess,
  'reciving_time': reciving_time,
  'descriptions': descriptions,
  'book_tags': book_tags,
  'ids_tags': ids_tags,
  'english_dialogs': english_dialogs[:-1],
  'persian_dialogs': persian_dialogs[:-1],
  'authors': athurs[:-1],
  'pleasure_text': pleasure_text
})

book_df.to_csv('books.csv', encoding='utf-8-sig')