import streamlit as st

st.set_page_config(page_title="대치수프리마 입시&코칭센터", layout="wide", initial_sidebar_state="collapsed")

# 모바일/태블릿 최적화 전용 CSS
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 */
    .stApp { background-color: #F8F9FA; }
    
    /* 모바일 대응 반응형 컨테이너 */
    @media (max-width: 768px) {
        .nav-bar { padding: 15px 20px !important; flex-direction: column; text-align: center; }
        .nav-menu { display: none; } /* 모바일에서 메뉴 숨김 */
        .service-card { padding: 25px !important; min-height: 120px !important; }
        .form-box { padding: 20px !important; }
    }

    /* 상단 헤더 */
    .nav-bar {
        background-color: #001f5b; color: white; padding: 20px 60px;
        display: flex; justify-content: space-between; align-items: center;
        border-radius: 0 0 20px 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    /* 입체 카드 디자인 */
    .service-card {
        background: linear-gradient(135deg, #001f5b 0%, #003366 100%);
        color: white; padding: 35px; border-radius: 20px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1); margin-bottom: 15px;
    }

    /* 상담 신청 박스 */
    .form-box {
        background: white; padding: 35px; border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #eee;
    }

    /* 골드 버튼 */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #F7B200 100%) !important;
        color: white !important; border: none !important; border-radius: 50px !important;
        font-weight: bold !important; height: 3.5em; width: 100%;
        box-shadow: 0 4px 12px rgba(247, 178, 0, 0.35);
    }
    </style>
    
    <div class="nav-bar">
        <div><h2 style='margin:0; font-size: 1.8rem;'>대치수프리마</h2><small>입시&코칭센터</small></div>
        <div class="nav-menu" style='display:flex; gap:20px; font-weight:bold;'>홈 | 서비스 | 소개</div>
    </div>
""", unsafe_allow_html=True)

st.write("#")

# 반응형 컬럼 배치 (태블릿 이상에서 좌우, 모바일에서 상하 자동 전환)
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.markdown('<div class="service-card"><h3>나의 입시위치 진단 📊</h3><p>데이터 기반 정밀 분석</p></div>', unsafe_allow_html=True)
    if st.button("진단 서비스 시작하기 ➔", key="diag"):
        st.switch_page("pages/01_입시위치_진단.py")
    
    st.markdown('<div class="service-card" style="background: linear-gradient(135deg, #222, #444);"><h3>AI 탐구/세특 생성기 🤖</h3><p>차별화된 학생부 문구 생성</p></div>', unsafe_allow_html=True)
    if st.button("AI 생성 서비스 시작하기 ➔", key="ai"):
        st.switch_page("pages/02_AI_세특_생성기.py")

with col2:
    st.markdown('<div class="form-box">', unsafe_allow_html=True)
    st.subheader("📝 상담 신청")
    with st.form("mobile_consult", clear_on_submit=True):
        st.text_input("학생 이름 / 학년")
        st.text_input("연락처")
        st.textarea("상담 요청 내용", height=100)
        if st.form_submit_button("신청 완료"):
            st.success("접수되었습니다.")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.markdown("<div style='text-align:center; color:#999; font-size:12px;'>대치수프리마 입시&코칭센터 | T. (071) 123-4444</div>", unsafe_allow_html=True)
