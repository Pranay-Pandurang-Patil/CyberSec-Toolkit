import streamlit as st
from modules import port_scanner, file_integrity

st.set_page_config(page_title="CyberSec Toolkit", layout="centered")

st.title("🛡️ CyberSec Toolkit")
st.write("Beginner-friendly cybersecurity fundamentals — all offline and safe.")

# Sidebar menu
menu = st.sidebar.radio("Select a module:", [
    "Port Scanner",
    "File Integrity Checker"
])

# Show only the selected module
if menu == "Port Scanner":
    port_scanner.run()
elif menu == "File Integrity Checker":
    file_integrity.run()
