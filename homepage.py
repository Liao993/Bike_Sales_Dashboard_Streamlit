import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import streamlit as st # type: ignore
from topkpi import topkpi
from bike_model import bike_model
from month import month

def homepage(multi_location, location, year, df_selection):
     # ---- MAINPAGE ----
    st.title(":bike: Bikes Sales Dashboard")
    st.markdown("##")
    if location != None:
        st.subheader(f"Sales Performance in {year} in {location}")
    else:
        location_string = ", ".join(multi_location)
        st.subheader(f"Sales Performance in {year} in {location_string}")

    st.markdown("######")

    topkpi(df_selection)

    st.markdown("---")

    bike_model(df_selection)

    st.markdown("---")

    month(df_selection)

    st.markdown("---")

    st.subheader(f'Explore More Details')

    st.dataframe(df_selection.drop(columns= ["Payment_Method" ]))