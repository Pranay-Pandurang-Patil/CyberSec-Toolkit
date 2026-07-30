import streamlit as st
import re
import math

def run():
    st.header("🔑 Password Analyzer")
    password = st.text_input("Enter a password to analyze:", type="password")

    if password:
        score = 0
        feedback = []

        # Length check
        if len(password) >= 8:
            score += 2
        else:
            feedback.append("Password too short (min 8 chars).")

        # Uppercase
        if re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback.append("Add uppercase letters.")

        # Lowercase
        if re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("Add lowercase letters.")

        # Digits
        if re.search(r"[0-9]", password):
            score += 1
        else:
            feedback.append("Add numbers.")

        # Symbols
        if re.search(r"[^A-Za-z0-9]", password):
            score += 1
        else:
            feedback.append("Add special characters.")

        # Entropy calculation (rough estimate)
        charset = 0
        if re.search(r"[a-z]", password): charset += 26
        if re.search(r"[A-Z]", password): charset += 26
        if re.search(r"[0-9]", password): charset += 10
        if re.search(r"[^A-Za-z0-9]", password): charset += 32
        entropy = len(password) * math.log2(charset) if charset else 0

        st.write(f"Password strength score: {score}/6")
        st.write(f"Estimated entropy: {entropy:.2f} bits")

        if feedback:
            st.warning("Suggestions:\n" + "\n".join(feedback))
        else:
            st.success("Strong password!")
