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

![Book (1)](https://github.com/amiralira/G8_BookBank/assets/47474659/6fca7860-557a-4c27-a429-d533046bbe99)

## Step 3 (*Dashboarding*)
In `st_git` file we create a dynamic dashboard with streamlit library. 

In this dashboard, graphs about the frequency of books of each genre, the number of books by top authors, translators and publishers, books published in different years, the frequency of books based on the type of cover, as well as the distribution of book prices based on the year of publication and book rating are displayed in has come

There is also a search section where the user can search for the desired book by specifying the maximum price, minimum score, author, publisher and book genre.

In the figure below, a view of the dashboard is displayed:
![qbctd](https://github.com/amiralira/G8_BookBank/assets/77622627/89bc7e66-768c-4d9f-82c8-2c07f07943eb)

> You can check final result here [Streamlit_Dashboard](https://bookbank-st.streamlit.app/) 🕶️

## Step 4 (*Null Hypothesis*)


Include Some statistics tests for finding relationships between features

### First Hypothesis
> Translation has a significant impact on the price of the book

### Second Hypothesis
> There is a significant difference in prices between hardcover and paperback versions

for more details you can check [`first_hyp`](https://github.com/mahdi-mghs/G8_BookBank/blob/main/Req%20Customer/first_hyp.py) & [`second_hyp`](https://github.com/mahdi-mghs/G8_BookBank/blob/main/Req%20Customer/sec_hyp.py)
