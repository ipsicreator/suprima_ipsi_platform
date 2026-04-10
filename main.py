import streamlit as st

st.set_page_config(page_title="대치수프리마", layout="wide", initial_sidebar_state="collapsed")

# 디자인 테두리 및 카드 스타일
st.markdown("""
<style>
    .stApp { background-color: #F8F9F5; }
    .nav-bar { background-color: #001f5b; color: white; padding: 20px; border-radius: 0 0 20px 20px; text-align: center; }
    .service-card {
        background: linear-gradient(145deg, #001f5b, #003366);
        color: white; padding: 30px; border-radius: 20px;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.1); margin-bottom: 20px;
    }
    .consult-box {
        background: white; padding: 30px; border-radius: 20px;
        border: 1px solid #eee; box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37, #F7B200) !important;
        color: white !important; border-radius: 30px !important;
        font-weight: bold; height: 3.5em; width: 100%; border: none;
    }
</style>
<div class="nav-bar">
    <h2 style='margin:0;'>대치수프리마 입시&코칭센터</h2>
</div>
<br>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown('<div class="service-card"><h3>나의 입시위치 진단</h3><p>정밀 데이터 분석 엔진</p></div>', unsafe_allow_html=True)
    if st.button("진단 서비스 시작하기 ➔", key="d"):
        st.switch_page("pages/01_입시위치_진단.py")

    st.markdown('<div class="service-card" style="background:#333;"><h3>AI 탐구/세특 생성기</h3><p>전문가용 문구 생성</p></div>', unsafe_allow_html=True)
    if st.button("AI 생성 시작하기 ➔", key="a"):
        st.switch_page("pages/02_AI_세특_생성기.py")

with col2:
    st.markdown('<div class="consult-box">', unsafe_allow_html=True)
    with st.form("consult_form_final"):
        st.subheader("📝 상담 신청")
        st.text_input("성함/학년")
        st.text_input("연락처")
        st.textarea("메모", height=100)
        if st.form_submit_button("신청 완료"):
            st.success("접수되었습니다!")
    st.markdown('</div>', unsafe_allow_html=True)
