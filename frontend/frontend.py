# make connection to database

# read data into pandas dataframe


###
# show the data using pagination for each player
# use streamlit to visualize the data or something
import streamlit as st
import pandas as pd
import numpy as np

# This is almost what I'm looking for I just want to add pagination 
# through all of the top users

st.write("Damn I really didnt finish this part... but you get the point I would call the database and use pagination for each player")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# here I will just query the database