import streamlit as st
import pandas as pd
import plotly.express as px
st.title("📊 나의 입시위치 진단")
st.info("데이터 기반의 객관적 위치를 진단합니다.")
grade = st.slider("평균 등급", 1.0, 9.0, 2.5)
df = pd.DataFrame({"구분": ["나", "목표치"], "등급": [grade, 2.1]})
st.plotly_chart(px.bar(df, x="구분", y="등급", color="구분", range_y=[9,1]))
