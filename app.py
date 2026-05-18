st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    h1, h2, h3 {
        color: #00c6ff;
    }
    .stButton button {
        background-color: #00c6ff;
        color: black;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Emad AI System", layout="wide")

# === SIDEBAR ===
page = st.sidebar.radio("Navigation", [
    "Home",
    "AI Assistant",
    "Data Center",
    "Dashboard",
    "Team Productivity",
    "To-Do List"
])

# ===== HOME =====
if page == "Home":
    st.title("🏥 Emad AI Personal System")

    st.image("https://via.placeholder.com/150", caption="Your Photo")

    st.write("Welcome to your AI assistant system for work automation and analysis.")

# ===== AI ASSISTANT =====
elif page == "AI Assistant":
    st.title("🤖 AI Assistant")

    user_input = st.text_area("Ask anything about your data")

    if user_input:
        st.write("💡 AI Response:")
        st.write(f"You asked: {user_input}")
        st.write("➡️ (Next step: real AI integration)")

# ===== DATA CENTER =====
elif page == "Data Center":
    st.title("📂 Data Center")

    file = st.file_uploader("Upload Excel or CSV")

    if file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.success("✅ Data uploaded")
        st.dataframe(df)

# ===== DASHBOARD =====
elif page == "Dashboard":
    st.title("📊 Dashboard")

    file = st.file_uploader("Upload data for analysis")

    if file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.metric("Rows", len(df))

        st.bar_chart(df.select_dtypes(include='number'))

# ===== TEAM PRODUCTIVITY =====
elif page == "Team Productivity":
    st.title("👨‍⚕️ Team Productivity")

    emp = st.text_input("Employee Name")
    task = st.text_input("Task Done")

    if st.button("Add Activity"):
        st.write(f"✅ Recorded: {emp} - {task}")

# ===== TO-DO LIST =====
elif page == "To-Do List":
    st.title("✅ To-Do List")

    task = st.text_input("Add Task")

    if st.button("Add"):
        st.write(f"📌 Task added: {task}")
