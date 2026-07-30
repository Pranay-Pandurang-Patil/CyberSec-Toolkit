import streamlit as st
from modules import port_scanner, file_integrity, password_analyzer, steganography_detector

# Sidebar Title
st.sidebar.title("🛡️ CyberSec Toolkit")

# Sidebar Info Box
st.sidebar.info(
    "📘 Cyber Security Project (Medium Level)\n\n"
    "Developed for educational purposes only.\n\n"
    "Modules included:\n"
    "🔍 Port Scanner – Scan open ports on a target system.\n"
    "🗂️ File Integrity Checker – Verify file hashes to detect tampering.\n"
    "🔑 Password Analyzer – Check password strength and entropy.\n"
    "🖼️ Steganography Detector – Detect hidden text in PNG images.\n\n"
    "⚠️ Note: Steganography Detector works only with PNG images. "
    "Hidden messages must end with the marker 'END'."
)

# Sidebar Module Selection
module = st.sidebar.radio(
    "Select a module:",
    (
        "🔍 Port Scanner",
        "🗂️ File Integrity Checker",
        "🔑 Password Analyzer",
        "🖼️ Steganography Detector"
    )
)

# Module Routing
if module == "🔍 Port Scanner":
    port_scanner.run()
elif module == "🗂️ File Integrity Checker":
    file_integrity.run()
elif module == "🔑 Password Analyzer":
    password_analyzer.run()
elif module == "🖼️ Steganography Detector":
    steganography_detector.run()
