from io import StringIO
import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center;'>Candidate Elimination Algorithm</h1>", unsafe_allow_html=True)

st.write("The candidate elimination algorithm incrementally builds the version space given a hypothesis space H and a set E of examples. The candidate elimination algorithm does this by updating the general and specific boundary for each new example. ")

uploaded_file = st.file_uploader("Upload a CSV file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

