import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from package.dataStatistics import *
from package.preProcessing import *
from package.dataIntergration import *
from package.machineLearning import *
from package.visualizing import *
from st_pages import Page, Section, show_pages, add_page_title, hide_pages


add_page_title()

# @st.cache_data
# def load_data():
#     # data1 = pd.read_excel('data/2008 Contoso Data.xlsx')
#     # data2 = pd.read_excel('data/2009 Contoso Data.xlsx')
#     data1 = pd.read_json("data/jsonl/2008_Contoso_Data.jsonl", lines=True)
#     data2 = pd.read_json("data/jsonl/2009_Contoso_Data.jsonl", lines=True)
#     data = pd.concat([data1, data2], ignore_index=True)

#     data3 = pd.read_excel('data/excel/Contoso_Lookup_Tables.xlsx', sheet_name=None)
#     # data = pd.concat([data1, data2], ignore_index=True)

#     product_data = pd.read_json("data/jsonl/DIM_product.jsonl", lines=True)
#     # product_data = pd.read_excel('data/Contoso Lookup Tables.xlsx', sheet_name='DIM Product')
#     # product_subcategory_data = pd.read_excel('data/Contoso Lookup Tables.xlsx', sheet_name='DIM Product Sub Category')
#     product_subcategory_data = pd.read_json("data/jsonl/DIM_product_subcategory_data.jsonl", lines=True)
#     # geography_data = pd.read_excel('data/Contoso Lookup Tables.xlsx', sheet_name='DIM Geography')
#     geography_data = pd.read_json("data/jsonl/DIM_geography_data.jsonl", lines=True)
#     # channel_data =  pd.read_excel('data/Contoso Lookup Tables.xlsx', sheet_name='DIM Channel')
#     channel_data =  pd.read_json("data/jsonl/DIM_channel_data.jsonl", lines=True)
#     return data1,data2, data3, data, product_data, product_subcategory_data, geography_data, channel_data

# @st.cache_data
# def load_model():
#     new_data = dataReduction(data)
#     x = new_data.drop('SalesAmount',axis = 1)
#     y = new_data['SalesAmount']
#     x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42) 
#     # model_rf = RandomForestRegressor().fit(x_train, y_train)
#     model_lr = LinearRegression().fit(x_train, y_train)
#     model_gr = GradientBoostingRegressor().fit(x_train, y_train)
#     return model_gr, model_lr, new_data
# # Load data and random_forest model only once
# data1, data2,data3, data, product_data, product_subcategory_data, geography_data, channel_data = load_data()
# model_gr, model_lr, new_data = load_model()

# model_rf = LinearRegression().fit(x_train, y_train)


# Hàm tạo liên kết đến các tab


# Tạo các tab trong sidebar
# tabs = ['Tab 1', 'Tab 2', 'Tab 3','Tab 4', 'Tab 5', 'Tab 6']
# selected_page = st.selectbox('Chọn trang:', ['Trang 1', 'Trang 2', 'Trang 3','Trang 4', 'Trang 5', 'Trang 6','Trang 7', 'Trang 8', 'Trang 9','Trang 10', 'Trang 11', 'Trang 12','Trang 13','Trang 14','Trang 15','Trang 16','Trang 17', 'Trang 18'])
# pages = [
#     'Trang 1', 'Trang 2', 'Trang 3', 'Trang 4', 'Trang 5', 
#     'Trang 6', 'Trang 7', 'Trang 8', 'Trang 9', 'Trang 10', 
#     'Trang 11', 'Trang 12', 'Trang 13', 'Trang 14', 'Trang 15', 
#     'Trang 16', 'Trang 17', 'Trang 18'
# ]
# selected_page = st.sidebar.selectbox('Chọn trang:', pages)

