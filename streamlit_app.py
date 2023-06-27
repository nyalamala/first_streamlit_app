import streamlit
import pandas


streamlit.title("My Mom's New Healthy Diner ")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 omenga 3 and Blueberry oatmeal")
streamlit.text("🥗  Kale , Spinch and Rocket Smoothie ")
streamlit.text("🐔 Hard Boiled Free Range Egg")
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
