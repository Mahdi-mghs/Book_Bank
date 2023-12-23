import numpy as np 
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

All_books=pd.read_csv('Req Customer/All_books.csv')
Author=pd.read_csv('Req Customer/Author.csv')
Book_languages=pd.read_csv('Req Customer/Book_languages.csv')
Book_Tag=pd.read_csv("Req Customer/Book_Tag.csv")
Publisher=pd.read_csv('Req Customer/Publiser.csv')
Tags=pd.read_csv('Req Customer/Tags.csv')
Translation=pd.read_csv('Req Customer/Translation.csv')
Writer=pd.read_csv('Req Customer/Writer.csv')
Book_Writer=pd.read_csv('Req Customer/Book_Writer.csv')
book_translation=pd.read_csv('Req Customer/book_translation.csv')




Book_and_tag_id=pd.merge( All_books, Book_Tag , on='ids_book' , how='inner' )
merged=pd.merge(Book_and_tag_id , Tags, on='ids_tags', how='inner' )
amount_of_books_by_tag_name=merged.groupby('book_tags')['ids_book'].count().reset_index()

amount_of_book_by_publisher=All_books.groupby('publisher_name')['ids_book'].count().reset_index()
amount_of_book_by_publisher=amount_of_book_by_publisher.sort_values(by='ids_book', ascending=False)
amount_of_book_by_publisher10=amount_of_book_by_publisher.head(10)


All_books_copy01=All_books.copy()
All_books_copy01 = All_books_copy01[~((All_books_copy01['sunny_date'].isna()) | (All_books_copy01['sunny_date'] == np.inf)  | (All_books_copy01['sunny_date'].isnull()))]
All_books_copy01['sunny_date'] = All_books_copy01['sunny_date'].astype(int)
All_books_copy01['sunny_date'] = All_books_copy01['sunny_date'].astype(str).apply(lambda x: int(x[:-1]) if len(x) == 5 else int(x))

amount_of_book_by_year=All_books_copy01.groupby('sunny_date')['ids_book'].count().reset_index()
amount_of_book_by_year= amount_of_book_by_year[~((amount_of_book_by_year['sunny_date']>1402) | (amount_of_book_by_year['sunny_date']<1319))]


bookw=pd.merge(Book_Writer , Writer , on='writer_id' , how='inner')
amount_of_book_by_writer=bookw.groupby(['writer_id','writer_name'])['ids_book'].count().reset_index().sort_values(by=['ids_book'] , ascending=False)

