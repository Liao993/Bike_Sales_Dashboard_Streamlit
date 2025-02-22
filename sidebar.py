
import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import streamlit as st # type: ignore

def sidebar(df):
    st.sidebar.header("Please Filter Here:")

    multi = st.sidebar.checkbox("View Mutiple Store Location?")
    multi_location = []
    location = None
    if multi:
        multi_location = st.sidebar.multiselect(
        "Select the Store Location:",
        options=df["Store_Location"].unique(),
        default=df["Store_Location"].unique()
        )
    else:
        location = st.sidebar.selectbox(
        "Select the Store Location:",
        df['Store_Location'].unique()
        )

    year = st.sidebar.selectbox(
        "Select the year you want to view:",
        df['Year'].unique()
    )

    gender = st.sidebar.multiselect(
        "Select the Gender:",
        options=df["Gender"].unique(),
        default=df["Gender"].unique()
        )

    ages = df['Age'].unique().tolist()
    age_selection = st.sidebar.slider("Age:",
                        min_value=min(ages),
                        max_value=max(ages),
                        value=(min(ages), max(ages)))
    
    min_age, max_age = age_selection

    df_selection = df.query(
    "Year == @year & (Store_Location == @location | Store_Location == @multi_location) & "
    "Gender == @gender & Age >= @min_age & Age <= @max_age"
    )

    return (df_selection, multi_location, location, year, gender, min_age, max_age)
