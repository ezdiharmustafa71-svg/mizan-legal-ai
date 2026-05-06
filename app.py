import streamlit as st

st.title("⚖️ Mizan Legal AI")

st.write("System is running...")

uploaded_file = st.file_uploader("Upload Contract", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    st.write("Contract loaded successfully")
    st.text_area("Contract Content", text, height=300)
