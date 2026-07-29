import streamlit as st   # Streamlit library for GUI
import socket            # Python's built-in networking library

def run():
    st.header("🔍 Port Scanner")   # Adds a title in the UI
    target = st.text_input("Enter target (default: localhost):", "127.0.0.1")
    # Text box for user to enter IP, default is localhost

    start_port = st.number_input("Start Port", 1, 65535, 20)
    end_port = st.number_input("End Port", 1, 65535, 1024)
    # Number inputs for port range

    if st.button("Scan"):   # Button triggers the scan
        open_ports = []
        st.write("Scanning ports...")
        for port in range(start_port, end_port + 1):   # Loop through ports
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket
            s.settimeout(0.1)   # Timeout for responsiveness
            result = s.connect_ex((target, port))   # Try connecting
            if result == 0:     # If connection succeeds
                open_ports.append(port)
            s.close()
        st.success(f"Open ports: {open_ports if open_ports else 'None found'}")
