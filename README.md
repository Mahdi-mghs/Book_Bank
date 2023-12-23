# G8_BookBank
main **Library** used:
```
request
numpy
pandas
mysqlConnector
SQLAlchemy
streamlit
```
Main page used is [_IranKetab_](https://www.iranketab.ir/)

# What is _Goal_ ?
Creating a beautiful dashboard and do some null hypothesis :smile:
> All purpose is just showing our skills and knowledge about Analytics, So we don't have any mistrust to "IranKetab" Website

## Step 1 (*Scraping*)

In two separate files named `scrap_link` and `crawl_page`, we have extracted all the necessary and unnecessary information from the target website.

### `scrap_link` File
In the `scrap_link` file, only all the links to the books from all categories (tags) have been extracted and saved in a file named `links.csv`. It takes approximately 60 minutes to extract all the links.

### `crawl_page` File
In the `crawl_page` file, all the essential details such as the book's ISBN, discount amount, print series, tags, etc., have been extracted. Subsidiary information includes footnotes or golden quotes from the book. The final file has an approximate size of 100 megabytes (assuming all links are present) and is saved in CSV format.
> instead of using classical method you can use _pandas\_readHTML_ method, but there is no way to get link of translators or publisher

## Step 2 (*Database*)

In the `cleaner_book` file, all the data is cleaned and then saved in a new CSV file. Following that, in the `ExportDB` file, we segregated the data according to the diagram below, storing it locally. Subsequently, we obtained CSV outputs from the same data.

### File Structure
- `cleaner_book`: Cleans and saves data in a new CSV file.
- `ExportDB`: Segregates data according to the diagram and saves locally.

Diagram:


## Step 3 (*Dashboarding*)



## Step 4 (*Null Hypothesis*)


Include Some statistics tests for finding relationships between features

### First Hypothesis
> Translation has a significant impact on the price of the book

### Second Hypothesis
> There is a significant difference in prices between hardcover and paperback versions

for more details you can check [`first_hyp`](https://github.com/mahdi-mghs/G8_BookBank/blob/main/Req%20Customer/first_hyp.py) & [`second_hyp`](https://github.com/mahdi-mghs/G8_BookBank/blob/main/Req%20Customer/sec_hyp.py)
