import streamlit as st
from src.charts import (
    sales_overview,
    revenue_by_states,
    tax_impact,
    sales_by_payment,
    correlation_analysis,
    state_choropleth_map,
    top_states_bar_chart
)
from src.filters import (
    category_filter,
    state_filter,
    year_filter,
    chart_type_toggle,
    state_year_filter
)

def render_homepage():
    st.markdown(
        """
        <div style="background-color:#f8f9fa; padding: 2rem; border-radius: 16px; margin-bottom: 1rem;">
            <p style="font-size: 1.05rem; color: #4f4f4f; line-height: 1.6;">
                This dashboard is designed to support data-driven decision making by presenting
                interactive views of Amazon sales performance across geography, product categories,
                payment behavior, and variable relationships.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Stakeholders")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="background-color:white; padding:1.2rem; border-radius:14px; border:1px solid #e6e6e6; min-height:190px;">
                <h4>Primary Audience</h4>
                <p>
                The primary audience for this dashboard is the <b>Amazon Sales Team</b>.
                The dashboard helps sales staff evaluate market performance, compare regions,
                identify category trends, and better understand customer purchasing patterns.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="background-color:white; padding:1.2rem; border-radius:14px; border:1px solid #e6e6e6; min-height:190px;">
                <h4>Other Stakeholders</h4>
                <p>
                Other stakeholders may include <b>marketing teams, business analysts, and product managers</b>.
                These groups can use the dashboard to assess promotional effectiveness, explore product demand,
                and support broader strategic planning.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Questions Answered by the Dashboard")
    st.markdown(
        """
        <div style="background-color:white; padding:1.2rem; border-radius:14px; border:1px solid #e6e6e6;">
            <ul style="line-height:1.8;">
                <li>Which geographic regions generate the highest and lowest sales?</li>
                <li>How do product category sales change over time?</li>
                <li>How do payment methods and discounts relate to customer spending?</li>
                <li>What relationships exist among major numerical variables in the dataset?</li>
                <li>Which areas of sales performance may require strategic attention?</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Visualization Guide")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div style="background-color:white; padding:1.2rem; border-radius:14px; border:1px solid #e6e6e6; margin-bottom:1rem;">
                <h4>Geographic Sales Analysis</h4>
                <p>
                Shows sales performance across states and helps identify regional patterns,
                high-performing markets, and low-performing areas.
                </p>
            </div>

            <div style="background-color:white; padding:1.2rem; border-radius:14px; border:1px solid #e6e6e6;">
                <h4>Category Sales Overview</h4>
                <p>
                Compares category performance over time and reveals growth patterns,
                decline, and possible seasonal variation.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div style="background-color:white; padding:1.2rem; border-radius:14px; border:1px solid #e6e6e6; margin-bottom:1rem;">
                <h4>Payment Method and Discount Analysis</h4>
                <p>
                Examines how payment choices and discount levels relate to total order amount,
                helping users interpret customer purchasing behavior.
                </p>
            </div>

            <div style="background-color:white; padding:1.2rem; border-radius:14px; border:1px solid #e6e6e6;">
                <h4>Correlation Analysis</h4>
                <p>
                Summarizes numerical relationships within the dataset and helps identify
                variables that may be associated with sales performance.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Dashboard Value")
    st.info(
        "Together, these visualizations provide a multi-dimensional view of sales performance and support more informed decisions about market focus, product strategy, and customer behavior."
    )

def render_dashboard(df):

    st.title("📊 Amazon Sales Dashboard")

    page = st.sidebar.selectbox(
        "Select Dashboard View",
        [
            "Homepage",
            "State Map Analysis",
            "Sales Overview",
            "Payment Method",
            "Correlation Analysis",
        ]
    )

    if page == "Homepage":
        render_homepage()

    elif page == "Sales Overview":
        st.subheader("Category Sales Overview")
        st.markdown("This page shows performance over time and reveals growth patterns, decline, and possible seasonal variation.")
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
        st.subheader("Payment Method Analysis")
        st.markdown("This page shows how payment choices and discount levels relate to total order amount, helping users interpret customer purchasing behavior.")
        selected_year = year_filter(df)
        sales_by_payment(df, selected_year)

    elif page == "Correlation Analysis":
        st.subheader("Correlation Analysis")
        st.markdown("This page summarizes numerical relationships within the dataset and helps identify variables that may be associated with sales performance.")
        correlation_analysis(df)

    elif page == "State Map Analysis":
        selected_year = year_filter(df)

        metric = st.sidebar.selectbox(
            "Select Map Metric",
            ["TotalSales", "AvgTaxRate", "AvgDiscount"],
            format_func=lambda x: {
                "TotalSales": "Total Sales",
                "AvgTaxRate": "Average Tax Rate",
                "AvgDiscount": "Average Discount"
            }[x]
        )

        st.subheader("Geographic Sales Analysis")
        st.markdown("This page shows state-level patterns in sales, tax rate, and discount across the United States.")

        col1, col2, col3 = st.columns(3)
        filtered_df = df if selected_year == "All" else df[df["Year"] == selected_year]

        col1.metric("Total Sales", f"{filtered_df['TotalAmount'].sum():,.2f}")
        col2.metric("Average Tax Rate", f"{filtered_df['TaxRate'].mean():.2f}")
        col3.metric("Average Discount", f"{filtered_df['Discount'].mean():.2f}")

        left_col, right_col = st.columns([1.4, 1])

        with left_col:
            state_choropleth_map(df, metric, selected_year)

        with right_col:
            top_states_bar_chart(df, selected_year)

        st.subheader("State-Level Summary")
        summary_df = (
            filtered_df.groupby("State", as_index=False)
            .agg(
                TotalSales=("TotalAmount", "sum"),
                AvgTaxRate=("TaxRate", "mean"),
                AvgDiscount=("Discount", "mean")
            )
            .sort_values("TotalSales", ascending=False)
            .reset_index(drop=True)
        )
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
