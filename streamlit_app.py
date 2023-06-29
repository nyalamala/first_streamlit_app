import streamlit
import pandas
import snowflake
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title("My Mom's New Healthy Diner ")
streamlit.header("Breakfast Favorites")
streamlit.text("🥣 omenga 3 and Blueberry oatmeal")
streamlit.text("🥗  Kale , Spinch and Rocket Smoothie ")
streamlit.text("🐔 Hard Boiled Free Range Egg")
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#new section to display fruits ================================================
def get_fruityvice_data(fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())  
     return fruityvice_normalized



streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
      streamlit.error('Please select fruit to get information..')
   else:
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
   streamlit.error()

#query the fruit data
streamlit.header("The fruit load list contains :")
#snowflake functions
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
          return my_cur.fetchall()

#add a button lo load the fruit data
if streamlit.button('get fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_row=get_fruit_load_list()
   streamlit.dataframe(my_data_row)
#dont run anything past here
streamlit.stop()





#allow end user to add fruit in the list
add_my_fruit=streamlit.text_input('What fruit would you like to add : ','jackfruit')  
streamlit.write('Thanks for adding  ', add_my_fruit)


#this will not work properly just go with the flow
my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")



















