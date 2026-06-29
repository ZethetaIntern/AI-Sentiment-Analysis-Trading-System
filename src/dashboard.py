import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE SETTINGS ---------------- #

st.set_page_config(
    page_title="AI Trading Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("🚀 AI Trading Dashboard")
st.markdown("---")

# ---------------- LOAD DATA ---------------- #

try:
    df = pd.read_csv("data/master_report.csv")
except:
    st.error("master_report.csv not found.")
    st.stop()

# ---------------- BASIC INFORMATION ---------------- #

ticker = df["ticker"].iloc[0]

current_price = df["current_price"].iloc[0]
percent_change = df["percent_change"].iloc[0]

buy_count = (df["trading_signal"] == "BUY").sum()
sell_count = (df["trading_signal"] == "SELL").sum()
hold_count = (df["trading_signal"] == "HOLD").sum()

avg_confidence = round(df["confidence"].mean(), 2)

# ---------------- TOP METRICS ---------------- #

col1, col2, col3, col4 = st.columns(4)

col1.metric("Ticker", ticker)
col2.metric("Current Price", f"${current_price}")
col3.metric("Today's Change", f"{percent_change}%")
col4.metric("Average Confidence", avg_confidence)

st.markdown("---")

# ---------------- AI RECOMMENDATION ---------------- #

recommendation = "HOLD"
reason = "Signals are mixed."

if buy_count >= 7 and avg_confidence >= 0.80:
    recommendation = "🟢 STRONG BUY"
    reason = "Most news is positive with high confidence."

elif sell_count >= 7 and avg_confidence >= 0.80:
    recommendation = "🔴 STRONG SELL"
    reason = "Most news is negative with high confidence."

elif buy_count > sell_count:
    recommendation = "🟢 BUY"
    reason = "Positive sentiment dominates."

elif sell_count > buy_count:
    recommendation = "🔴 SELL"
    reason = "Negative sentiment dominates."

else:
    recommendation = "🟡 HOLD"
    reason = "Market sentiment is balanced."

st.subheader("Overall AI Recommendation")

st.success(recommendation)

st.write("Reason:", reason)

st.write("BUY Signals:", buy_count)
st.write("SELL Signals:", sell_count)
st.write("HOLD Signals:", hold_count)

st.markdown("---")

# ---------------- CHARTS ---------------- #

left, right = st.columns(2)

with left:

    st.subheader("Trading Signals")

    fig = px.bar(
        df["trading_signal"].value_counts(),
        labels={"value": "Count", "index": "Signal"},
        title="Trading Signals"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Sentiment Distribution")

    fig2 = px.pie(
        names=df["sentiment"].value_counts().index,
        values=df["sentiment"].value_counts().values,
        title="Sentiment Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ---------------- CONFIDENCE ---------------- #

st.subheader("FinBERT Confidence Scores")

fig3 = px.line(
    df,
    y="confidence",
    markers=True,
    title="Confidence Score"
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# ---------------- NEWS ---------------- #

st.subheader("Latest News")

for _, row in df.iterrows():

    with st.expander(row["headline"]):

        st.write("Ticker:", row["ticker"])
        st.write("Headline:", row["headline"])
        st.write("Sentiment:", row["sentiment"])
        st.write("Confidence:", row["confidence"])
        st.write("Trading Signal:", row["trading_signal"])
        st.write("Current Price:", row["current_price"])
        st.write("Percent Change:", row["percent_change"])

st.markdown("---")

# ---------------- TABLE ---------------- #

st.subheader("Complete Trading Report")

st.dataframe(df)