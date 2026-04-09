import streamlit as st
import requests
import pandas as pd

st.title("Urban Livelihoods Delivery Dashboard 🇮🇳")

API_URL = "http://backend:8000"

# Fetch data
cities = requests.get(f"{API_URL}/cities").json()
metrics = requests.get(f"{API_URL}/metrics").json()

df = pd.DataFrame(cities)

# 🎯 Define Targets (VERY IMPORTANT)
JOB_TARGET = 150
DELAY_THRESHOLD = 10

# Metrics
st.header("Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Jobs Completed", metrics["total_jobs"])
col2.metric("Total Delays", metrics["total_delays"])

# Status logic based on KPI
def get_status(row):
    if row["jobs_completed"] >= JOB_TARGET and row["delays"] <= DELAY_THRESHOLD:
        return "🟢 On Track"
    elif row["delays"] > DELAY_THRESHOLD:
        return "🔴 At Risk"
    else:
        return "🟡 Needs Attention"

df["status"] = df.apply(get_status, axis=1)

# Charts
st.header("Performance Overview")
st.bar_chart(df.set_index("name")["jobs_completed"])
st.bar_chart(df.set_index("name")["delays"])

# 🚨 Alerts Section
st.header("🚨 Alerts & Risks")

alerts = df[df["status"] == "🔴 At Risk"]

if alerts.empty:
    st.success("No critical risks detected")
else:
    for _, row in alerts.iterrows():
        st.error(f"{row['name']} has high delays ({row['delays']})")

# Table
st.header("Detailed View")
st.dataframe(df)