import streamlit as st
from st_pages import add_page_title
from package.visualizing import *
add_page_title()
data = st.session_state['data']
product_data = st.session_state['product_data']
st.subheader('1. DOANH THU CỦA NHÀ CUNG CẤP')
revenuebyManufacturer(data,product_data)