amount_of_book_by_pices=All_books.groupby('pices')['ids_book'].count().reset_index()
amount_of_book_by_pices=amount_of_book_by_pices.sort_values(by=['ids_book'] , ascending=False)

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
        body {
            background-color: #f7dd59;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Analysis of books on IranKetab site')
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

####################################################################################################################################


#1
st.header('Display the number of books by tag')


st.bar_chart(amount_of_books_by_tag_name.set_index('book_tags'))
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

#2
st.header('The top ten publishers in terms of number of books ')
st.bar_chart(amount_of_book_by_publisher10.set_index('publisher_name'))
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

#3
st.header('Number of books by year of publication')
st.bar_chart(amount_of_book_by_year.set_index('sunny_date'))
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

#4
st.header('Showing the number of books of the top ten authors from the perspective of the number of books')
amount_of_book_by_writer10 = amount_of_book_by_writer.iloc[1:11]
st.bar_chart(amount_of_book_by_writer10.drop(columns=['writer_id']).set_index('writer_name'))
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

#5
st.header('Showing the number of books of the top ten translators from the perspective of the number of books')
book_motarjem=book_translation.groupby('translations')['ids_book'].count().reset_index()
book_motarjem=book_motarjem.sort_values(by=['ids_book'] , ascending=False).reset_index()
book_motarjem=book_motarjem.drop(columns=['index'])
book_motarjem10=book_motarjem.head(10)
st.bar_chart(book_motarjem10.set_index('translations'))
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

#6
st.header('Scatter diagram of the average number of book pages and year of publication')
year_page=All_books_copy01.groupby('sunny_date')['pages'].mean().reset_index()
year_page=year_page.iloc[4:-8]
fig, ax = plt.subplots()
ax.scatter(year_page['sunny_date'], year_page['pages'])
ax.set_xlabel('year')
ax.set_ylabel('number of book page')
ax.set_facecolor('#f0f8ff')  # Set background color

st.pyplot(fig)
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

#7
st.header('Scatter diagram of the average number of book price and year of publication')

year_price=All_books_copy01.groupby('sunny_date')['current_price'].mean().reset_index()
year_price=year_price.iloc[4:-8]
fig , ax = plt.subplots()
ax.scatter(year_price['sunny_date'],year_price['current_price'])
ax.set_xlabel('year')
ax.set_ylabel('price(tooman)')
ax.set_facecolor('#f0f8ff')  # Set background color

st.pyplot(fig)
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

#8
st.header('Scatter plot of average price by rate')
price_rate=All_books_copy01.groupby('rate')['current_price'].mean().reset_index()
price_rate=price_rate.iloc[1:]
fig , ax = plt.subplots()
ax.scatter(price_rate['rate'],price_rate['current_price'])
ax.set_ylabel('price')
ax.set_xlabel('rate')
ax.set_facecolor('#f0f8ff')  # Set background color


st.pyplot(fig)
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

#9

st.header('Display the number of books according to their cut type')
pices_book=All_books_copy01.groupby('pices')['ids_book'].count().reset_index()

st.bar_chart(pices_book.set_index('pices'))
st.markdown("<hr style='border: 2px solid #1f77b4; border-width: 0px 0px 2px 0px; background-color:#1f77b4;'>", unsafe_allow_html=True)

###############################section2

selected_columns = ['sunny_date', 'book_tags', 'current_price', 'title_english', 'title_persian', 'publisher_id',
                    'publisher_name', 'ids_book', 'ids_tags', 'rate']

# Create a subDataFrame with specific columns
sub_df = merged[selected_columns]
sub_df = pd.merge(sub_df, Book_Writer, on='ids_book', how='inner')
sub_df = pd.merge(sub_df, Writer, on='writer_id', how='inner')

st.sidebar.title('Filter Box')  # Add a title to the filter box



# Sidebar filters with conditional visibility
enable_genre_filter = st.sidebar.checkbox('Enable Genre Filter', value=True)
genre_options = sub_df['book_tags'].unique() if enable_genre_filter else ['']
genre = st.sidebar.selectbox('Select Genre', genre_options)

enable_publisher_filter = st.sidebar.checkbox('Enable Publisher Filter', value=True)
publisher_options = sub_df['publisher_name'].unique() if enable_publisher_filter else ['']
publisher = st.sidebar.selectbox('Select Publisher', publisher_options)

enable_writer_filter = st.sidebar.checkbox('Enable Writer Filter', value=True)
writer_options = sub_df['writer_name'].unique() if enable_writer_filter else ['']
writer = st.sidebar.selectbox('Select Writer', writer_options)

enable_min_rate_filter = st.sidebar.checkbox('Enable Minimum Rate Filter', value=True)
enable_max_price_filter = st.sidebar.checkbox('Enable Maximum Price Filter', value=True)

min_rate = st.sidebar.slider('Minimum Rate', min_value=0.0, max_value=5.0, value=0.0) if enable_min_rate_filter else 0.0
max_price = st.sidebar.slider('Maximum Price', min_value=0.0, max_value=sub_df['current_price'].max(),
                              value=sub_df['current_price'].max()) if enable_max_price_filter else sub_df['current_price'].max()

# Apply filters
filtered_df = sub_df[
    ((sub_df['book_tags'] == genre) if enable_genre_filter else True) &
    ((sub_df['publisher_name'] == publisher) if enable_publisher_filter else True) &
    ((sub_df['writer_name'] == writer) if enable_writer_filter else True) &
    ((sub_df['rate'] >= min_rate) if enable_min_rate_filter else True) &
    ((sub_df['current_price'] <= max_price) if enable_max_price_filter else True)
]

# Display filtered results
st.sidebar.subheader('Filtered Books:')
st.sidebar.table(filtered_df[['title_english', 'title_persian']].reset_index(drop=True).drop_duplicates())


