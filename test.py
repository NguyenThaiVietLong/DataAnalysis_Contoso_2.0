import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

selected_page = st.selectbox('Chọn trang:', ['Trang 1', 'Trang 2', 'Trang 3','Trang 4', 'Trang 5', 'Trang 6','Trang 7', 'Trang 8', 'Trang 9','Trang 10', 'Trang 11', 'Trang 12','Trang 13','Trang 14','Trang 15','Trang 16','Trang 17', 'Trang 18'])

if selected_page  == 'Trang 1':
    st.title("Chào Mừng Đến Với Ứng Dụng Của Tôi")  # Thêm tiêu đề cho trang bìa
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Ftopdev.vn%2Fblog%2Fdata-analyst-can-hoc-gi%2F&psig=AOvVaw3p-vbuWSrHiWWo7nD9AHiD&ust=1708854147283000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMCjjfXXw4QDFQAAAAAdAAAAABAE", use_column_width=True)  # Thêm ảnh bìa, thay thế URL bằng đường dẫn thực tế của bạn
    st.header("Ứng Dụng Streamlit Độc Đáo")  # Thêm phụ đề hoặc thông tin bổ sung
    st.write("""
    Đây là ứng dụng Streamlit được thiết kế để giới thiệu các dự án, ý tưởng, và thông tin liên hệ của tôi. 
    Bạn có thể sử dụng menu ở trên để điều hướng giữa các trang khác nhau và khám phá thêm về công việc của tôi.
    """)
    st.subheader("Liên Hệ")
    st.write("""
    - Email: emailcuaban@example.com
    - LinkedIn: [LinkedIn của bạn](https://www.linkedin.com/in/yourprofile)
    - GitHub: [GitHub của bạn](https://github.com/yourprofile)
    """)
