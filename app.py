import streamlit as st

# Giả sử có hàm inference trong repo, ví dụ:
# from ai_model import run_inference

st.title("AI Researcher Demo App")

user_input = st.text_input("Nhập câu hỏi hoặc dữ liệu vào đây:")

if st.button("Chạy AI"):
    # Kết quả giả lập, thay bằng gọi hàm thật từ repo
    # result = run_inference(user_input)
    result = f"Kết quả AI cho input: {user_input}"
    st.write(result)
