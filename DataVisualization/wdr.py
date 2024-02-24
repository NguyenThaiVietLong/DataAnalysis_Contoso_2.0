import streamlit as st
from st_pages import add_page_title
from package.visualizing import *
add_page_title()
# data1 = pd.read_json("data/jsonl/2008_Contoso_Data.jsonl", lines=True)
# data2 = pd.read_json("data/jsonl/2009_Contoso_Data.jsonl", lines=True)
st.header('BÀI TOÁN: TẠI SAO LỢI NHUẬN GIẢM')
col1, col2 = st.columns(2)
col1.image('./Photo/1496.jpg', caption='Tình hình kinh tế nước Mỹ các năm trước 2010',use_column_width='auto')
col2.image('./Photo/4.jpg', caption='Tỷ lệ thất nghiệp ở Mỹ năm 2009',use_column_width='auto')