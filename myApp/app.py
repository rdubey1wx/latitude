import streamlit as st
import pandas as pd
import numpy as np


st.write("This is my first website")

users_sports_input = st.text_input("Whats you favourite sports?")

st.write(f"Your favorite **sports** is :=> {users_sports_input}")

st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.header("This is a header with a divider", divider="gray")

st.header("These headers have rotating dividers", divider=True)

st.button("submit")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df) 

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.line_chart(chart_data)