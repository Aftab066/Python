import streamlit as st 

st.title("Hello World")
box = st.selectbox("Select Any:",["CS","Stat","Math"])

if box:
    st.success(box)
    
    
st.sidebar.title("Options")
col1,col2 = st.columns(2)

with col1:
    st.header("Home")
    
with col2:
    st.header
    ("Login")
    
st.container()
st.expander("See More")