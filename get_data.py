import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import streamlit as st # type: ignore

@st.cache_data
def get_data():
    file_1 = "bike_sales.csv"
    file_2 = "Salesperson_name.csv"
    db1 = pd.read_csv(file_1)
    db2 = pd.read_csv(file_2)
    df = pd.merge(db1, db2, on='Salesperson_ID', how='inner')
    df = df.rename(columns={"Customer_Gender": "Gender", "Customer_Age":"Age"})
    df['Total'] = df["Price"] * df["Quantity"]
    # Convert the 'date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', dayfirst=True)

    # Extract month and year
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    return df