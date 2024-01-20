import streamlit as st
import requests

st.title('Hello!')
res=requests.get(API_URL)
records=res.json()
st.subheader(records)