
import pandas as pd
import plotly.express as px
import streamlit as st
from sidebar import sidebar
from get_data import get_data
from homepage import homepage

def main():
    #emojis and page title:
    st.set_page_config(page_title="Bike Sales Dashboard",
                    page_icon=":bar_chart:",
                    layout="wide")

    df = get_data()

    df_selection, multi_location, location, year, _, _,_ = sidebar(df)

    homepage(multi_location, location, year, df_selection)

    

    



if __name__ == "__main__":
    main()