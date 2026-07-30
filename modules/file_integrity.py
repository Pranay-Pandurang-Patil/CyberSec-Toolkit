import streamlit as st
import hashlib

def run():
    st.header("🗂️ File Integrity Checker")
    file = st.file_uploader("Upload a file to check integrity")

    if file is not None:
        # Read file bytes
        data = file.read()
        # Generate SHA256 hash
        file_hash = hashlib.sha256(data).hexdigest()
        st.write(f"SHA256 Hash: {file_hash}")

        # User can paste a known hash to compare
        known_hash = st.text_input("Enter known hash to compare:")
        if known_hash:
            if known_hash == file_hash:
                st.success("✅ File integrity verified — hashes match.")
            else:
                st.error("❌ File integrity failed — hashes do not match.")
