import pandas as pd
import streamlit as st

def category_filter(df):
    categories = st.sidebar.multiselect(
        "Select Category",
        df["Category"].unique(),
        default=df["Category"].unique()
    )
    return categories

def state_filter(df):
    states = st.sidebar.multiselect(
        "Select State",
        df["State"].unique(),
        default=df["State"].unique()
    )
    return states

def chart_type_toggle():
    chart_type = st.sidebar.radio(
        "Select Chart Type",
        ["Bar Chart", "Line Chart"]
    )
    return chart_type

def year_filter(df):

    min_year = int(df["Year"].min())
    max_year = int(df["Year"].max())

    selected_year = st.sidebar.selectbox(
        "Select Year",
        ["All"] + list(range(min_year, max_year + 1))
    )
    return selected_year

def state_year_filter(df):
    return st.sidebar.selectbox(
        "Select Year for Revenue by State",
        sorted(df["Year"].unique())
    )
