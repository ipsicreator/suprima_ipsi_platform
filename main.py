import streamlit as st
st.set_page_config(page_title="대치수프리마 입시&코칭센터", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp { background-color: #F9F9F7; }
    .nav-bar { background-color: #001f5b; color: white; padding: 15px 60px; display: flex; justify-content: space-between; align-items: center; border-radius: 0 0 15px 15px; }
    .diag-card { background: linear-gradient(135deg, #001f5b 0%, #003366 100%); color: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); height: 150px; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37 0%, #F7B200 100%); color: white !important; border-radius: 30px !important; font-weight: bold; height: 3.5em; width: 100%; border: none; }
    </style>
    <div class="nav-bar">
        <div><h2 style='margin:0;'>대치수프리마</h2><small>입시&코칭센터</small></div>
        <div style='display:flex; gap:30px; font-weight:bold;'>홈 | 서비스 | 소개 | 공지사항</div>
    </div>
""", unsafe_allow_html=True)
st.write("#")
col1, col2 = st.columns([1, 1.1])
with col1:
    st.markdown('<div class="diag-card"><h2>나의 입시위치 진단</h2><p>실시간 분석 엔진 가동</p></div>', unsafe_allow_html=True)
    if st.button("진단 서비스 시작하기"): st.switch_page("pages/01_입시위치_진단.py")
    st.write("#")
    st.markdown('<div class="diag-card" style="background: linear-gradient(135deg, #222, #444);"><h2>AI 탐구/세특 생성기</h2><p>전문가용 AI 로직 탑재</p></div>', unsafe_allow_html=True)
    if st.button("AI 생성 서비스 시작하기"): st.switch_page("pages/02_AI_세특_생성기.py")
with col2:
    with st.form("consult"):
        st.subheader("📝 입시 컨설팅 신청")
        name = st.text_input("학생 성함")
        phone = st.text_input("연락처")
        if st.form_submit_button("상담 신청하기"): st.success(f"{name}님, 접수 완료!")
