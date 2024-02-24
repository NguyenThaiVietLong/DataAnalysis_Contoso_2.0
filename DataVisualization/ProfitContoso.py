import streamlit as st
from st_pages import add_page_title, hide_pages
from package.visualizing import *
add_page_title()

data1 = st.session_state['data1']
data2 = st.session_state['data2']
st.subheader('LỢI NHUẬN NĂM 2008 - 2009')
revenueOverTime(data1 ,data2)