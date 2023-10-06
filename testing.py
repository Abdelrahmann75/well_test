import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(layout="wide")
conn = sqlite3.connect('D:/Work_files\MyData.db')

sql_query1 = '''SELECT Datee, WellName, GrossTest, NetOil FROM DailyProduction
                INNER JOIN WellTest ON DailyProduction.ID = WellTest.DailyProdID'''

df = pd.read_sql_query(sql_query1, conn)

df['Datee'] = pd.to_datetime(df['Datee'], errors='coerce')

unique_dates = df['Datee'].dt.strftime('%Y-%m-%d').unique().tolist()
default_date = unique_dates[-1]


col1, col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,1])

with col1:
    selected_date1 = st.selectbox("Date_1", unique_dates, index=len(unique_dates) - 1)

with col2:
    selected_date2 = st.selectbox('Date_2', unique_dates, index=len(unique_dates) - 1)

df_selection = df.query('@selected_date1 <= Datee <= @selected_date2')

df_selection['Datee'] = df_selection['Datee'].dt.strftime('%Y-%m-%d')
st.dataframe(df_selection)



with col3:
    button1=st.button('Export to csv')
    if button1:
        myfile = 'well_test.csv'
        df_selection.to_csv(myfile)
        os.startfile(myfile)