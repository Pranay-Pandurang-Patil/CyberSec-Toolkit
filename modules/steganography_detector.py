import streamlit as st
from PIL import Image
import numpy as np

def run():
    st.header("🖼️ Steganography Detector")

    st.info("ℹ️ Upload a PNG image only. JPEGs are not supported because compression destroys hidden bits.")

    uploaded_file = st.file_uploader("Upload an image to scan", type=["png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", width=400)

        data = np.array(image, dtype=np.uint8)
        lsb_bits = data & 1
        flat_bits = lsb_bits.flatten()

        chars = []
        for i in range(0, len(flat_bits), 8):
            byte = flat_bits[i:i+8]
            if len(byte) < 8:
                break
            value = int("".join(str(bit) for bit in byte), 2)
            if 32 <= value <= 126:  # printable ASCII
                chars.append(chr(value))

        hidden_text = "".join(chars)

        # Stop at END marker if present
        if "END" in hidden_text:
            hidden_text = hidden_text.split("END")[0] + "END"

        printable = "".join([c for c in hidden_text if 32 <= ord(c) <= 126])

        if printable.strip():
            st.success("✅ Hidden text detected!")
            st.text_area("Extracted Message:", printable.strip(), height=150)
            st.info("Message ends at 'END' marker. If you don’t see it, the image may not contain valid hidden text.")
        else:
            st.warning("⚠️ No hidden text found. Ensure you uploaded a PNG image with embedded text.")
