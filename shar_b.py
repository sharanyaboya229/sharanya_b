import streamlit

streamlit.title('love country')
streamlit.header('all')
streamlit.text('india')
streamlit.text('canada')
streamlit.text('UK')

streamlit.title('healthy dite')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
