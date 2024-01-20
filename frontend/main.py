import streamlit as st
import requests

st.title('Hello!')
API_URL="https://gcp-test.onrender.com"
res=requests.get(API_URL+"/"+"hello")
records=res.json()
st.subheader(records[message])
res=requests.get(API_URL+"/"+"world")
records=res.json()
st.subheader(records[message])