import streamlit as st

def show():
    st.title("HÌNH TRỤ")
    
    st.header("Định nghĩa")
    st.write("Hãy cùng tìm hiểu định nghĩa hình trụ qua hoạt động dưới đây.")
    
    geogebra_url = "https://www.geogebra.org/m/qkp4se2d"
    if st.button("Tìm hiểu định nghĩa Hình trụ trên Geogebra"):
        st.write("Mở liên kết [Geogebra - Hình trụ](%s)" % geogebra_url)
        st.write("Hoặc bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình trụ</button></a>', unsafe_allow_html=True)
    
    st.header("Công thức")
    st.write("Hãy cùng tìm hiểu công thức tính diện tích xung quanh và thể tích của hình trụ qua hoạt động dưới đây.")

    geogebra_url = "https://www.geogebra.org/m/qkp4se2d"
    if st.button("Tìm hiểu các công thức của Hình trụ trên Geogebra"):
        st.write("Mở liên kết [Geogebra - Hình trụ](%s)" % geogebra_url)
        st.write("Hoặc bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình trụ</button></a>', unsafe_allow_html=True)

    st.header("Một số bài tập tự luyện")