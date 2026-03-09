import streamlit as st
from src.data import load_data
from src.layouts import render_dashboard

st.set_page_config(layout="wide")

def main():
    df = load_data("data/Amazon.csv")
    render_dashboard(df)

if __name__ == "__main__":
    main()