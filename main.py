import streamlit as st

st.set_page_config(page_title="대치수프리마 입시&코칭센터", layout="wide")

st.markdown("""
    <style>
    .main-header { text-align: center; padding: 40px; background-color: #001f5b; color: white; border-radius: 0 0 40px 40px; }
    .card { background: #001f5b; color: white; padding: 35px; border-radius: 30px; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.2); }
    .diag-up { transform: translateY(-20px); border-bottom: 8px solid #f7b200; }
    .diag-down { transform: translateY(20px); border-bottom: 8px solid #f7b200; }
    .stButton>button { width: 100%; border-radius: 50px; background-color: #f7b200; color: white; font-weight: bold; height: 3.5em; border: none; }
    </style>
    <div class="main-header">
        <h1>대치수프리마</h1>
        <p>대치수프리마 입시&코칭센터</p>
    </div>
""", unsafe_allow_html=True)

st.write("#")
st.info("### ✨ 브랜드 가치: 전략수리 입시 설계\n단순한 분석을 넘어 아이의 잠재력을 결과로 증명하는 대치수프리마만의 솔루션입니다.")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card diag-up"><h2>나의 입시위치 진단</h2><p>PDF 기반 정밀 분석</p></div>', unsafe_allow_html=True)
    if st.button("📊 진단 서비스 시작"):
        st.switch_page("pages/01_입시위치_진단.py")
with col2:
    st.markdown('<div class="card diag-down"><h2>AI 탐구/세특 생성기</h2><p>차별화된 학생부 문구 생성</p></div>', unsafe_allow_html=True)
    if st.button("🤖 AI 생성 서비스 시작"):
        st.switch_page("pages/02_AI_세특_생성기.py")
