import streamlit as st
import os
from dotenv import load_dotenv
from main_ai_researcher import main_ai_researcher

# Load environment variables
load_dotenv()

def main():
    st.title("AI Researcher Demo")
    
    # Input fields
    question = st.text_area("Nhập câu hỏi của bạn:", height=100)
    reference = st.text_area("Nhập tài liệu tham khảo (nếu có):", height=100)
    mode = st.selectbox(
        "Chọn chế độ:",
        ["Detailed Idea Description", "Reference-Based Ideation"]
    )
    
    # Process button
    if st.button("Phân tích"):
        if question:
            with st.spinner('Đang xử lý...'):
                try:
                    result = main_ai_researcher(question, reference, mode)
                    st.success("Phân tích hoàn tất!")
                    st.write(result)
                except Exception as e:
                    st.error(f"Có lỗi xảy ra: {str(e)}")
        else:
            st.warning("Vui lòng nhập câu hỏi!")

if __name__ == "__main__":
    main()
