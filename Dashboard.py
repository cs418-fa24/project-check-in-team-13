import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

st.title("Stock Market Analysis Dashboard")
st.markdown("""
This dashboard provides an analysis of stock performance across sectors and indices, visualizes trends around significant events, and detects anomalies in stock volatility.
""")

sector_choice = st.sidebar.selectbox(
    "Choose a Sector",
    ["Defense", "Tech", "Healthcare", "Energy", "Index"]
)

start_date = st.sidebar.date_input("Start Date", value=pd.Timestamp("2019-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.Timestamp("2024-01-01"))

tickers = {
    "Defense": ["LMT", "RTX", "GD", "NOC"],
    "Tech": ["AAPL", "MSFT", "GOOGL", "NVDA", "META"],
    "Healthcare": ["JNJ", "PFE", "MRK", "ABBV", "UNH"],
    "Energy": ["XOM", "CVX", "COP", "SLB", "BP"],
    "Index": ["^GSPC", "^IXIC", "^DJI"],
}

@st.cache_data
def load_data(tickers, start, end):
    return yf.download(tickers, start=start, end=end)['Adj Close'].dropna()

selected_tickers = tickers[sector_choice]
data = load_data(selected_tickers, start_date, end_date)

normalized_prices = data / data.iloc[0] * 100

st.subheader(f"{sector_choice} Sector Performance")
fig, ax = plt.subplots(figsize=(14, 8))
for ticker in selected_tickers:
    ax.plot(normalized_prices.index, normalized_prices[ticker], label=ticker)
ax.set_title(f"{sector_choice} Sector Prices (Normalized)")
ax.set_xlabel("Date")
ax.set_ylabel("Normalized Price")
ax.legend()
st.pyplot(fig)

if st.checkbox("Display Correlation Heatmap"):
    st.subheader(f"{sector_choice} Sector Correlation")
    correlation_matrix = normalized_prices.corr()
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

if st.checkbox("Analyze Volatility and Anomalies"):
    st.subheader(f"{sector_choice} Sector Volatility")
    returns = data.pct_change().dropna()
    volatility = returns.rolling(window=25).std() * np.sqrt(252)
    volatility = volatility.dropna()

    @st.cache_resource
    def get_isolation_forest():
        contamination_rate = 0.1  
        return IsolationForest(contamination=contamination_rate, random_state=42)
    
    isolation_forest = get_isolation_forest()
    volatility_values = volatility.values
    isolation_forest.fit(volatility_values)

    # Update anomaly detection logic
    volatility['Anomaly'] = isolation_forest.predict(volatility_values)

    # Filter only high-volatility anomalies based on a threshold
    volatility_threshold = 0.35 
    high_volatility_anomalies = volatility[
        (volatility['Anomaly'] == -1) & (volatility[selected_tickers] > volatility_threshold).any(axis=1)
    ]
    high_volatility_anomalies = high_volatility_anomalies.drop(columns='Anomaly')

    fig, ax = plt.subplots(figsize=(14, 7))
    for ticker in selected_tickers:
        ax.plot(volatility.index, volatility[ticker], label=ticker)
        if not high_volatility_anomalies.empty:
            anomaly_points = high_volatility_anomalies.index
            ax.scatter(anomaly_points, high_volatility_anomalies[ticker], color='red', label=f"{ticker} High Volatility Anomalies")
    ax.set_title(f"{sector_choice} Sector Volatility with High Volatility Anomalies")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility")
    ax.legend()
    st.pyplot(fig)

