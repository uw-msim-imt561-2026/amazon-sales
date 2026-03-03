import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def load_data(path: str) -> pd.DataFrame:

    df = pd.read_csv(path)

    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    df["Year"] = df["OrderDate"].dt.year
    df["Month"] = df["OrderDate"].dt.month
    df['YearMonth'] = df['OrderDate'].dt.strftime('%Y-%m')
    df["MonthName"] = df["OrderDate"].dt.strftime("%b")
    df['TaxRate'] = df['Tax'] / (df['TotalAmount'] - df['ShippingCost'])

    return df
