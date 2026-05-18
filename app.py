import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Emad Smart AI", layout="wide")

st.title("🏥 Emad Smart Operations AI")

# ===== Upload Data =====
st.header("📂 Upload Data")
file = st.file_uploader("Upload Excel or CSV")

if file:
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.success("✅ File uploaded successfully")
    st.dataframe(df)

    # ===== Dashboard =====
    st.header("📊 Dashboard")

    col1, col2 = st.columns(2)

    col1.metric("Total Records", len(df))

    if "Status" in df.columns:
        waiting = len(df[df["Status"] == "Waiting"])
        col2.metric("Waiting", waiting)

    st.bar_chart(df.select_dtypes(include='number'))

# ===== Manual Entry (optional) =====
st.header("➕ Quick Add Patient")
name = st.text_input("Patient Name")
status = st.selectbox("Status", ["Arrived", "Waiting", "In Progress", "Done"])

if st.button("Add"):
    st.write(f"✅ Added: {name} - {status}")

# ===== Image Upload =====
st.header("📷 Upload Images")

image = st.file_uploader("Upload image", type=["png","jpg","jpeg"])
if image:
    st.image(image)

# ===== Simple AI Chat =====
st.header("🤖 AI Assistant")

user_input = st.text_input("Ask something about your data")

if user_input:
    st.write("💡 AI Response:")
    st.write(f"You asked: {user_input}")
    st.write("➡️ (Next version will include real AI analysis)")
