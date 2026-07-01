import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Sentiment Trading Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Sentiment Analysis Trading Dashboard")
st.write("News-driven trading system using NLP, FinBERT sentiment analysis, event classification, market reaction prediction, and automated signal generation.")

st.markdown("---")

try:
    df = pd.read_csv("data/master_report.csv")
except FileNotFoundError:
    st.error("data/master_report.csv not found. Please run: python3 src/main.py first.")
    st.stop()

ticker = df["ticker"].iloc[0]
current_price = df["current_price"].iloc[0]
previous_close = df["previous_close"].iloc[0]
percent_change = df["percent_change"].iloc[0]

buy_count = (df["trading_signal"] == "BUY").sum()
sell_count = (df["trading_signal"] == "SELL").sum()
hold_count = (df["trading_signal"] == "HOLD").sum()

positive_count = (df["sentiment"] == "POSITIVE").sum()
negative_count = (df["sentiment"] == "NEGATIVE").sum()
neutral_count = (df["sentiment"] == "NEUTRAL").sum()

avg_confidence = round(df["confidence"].mean(), 2)

st.subheader("Market Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Ticker", ticker)
col2.metric("Current Price", f"${current_price}")
col3.metric("Previous Close", f"${previous_close}")
col4.metric("Today's Change", f"{percent_change}%")

col5, col6, col7, col8 = st.columns(4)

col5.metric("Articles Analysed", len(df))
col6.metric("Average Confidence", avg_confidence)
col7.metric("BUY Signals", buy_count)
col8.metric("SELL Signals", sell_count)

st.markdown("---")

st.subheader("Overall AI Recommendation")

if buy_count > sell_count and buy_count >= hold_count:
    recommendation = "🟢 BUY"
    reason = "Bullish or positive market signals are stronger than negative signals."
elif sell_count > buy_count and sell_count >= hold_count:
    recommendation = "🔴 SELL"
    reason = "Bearish or negative market signals are stronger than positive signals."
else:
    recommendation = "🟡 HOLD"
    reason = "Signals are mixed or not strong enough for a clear trade."

st.success(recommendation)
st.write("Reason:", reason)

st.markdown("---")

left, right = st.columns(2)

with left:
    st.subheader("Sentiment Distribution")
    fig_sentiment = px.pie(
        names=df["sentiment"].value_counts().index,
        values=df["sentiment"].value_counts().values,
        title="Sentiment Distribution"
    )
    st.plotly_chart(fig_sentiment, use_container_width=True)

with right:
    st.subheader("Trading Signal Distribution")
    fig_signal = px.bar(
        df["trading_signal"].value_counts(),
        labels={"value": "Count", "index": "Trading Signal"},
        title="Trading Signal Distribution"
    )
    st.plotly_chart(fig_signal, use_container_width=True)

st.markdown("---")

left2, right2 = st.columns(2)

with left2:
    st.subheader("News Event Classification")
    fig_event = px.bar(
        df["event_type"].value_counts(),
        labels={"value": "Count", "index": "Event Type"},
        title="Event Type Distribution"
    )
    st.plotly_chart(fig_event, use_container_width=True)

with right2:
    st.subheader("Market Reaction Prediction")
    fig_reaction = px.pie(
        names=df["market_reaction"].value_counts().index,
        values=df["market_reaction"].value_counts().values,
        title="Predicted Market Reaction"
    )
    st.plotly_chart(fig_reaction, use_container_width=True)

st.markdown("---")

st.subheader("Confidence Score by News Article")

fig_confidence = px.line(
    df,
    y="confidence",
    markers=True,
    title="FinBERT Confidence Scores"
)

st.plotly_chart(fig_confidence, use_container_width=True)

st.markdown("---")

st.subheader("Latest News Intelligence")

for _, row in df.iterrows():
    with st.expander(row["headline"]):
        st.write("Ticker:", row["ticker"])
        st.write("Companies:", row["companies"])
        st.write("People:", row["people"])
        st.write("Event Type:", row["event_type"])
        st.write("Sentiment:", row["sentiment"])
        st.write("Confidence:", row["confidence"])
        st.write("Market Reaction:", row["market_reaction"])
        st.write("Reaction Confidence:", row["reaction_confidence"])
        st.write("Expected Price Move:", row["expected_price_move"])
        st.write("Trading Signal:", row["trading_signal"])
        st.write("Current Price:", row["current_price"])
        st.write("Percent Change:", row["percent_change"])

st.markdown("---")

st.subheader("Complete Enhanced Trading Report")

st.dataframe(df, use_container_width=True)