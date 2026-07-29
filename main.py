import streamlit as st
from modules import port_scanner

# Page setup
st.set_page_config(page_title="CyberSec Toolkit", layout="centered")

# Title
st.title("🛡️ CyberSec Toolkit")
st.write("Beginner-friendly cybersecurity fundamentals — all offline and safe.")

# Sidebar menu
menu = st.sidebar.radio("Select a module:", [
    "Port Scanner"
])

# Module routing
if menu == "Port Scanner":
    port_scanner.run()
