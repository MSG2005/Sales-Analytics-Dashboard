import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

# Load data
df = pd.read_csv("data/processed/cleaned_sales_data.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ===============================
# SIDEBAR FILTERS
# ===============================
st.sidebar.header("Filter Data")

region = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

filtered_df = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category))
]

# ===============================
# TITLE & KPIs
# ===============================
st.title("📊 Sales Performance Dashboard")

k1, k2, k3 = st.columns(3)
k1.metric("Total Sales", f"₹{filtered_df['Sales'].sum():,.0f}")
k2.metric("Total Orders", filtered_df['Order ID'].nunique())
k3.metric("Total Customers", filtered_df['Customer ID'].nunique())

st.divider()

# ===============================
# ROW 1: CATEGORY & REGION
# ===============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    fig1, ax1 = plt.subplots(figsize=(5, 3))
    sns.barplot(data=filtered_df, x='Category', y='Sales', estimator=sum, ax=ax1)
    ax1.tick_params(axis='x', rotation=30)
    st.pyplot(fig1, use_container_width=True)

with col2:
    st.subheader("Sales by Region")
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    sns.barplot(data=filtered_df, x='Region', y='Sales', estimator=sum, ax=ax2)
    ax2.tick_params(axis='x', rotation=30)
    st.pyplot(fig2, use_container_width=True)

# ===============================
# ROW 2: MONTHLY TREND & CUSTOMER SEGMENTS
# ===============================
# ===============================
# FULL-WIDTH MONTHLY SALES TREND
# ===============================
st.subheader("Monthly Sales Trend")

monthly = (
    filtered_df
    .groupby(filtered_df['Order Date'].dt.to_period("M"))['Sales']
    .sum()
    .reset_index()
)

monthly['Order Date'] = monthly['Order Date'].astype(str)

# Full-width container
with st.container():
    fig, ax = plt.subplots(figsize=(12, 4))  # wider chart

    sns.lineplot(
        data=monthly,
        x='Order Date',
        y='Sales',
        marker='o',
        linewidth=2,
        ax=ax
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.set_title("Monthly Sales Trend")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig, use_container_width=True)

# Customer Segments
    st.subheader("Customer Segments")

    rfm = filtered_df.groupby('Customer ID').agg({
        'Order Date': lambda x: (filtered_df['Order Date'].max() - x.max()).days,
        'Order ID': 'nunique',
        'Sales': 'sum'
    }).reset_index()

    rfm.columns = ['Customer_ID', 'Recency', 'Frequency', 'Monetary']

    rfm['Segment'] = pd.qcut(rfm['Monetary'], 4, labels=['Low', 'Medium', 'High', 'Very High'])

    fig4, ax4 = plt.subplots(figsize=(5, 3))
    sns.countplot(x='Segment', data=rfm, ax=ax4)
    st.pyplot(fig4, use_container_width=True)
