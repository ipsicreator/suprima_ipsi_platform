import streamlit as st

# 1. 페이지 설정 및 시안 기반 스타일 커스터마이징
st.set_page_config(page_title="대치수프리마 입시&코칭센터", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* 전체 배경색: 시안과 동일한 부드러운 화이트/미색 */
    .stApp { background-color: #F8F9FA; }
    
    /* 상단 네이비 헤더 */
    .header-bar {
        background-color: #001f5b; color: white; padding: 20px 50px;
        display: flex; justify-content: space-between; align-items: center;
        border-radius: 0 0 20px 20px;
    }
    
    /* 메인 카드 스타일 (입체감 적용) */
    .service-card {
        background: linear-gradient(145deg, #001f5b, #003399);
        color: white; padding: 30px; border-radius: 20px;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.1);
        position: relative; overflow: hidden; height: 180px;
    }
    .service-card::after {
        content: ''; position: absolute; right: -20px; bottom: -20px;
        width: 100px; height: 100px; background: rgba(255,255,255,0.1); border-radius: 50%;
    }
    
    /* 화이트 섹션 박스 (상담신청, 브랜드소개 등) */
    .white-box {
        background: white; padding: 30px; border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px;
    }
    
    /* 버튼 스타일 (골드 그라데이션) */
    .stButton>button {
        background: linear-gradient(to right, #D4AF37, #F7B200);
        color: white; border: none; border-radius: 30px;
        padding: 10px 25px; font-weight: bold; width: 100%;
    }
    </style>
    
    <div class="header-bar">
        <div><h2 style='margin:0;'>대치수프리마</h2><small>입시&코칭센터</small></div>
        <div style='display:flex; gap:20px; font-weight:bold;'>홈  |  서비스  |  소개  |  공지사항</div>
    </div>
""", unsafe_allow_html=True)

st.write("#")

# --- 메인 레이아웃 구성 (시안 배치 반영) ---
col_left, col_right = st.columns([1, 1])

with col_left:
    # 1. 나의 입시위치 진단 (기능 연결)
    st.markdown('<div class="service-card"><h2>나의 입시위치 진단 📊</h2><p>데이터 기반 정밀 분석</p></div>', unsafe_allow_html=True)
    if st.button("진단 시작하기 ➔", key="btn_diag"):
        st.switch_page("pages/01_입시위치_진단.py")
    
    st.write("#")
    
    # 2. AI 탐구/세특 생성기 (기능 연결)
    st.markdown('<div class="service-card" style="background: linear-gradient(145deg, #222, #444);"><h2>AI 탐구/세특 생성기 ✍️</h2><p>맞춤형 학생부 문구 생성</p></div>', unsafe_allow_html=True)
    if st.button("생성 시작하기 ➔", key="btn_gen"):
        st.switch_page("pages/02_AI_세특_생성기.py")

with col_right:
    # 3. 대치수프리마의 가치 (브랜드 소개)
    st.markdown("""
    <div class="white-box" style="background-color:#001f5b; color:white;">
        <h3>대치수프리마의 가치</h3>
        <p>단순한 분석을 넘어, 아이의 잠재력을 결과로 증명합니다.</p>
        <button style="background:#F7B200; border:none; border-radius:10px; padding:5px 15px;">가치 알아보기</button>
    </div>
    """, unsafe_allow_html=True)
    
    # 4. 입시 컨설팅/상담 신청 (실제 폼 기능)
    with st.container():
        st.markdown('<div class="white-box"><h4>입시 컨설팅/상담 신청</h4>', unsafe_allow_html=True)
        with st.form("consult_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            name = c1.text_input("학생 이름")
            grade = c2.selectbox("학년", ["중3", "고1", "고2", "고3", "N수"])
            phone = st.text_input("연락처")
            subject = st.multiselect("희망 분야", ["종합전형", "교과전형", "논술/정시", "세특/생성"])
            request = st.text_area("자세한 요청 사항")
            
            if st.form_submit_button("상담 신청하기"):
                st.balloons()
                st.success(f"{name} 학생의 상담 신청이 완료되었습니다. 곧 연락드리겠습니다.")
        st.markdown('</div>', unsafe_allow_html=True)

# 5. 하단 브랜드 상세 소개 (아이콘 영역 대체)
st.write("---")
b1, b2, b3 = st.columns(3)
b1.markdown('<div class="white-box" style="text-align:center;">🔍 <b>정밀 분석</b><br>객관적 위치 진단</div>', unsafe_allow_html=True)
b2.markdown('<div class="white-box" style="text-align:center;">🎯 <b>맞춤 코칭</b><br>특화 세특 설계</div>', unsafe_allow_html=True)
b3.markdown('<div class="white-box" style="text-align:center;">📈 <b>결과 선도</b><br>최적화 솔루션</div>', unsafe_allow_html=True)

# 6. 푸터
st.markdown("""
    <div style="background:#222; color:#888; padding:30px; text-align:center; border-radius:20px 20px 0 0;">
        대치수프리마 입시&코칭센터 | 전략수리 입시연구소 | T. (071) 123-4444<br>
        <small>© 2026 Daechi Suprema. All Rights Reserved.</small>
    </div>
""", unsafe_allow_html=True)