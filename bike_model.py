import pandas as pd
import plotly.express as px
import streamlit as st

def bike_model(df_selection):

    # SALES BY BIKE MODEL [BAR CHART]
    sales_by_bike_model = df_selection.groupby(by=["Bike_Model"])[["Total"]].sum().sort_values(by="Total")
    fig_product_sales = px.bar(
        sales_by_bike_model,
        y=sales_by_bike_model.index,
        x="Total",
        orientation="h",
        title="<b>Total Sales by Bike Model</b>",
        color_discrete_sequence=["#0083B8"] * len(sales_by_bike_model),
        template="plotly_white",
    )
    fig_product_sales.update_layout(
        title_font = dict(size=24, color="#ffde21"),
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )


    # SALES BY BIKE MODEL [BAR CHART]
    sales_by_bike_model_qt = df_selection.groupby(by=["Bike_Model"])[["Quantity"]].sum().sort_values(by="Quantity")
    fig_product_sales_qt = px.bar(
        sales_by_bike_model_qt,
        x=sales_by_bike_model_qt.index,
        y="Quantity",
        orientation="v",
        title="<b>Total Number of Bikes Sold by Bike Model</b>",
        color_discrete_sequence=["#4379F2"] * len(sales_by_bike_model_qt),
        template="plotly_white",
    )
    fig_product_sales_qt.update_layout(
        title_font = dict(size=24, color="#ffde21"),
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )


    col_1, col_2 = st.columns(2)
    col_1.plotly_chart(fig_product_sales, use_container_width=True)
    col_2.plotly_chart(fig_product_sales_qt, use_container_width=True)


#orange f58700