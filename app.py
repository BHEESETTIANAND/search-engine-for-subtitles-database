import streamlit as st
import pandas as pd

df=pd.read_csv("final_data.csv")

st.title("Search Engine For Movie Sub-titles DataBase")

user_input = st.text_input("enter user query related to movie subtitles")

results = df[df['ncc'].str.contains(user_input, case=False)]['name'].tolist()

if st.button("search"):
    
    if len(results)==0:
        st.write("user searched query is not present in the database")
    else:
        st.write(results)