# Nội dung của tab được chọn
show_pages(
    [
        Page("main.py", "Data Analysis - Contoso", "💻"),
        Page("main1.py", "Describe Dataset", "💻"),
        Page("main2.py", "Data Statistics ", "💻"),
        Page("main3.py", "Data Preprocessing ", "💻"),
        Section( "Data Visualization ", "💻"),
        Page("main.py", "Profit Contoso in 2008 - 2009 ", "💻", in_section=True),
        Page("main.py", "Data Preprocessing ", "💻", in_section=True),
        Page("main.py", "Why Decrease Revenue ", "💻", in_section=True),
        Page("main.py", "Supplier's Profit ", "💻", in_section=True),
        Page("main.py", "Quantity Sale by Class ", "💻", in_section=True),
        Page("main.py", "Revenue by Class ", "💻", in_section=True),
        Page("main.py", "Quantity Sold by Brand ", "💻", in_section=True),
        Page("main.py", "Quantity Sales by Product Subcategory ", "💻", in_section=True),
        Page("main.py", "Number of Stores by Region ", "💻", in_section=True),
        Page("main.py", "Profit by Region ", "💻", in_section=True),
        Page("main.py", "Revenues by Channel ", "💻", in_section=True),
        Page("main.py", "Summary and Propose ", "💻", in_section=True),
        Section( "Data Modeling ", "💻"),
        Page("main.py", "Heatmap ", "💻", in_section=True),
        Page("main.py", "Data Collection ", "💻", in_section=True),
        Section( "Machine Learning ", "💻"),
        Page("main.py", "Calculate model points ", "💻", in_section=True),
        Page("main.py", "Test model against dataset ", "💻", in_section=True),
        Page("main.py", "Demo model ", "💻", in_section=True),

    ]
)
hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 Data Analyst by Việt Long & Sơn Lộc")

st.image("https://statics.cdn.200lab.io/2021/07/59-data-analysis-1.jpg")

st.info("Original Course Repository on [Github](https://github.com/DataTalksClub/data-engineering-zoomcamp)")

st.markdown("---")

with st.expander("Sign up here for 2024 Cohort"):
    st.markdown("""
    
    <a href="https://airtable.com/appzbS8Pkg9PL254a/shr6oVXeQvSI5HuWD"><img src="https://user-images.githubusercontent.com/875246/185755203-17945fd1-6b64-46f2-8377-1011dcb1a444.png" height="50" /></a>

    #

    - Register in [DataTalks.Club's Slack](https://datatalks.club/slack.html)
    - Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel
    - Join the [course Telegram channel with announcements](https://t.me/dezoomcamp)
    - The videos are published on [DataTalks.Club's YouTube channel](https://www.youtube.com/c/DataTalksClub) in [the course playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
    - [Frequently asked technical questions](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing)
        
    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Taking the course

##### 👨‍👦‍👦 2024 Cohort

* **Start**: 15 January 2024 (Monday) at 17:00 CET
* **Registration link**: https://airtable.com/shr6oVXeQvSI5HuWD
* [Cohort folder](cohorts/2024/) with homeworks and deadlines 


##### 👨‍🔧 Self-paced mode

All the materials of the course are freely available, so that you
can take the course at your own pace

* Follow the suggested syllabus (see below) week by week
* You don't need to fill in the registration form. Just start watching the videos and join Slack
* Check [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing) if you have problems
* If you can't find a solution to your problem in FAQ, ask for help in Slack

### 🔎 Overview""", unsafe_allow_html=True)


st.image("https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/architecture/photo1700757552.jpeg")

# if selected_page  == 'Trang 1':

#     st.markdown('<h1 ">Mục Lục</h1>', unsafe_allow_html=True)
#     st.header('1. MÔ TẢ VỀ BỘ DỮ LIỆU',anchor = 'Trang 2', )
#     st.header('2.THỐNG KÊ DỮ LIỆU',)
#     st.header('3. TIỀN XỬ LÝ DỮ LIỆU',)
#     st.header('4. TRỰC QUAN HÓA DỮ LIỆU',)
#     st.header('5. MÔ HÌNH HÓA DỮ LIỆU',)
#     st.header('6. KẾT LUẬN',)


# elif selected_page  == 'Trang 2':
#     st.header('MÔ TẢ VỀ BỘ DỮ LIỆU',divider = 'rainbow')
#     col1, col2 = st.columns(2)
#     col1.header('1. Company Background',)
#     col1.markdown("""
# <ul>
#   <li>Contoso là một công ty bán lẻ đa quốc gia</li>
#   <li>Thời gian: 2008 - 2009</li>
#   <li>Thị trường: North America, Australia, Asia, Europe</li>
#   <li>Kênh phân phối: Online, Store, Catalog, Reseller</li>
#   <li>Sản phẩm: Thiết bị điện tử và dịch vụ media</li>
# </ul>
#  """, unsafe_allow_html=True)
#     col2.image('./Photo/2.jfif', caption='Công ty Contoso', width=350)

