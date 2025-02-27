import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide")

st.markdown('''
# Exploratory Data Analysis App
This app performs EDA based on the Pandas Profiling Report!
- App built by Abdul Haq of Team Skillocity
- Note: Data inputs are taken from the sidebar. User dataset can be uploaded or a sample dataset can be used.
''')

with st.sidebar.header('1. Upload your CSV dataset'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file for EDA", type=["csv"])
    st.sidebar.markdown("""
[Sample CSV input file](https://raw.githubusercontent.com/pranav-coder2005/Diabetes_detector/main/diabetes.csv)
""")

@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

@st.cache_data
def generate_profile_report(df):
    return ProfileReport(df, explorative=True)

if uploaded_file is not None:
    df = load_csv(uploaded_file)
    pr = generate_profile_report(df)
    st.header('**Input Data Frame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Waiting for CSV file to be uploaded.')
    if st.button('Use Sample Dataset'):
        sample_df = load_csv('https://raw.githubusercontent.com/pranav-coder2005/Diabetes_detector/main/diabetes.csv')
        pr = generate_profile_report(sample_df)
        st.header('**Input Data Frame (Sample Data)**')
        st.write(sample_df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

st.sidebar.markdown('---')

