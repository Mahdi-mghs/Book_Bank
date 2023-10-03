import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="BOOK_DASHBORD",
                   page_icon=":bar_chart:",
                   layout = "wide")

dataframe1 = pd.read_csv("Book_Tag.csv")

# Dashboard title
st.title("Data Visualization Dashboard")

# Add interactive widgets
st.sidebar.header("Settings")

data_option = st.sidebar.selectbox("Select Data", ["Data 1", "Data 2", "Data 3"])

# Display data
st.write(f"You've selected '{dataframe1}' data.")

st.title("تعداد کتاب‌ها بر حسب تگ")

# dataframe1 = pd.read_csv("i:\DARS\Boot Camp\project\Book_Tag.csv")
fig, ax = plt.subplots()
tag_counts = dataframe1['ids_tags'].value_counts()

ax.bar(tag_counts.index, tag_counts.values)
plt.xlabel("Tag")
plt.ylabel("number of books")
plt.xticks(rotation=90)
st.pyplot()

st.write(tag_counts)

# dataframe3 = pd.read_csv("Book_Writer.csv")
# dataframe4 = pd.read_csv("Writer.csv")
# merged_df = pd.merge(dataframe3, dataframe4, on='writer_id', how='inner')
# book_counts = merged_df.groupby('writer_id').size().reset_index(name='book_counts')

# st.title("best writer.number of books")

# # نمودار بارپلات
# fig, ax = plt.subplots()
# ax.bar(merged_df["writer_name"], merged_df['book_counts'], color='royalblue')
# ax.set_xlabel("writer_name")
# ax.set_ylabel('book_counts')
# ax.set_title("best writer.number of books")
# plt.xticks(rotation=45, ha="right")  # چرخش نام نویسنده‌ها به افقی

# # نمایش نمودار
# st.pyplot(fig)

dataframe5 = pd.read_csv("All_bools.csv")
st.title('AVGpage per year')
# نمودار پراکندگی
fig, ax = plt.subplots()
ax.scatter(dataframe5['year'], dataframe5['page'], color='blue', alpha=0.7)
ax.set_xlabel('year')
ax.set_ylabel( 'AVGpage')
ax.set_title('AVGpage per year')
st.pyplot(fig)