import pandas as pd
import plotly.express as px
import streamlit as st

def month(df_selection):

    # SALES BY Month [BAR CHART]
    sales_by_months = df_selection.groupby(by=["Month"])[["Total"]].sum().sort_values(by="Total")
    fig_product_sales = px.bar(
        sales_by_months,
        y=sales_by_months.index,
        x="Total",
        orientation="h",
        title="<b>Total Sales by Bike Month</b>",
        color_discrete_sequence=["#0083B8"] * len(sales_by_months),
        template="plotly_white",
    )
   
    fig_product_sales.update_layout(
        title_font = dict(size=24, color="#f58700"),
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )


    # Number of Bikes Sold BY Month [BAR CHART]
    sales_by_bike_months_qt = df_selection.groupby(by=["Month"])[["Quantity"]].sum().sort_values(by="Quantity")
    fig_product_sales_qt = px.bar(
        sales_by_bike_months_qt,
        x=sales_by_bike_months_qt.index,
        y="Quantity",
        orientation="v",
        title="<b>Total Number of Bikes Sold by Month</b>",
        color_discrete_sequence=["#4379F2"] * len(sales_by_bike_months_qt),
        template="plotly_white",
    )
   
    fig_product_sales_qt.update_layout(
        title_font = dict(size=24, color="#f58700"),
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )


    col_1, col_2 = st.columns(2)
    col_1.plotly_chart(fig_product_sales, use_container_width=True)
    col_2.plotly_chart(fig_product_sales_qt, use_container_width=True)