#     st.header('2. Mô hình Star Schema')
#     st.write('- Data Star Schema là một mô hình tổ chức dữ liệu, nơi có một bảng trung tâm (fact table) đại diện cho sự kiện hoặc thông tin cơ bản, được bao quanh bởi các bảng chiều (dimension tables) mô tả chi tiết.\n\n- Điểm mạnh của mô hình này nằm ở khả năng tối ưu hiệu suất truy vấn và phân tích dữ liệu.\n\n- Các bảng chiều được tổ chức linh hoạt và dễ hiểu, giúp giảm thời gian xử lý, tăng cường khả năng hiển thị thông tin, và hỗ trợ mở rộng dữ liệu một cách thuận tiện.')   
#     st.image('./Photo/1.png', caption='Mô hình Star Schema')
#     st.write(data)
#     tabs = st.tabs([sheet_name for sheet_name in data3.keys()])
#     for index, sheet_name in enumerate(data3.keys()):
#         with tabs[index]: 
#             st.write(data3[sheet_name])
    
    
# elif selected_page  == 'Trang 3':
#     st.header('THỐNG KÊ DỮ LIỆU',)
#     st.header('DATA 2008')
#     dataStatistics2008(data1)
#     st.header('DATA 2009')
#     dataStatistics2009(data2)


    
    
    

# elif selected_page   == 'Trang 4':
#     handleMissingData2008(data1)    
#     handleDuplicateData2008(data1)
#     checkDataType2008(data1)
#     handleMissingData2009(data2)
#     handleDuplicateData2009(data2)
#     checkDataType2009(data2)

#     dI_preProcessing(data)
    
# elif selected_page == 'Trang 5':
    
#     st.subheader('LỢI NHUẬN NĂM 2008 - 2009')
#     revenueOverTime(data1, data2)

# elif selected_page == 'Trang 6':
#     st.header('BÀI TOÁN: TẠI SAO LỢI NHUẬN GIẢM')
#     col1, col2 = st.columns(2)
#     col1.image('./Photo/1496.jpg', caption='Tình hình kinh tế nước Mỹ các năm trước 2010')
#     col2.image('./Photo/4.jpg', caption='Tỷ lệ thất nghiệp ở Mỹ năm 2009')

# elif selected_page == 'Trang 7':
    
#     st.header('TRỰC QUAN HÓA DỮ LIỆU',)
#     st.subheader('1. DOANH THU CỦA NHÀ CUNG CẤP')
#     revenuebyManufacturer(data,product_data)
    
    
# elif selected_page == 'Trang 8':
#     quantitySalesByClass(data, product_data)
# elif selected_page == 'Trang 9':
#     st.subheader('4. SỐ LƯỢNG MẶT HÀNG THEO THƯƠNG HIỆU')
#     quantitySoldByBrand(data, product_data)
# elif selected_page == 'Trang 10':
#     st.subheader('5. SỐ LƯỢNG MẶT HÀNG THEO LOẠI SẢN PHẨM')
#     quantitySalesByProductSub(product_data, product_subcategory_data,data)
# elif selected_page == 'Trang 11':
#     st.subheader('5. SỐ LƯỢNG CỬA HÀNG THEO KHU VỰC')
#     storeCount(geography_data)
#     st.subheader('6. LỢI NHUẬN THEO KHU VỰC')
#     profitByQuarterForAll(data, geography_data)
# elif selected_page == 'Trang 12':
#     st.subheader('7. DOANH THU THEO KÊNH BÁN HÀNG')
#     revenueByChannelPieChart(data, channel_data)
#     revenueByYearForCatalog(data, channel_data)

# elif selected_page == 'Trang 13':
#     st.header('ĐỀ XUẤT',)
#     st.subheader('- Tập trung các sản phẩm tiện lợi, dễ sử dụng ')
#     st.subheader('- Mở rộng thị trường Châu Á ')
#     st.subheader('- Phát triển kênh bán hàng trực tuyến ')


# elif selected_page == 'Trang 14':
#     st.header('MÔ HÌNH HÓA DỮ LIỆU',)
#     heatMap(data)
    



# elif selected_page == 'Trang 15':
#     st.header('THU GIẢM DỮ LIỆU',)
#     data = dataReduction(data)
#     st.write(data)
# elif selected_page == 'Trang 16':
#     st.header('MÔ HÌNH HÓA DỮ LIỆU',)
#     data = dataReduction(data)
#     machineLearning(data)


# elif selected_page == 'Trang 17':
#     st.header('KIỂM TRA BỘ DỮ LIỆU',)
#     predictValue(data=new_data, model_gr = model_gr, model_lr = model_lr)

# elif selected_page == 'Trang 18':
#     st.header('DEMO',)
#     predictValue2(model_gr)










# Tính ma trận tương quan
#    
