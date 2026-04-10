import streamlit as st
st.title("🤖 AI 탐구/세특 생성기")
kw = st.text_input("탐구 키워드 입력")
if st.button("AI 생성"):
    st.success(f"생성 결과: {kw}에 대한 심화 탐구 역량이 돋보이며...")
