import streamlit as st
from src.charts import (
    sales_overview,
    revenue_by_states,
    tax_impact,
    sales_by_payment,
    correlation_analysis
)
from src.filters import (
    category_filter,
    state_filter,
    year_filter,
    chart_type_toggle,
    state_year_filter
)

def render_dashboard(df):

    st.title("📊 Amazon Sales Dashboard")

    page = st.sidebar.selectbox(
        "Select Dashboard View",
        [
            "Sales Overview",
            "Revenue by State",
            "Tax Impact",
            "Payment Method",
            "Correlation Analysis"
        ]
    )

    if page == "Sales Overview":
        categories = category_filter(df)
        selected_year = year_filter(df)
        chart_type = chart_type_toggle()
        sales_overview(df, categories, selected_year, chart_type)


    elif page == "Revenue by State":

        selected_states = state_filter(df)
        selected_year = state_year_filter(df)
        revenue_by_states(df, selected_states, selected_year)

    elif page == "Tax Impact":
        selected_year = state_year_filter(df)
        tax_impact(df, selected_year)

    elif page == "Payment Method":
        selected_year = year_filter(df)
        sales_by_payment(df, selected_year)

    elif page == "Correlation Analysis":
        correlation_analysis(df)