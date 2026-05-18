import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Emad Smart Operations AI", layout="wide")

st.title("🏥 Emad Smart Operations AI")

# Store data
if "patients" not in st.session_state:
    st.session_state.patients = []

# Add patient
st.header("Add Patient")
name = st.text_input("Patient Name")
status = st.selectbox("Status", ["Arrived", "Waiting", "In Progress", "Done"])

if st.button("Add Patient"):
    st.session_state.patients.append({
        "name": name,
        "status": status,
        "time": datetime.now().strftime("%H:%M:%S")
    })

# Display data
st.header("Live Patients")
st.write(st.session_state.patients)

# Simple stats
st.header("Dashboard")
st.metric("Total Patients", len(st.session_state.patients))
