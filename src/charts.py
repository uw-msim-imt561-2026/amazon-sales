import streamlit as st
import plotly.express as px
import numpy as np

def sales_overview(df, categories, selected_year, chart_type):

    if selected_year != "All":
        df = df[df["Year"] == selected_year]

    if selected_year == "All":

        grouped = (
            df.groupby(["Year", "Month"])["TotalAmount"]
            .sum()
            .reset_index()
        )

        if chart_type == "Bar Chart":
            fig = px.bar(
                grouped,
                x="Month",
                y="TotalAmount",
                color="Year",
                barmode="group",
                title="Monthly Sales (All Years)"
            )
        else:
            fig = px.line(
                grouped,
                x="Month",
                y="TotalAmount",
                color="Year",
                markers=True,
                title="Monthly Sales Trend (All Years)"
            )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Total Sales"
        )

    else:

        df = df[df["Category"].isin(categories)]

        grouped = (
            df.groupby(["Month", "Category"])["TotalAmount"]
            .sum()
            .reset_index()
        )

        if chart_type == "Bar Chart":
            fig = px.bar(
                grouped,
                x="Month",
                y="TotalAmount",
                color="Category",
                barmode="group",
                title=f"Monthly Sales by Category ({selected_year})"
            )
        else:
            fig = px.line(
                grouped,
                x="Month",
                y="TotalAmount",
                color="Category",
                markers=True,
                title=f"Monthly Sales Trend by Category ({selected_year})"
            )

        fig.update_layout(
            xaxis_title=f"Month ({selected_year})",
            yaxis_title="Total Sales"
        )

    fig.update_xaxes(
        tickmode="linear",
        dtick=1,
        range=[1, 12]
    )

    st.plotly_chart(fig, use_container_width=True)

def revenue_by_states(df, states, year):

    filtered_df = df[
        (df["State"].isin(states)) &
        (df["Year"] == year)
    ]

    grouped = (
        filtered_df
        .groupby("State")["TotalAmount"]
        .sum()
        .reset_index()
    )

    grouped = grouped.sort_values(
        "TotalAmount",
        ascending=False
    )

    fig = px.bar(
        grouped,
        x="State",
        y="TotalAmount",
        title=f"Total Revenue by States - {year}"
    )

    st.plotly_chart(fig, use_container_width=True)


def tax_impact(df, year):
    df = df[df["Year"] == year]

    grouped = (
        df.groupby(["Year", "State"])
        .agg({"TaxRate": "mean", "TotalAmount": "sum"})
        .reset_index()
    )

    fig = px.scatter(
        grouped,
        x="TaxRate",
        y="TotalAmount",
        trendline="ols",
        title=f"Tax Rate Impact on Sales Volume - {year}"
    )

    st.plotly_chart(fig, use_container_width=True)


def sales_by_payment(df, selected_year):

    if selected_year == "All":

        grouped = (
            df.groupby("PaymentMethod")["TotalAmount"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            grouped,
            x="PaymentMethod",
            y="TotalAmount",
            title="Total Sales by Payment Method (All Years)"
        )

        fig.update_layout(
            xaxis_title="Payment Method",
            yaxis_title="Total Sales"
        )


    else:

        df = df[df["Year"] == selected_year]

        fig = px.box(
            df,
            x="PaymentMethod",
            y="TotalAmount",
            color="Discount",
            title=f"Payment Methods and Discounts over Total Amount ({selected_year})"
        )

        fig.update_layout(
            xaxis_title="Payment Method",
            yaxis_title="Total Amount"
        )

    st.plotly_chart(fig, use_container_width=True)

def correlation_analysis(df):

    numeric_df = df.select_dtypes(include=np.number)

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Matrix Heatmap"
    )

    fig.update_layout(
        height=700,
        width=900
    )

    st.plotly_chart(fig, use_container_width=True)

def state_choropleth_map(df, metric, selected_year="All"):
    if selected_year != "All":
        df = df[df["Year"] == selected_year]

    grouped = (
        df.groupby("State", as_index=False)
        .agg(
            TotalSales=("TotalAmount", "sum"),
            AvgTaxRate=("TaxRate", "mean"),
            AvgDiscount=("Discount", "mean")
        )
    )

    metric_title = {
        "TotalSales": "Total Sales by State",
        "AvgTaxRate": "Average Tax Rate by State",
        "AvgDiscount": "Average Discount by State"
    }

    # Always create one shared plotting column
    if metric == "TotalSales":
        grouped["MapValue"] = np.log1p(grouped["TotalSales"])
        colorbar_title = "Log Sales"
    else:
        grouped["MapValue"] = grouped[metric]
        colorbar_title = metric_title[metric]

    fig = px.choropleth(
        grouped,
        locations="State",
        locationmode="USA-states",
        color="MapValue",
        hover_name="State",
        scope="usa",
        color_continuous_scale="Blues",
        title=metric_title[metric],
        hover_data={
            "TotalSales": ":,.2f",
            "AvgTaxRate": ":.2f",
            "AvgDiscount": ":.2f",
            "MapValue": False
        }
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=50, b=0),
        coloraxis_colorbar_title=colorbar_title
    )

    st.plotly_chart(fig, use_container_width=True)

def top_states_bar_chart(df, selected_year="All", top_n=10):
    if selected_year != "All":
        df = df[df["Year"] == selected_year]

    grouped = (
        df.groupby("State", as_index=False)["TotalAmount"]
        .sum()
        .sort_values("TotalAmount", ascending=False)
        .head(top_n)
    )

    fig = px.bar(
        grouped,
        x="State",
        y="TotalAmount",
        title=f"Top {top_n} States by Total Sales",
        text_auto=".2s"
    )

    fig.update_layout(
        xaxis_title="State",
        yaxis_title="Total Sales"
    )

    st.plotly_chart(fig, use_container_width=True)
