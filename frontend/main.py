import streamlit as st
import requests

st.title('Hello!')
API_URL="https://gcp-test.onrender.com"
res=requests.get("https://gcp-test.onrender.com/hello")
records=res.json()
st.write(records)