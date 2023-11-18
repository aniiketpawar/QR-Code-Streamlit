import io
import qrcode
import streamlit as st


st.title("Let's connect on LinkedIn.")
st.caption("QR code")


url = st.text_input(
    "URL to encode:", 
    "www.linkedin.com/in/aniiketpawar"
)


img = qrcode.make(url)
virtualfile = io.BytesIO()
img.save(virtualfile)


st.image(virtualfile)