import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import streamlit as st # type: ignore

def topkpi(df_selection):
    #TOP KPI's
    total_transation = int(df_selection['Sale_ID'].count())
    total_sales = int(df_selection["Total"].sum())
    average_sale_by_selection = round(df_selection["Total"].mean(),2)
    top_salesperson = df_selection.groupby(by=["Sales_Person"])[["Total"]].sum().sort_values(by="Total", ascending=False).rename(columns={"Total": "Total_Sales"}).reset_index()
    top_salesperson_name = top_salesperson.iloc[0]["Sales_Person"]
    top_salesperson_sales = int(top_salesperson.iloc[0]["Total_Sales"])

    col_1, col_2, col_3, col_4, col_5 =st.columns(5)
    with col_1:
        st.markdown(f'<h3 style="color: #B1D690;">Total Transaction</h3>', unsafe_allow_html=True)
        st.subheader(f"{total_transation}")
    with col_2:
        st.markdown(f'<h3 style="color: #B1D690;">Total Sales</h3>', unsafe_allow_html=True)
        st.subheader(f"US $ {total_sales:,}")
    with col_3:
        st.markdown(f'<h3 style="color: #B1D690;">Average Sales</h3>', unsafe_allow_html=True)
        st.subheader(f"US $ {average_sale_by_selection:,}")
    with col_4:
        st.empty()  # Create a placeholder for the content
        st.markdown("<br>" * 1, unsafe_allow_html=True)  # Adjust the number of breaks for vertical spacing
        st.markdown(f'<h3 style="color: #F95454;">Our Best Seller</h3>', unsafe_allow_html=True)
        
    with col_5:
        st.subheader(f'{top_salesperson_name}')
        st.subheader(f"US $ {top_salesperson_sales:,}")
