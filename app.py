import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown('''
# Exploratory Data Analysis App
- This app performs EDA based upon the Pandas Profiling Report!
- App built by Pranav Sawant and Anshuman Shukla of Team Skillocity
- Note: Data inputs are taken from the sidebar at the top left of the page (arrow symbol). User dataset can be added from the sidebar and a sample dataset has also been provided for convenience.
- Tap the button named 'Sample Dataset' to obtain a report for the Pima Indian Diabetes Dataset. 
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV dataset'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file for EDA", type=["csv"])
    st.sidebar.markdown("""
[Sample CSV input file](https://github.com/pranav-coder2005/Diabetes_detector/blob/main/diabetes.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Waiting for CSV file to be uploaded.')
    if st.button('Sample Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
