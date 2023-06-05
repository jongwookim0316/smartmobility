import streamlit as st
from PIL import Image
    # 체질량 지수 구하기


def bmi_range(bmi):
    if bmi < 20:
        st.warning("저체중입니다")
    elif (bmi >= 20) and (bmi <= 23):
        st.success("정상체중입니다")
    elif (bmi > 23) and (bmi<=25):
        st.warning("과체중입니다")
    else:
        st.error("비만입니다")

st.write('# 체질량 지수 계산기')

st.write('체질량 지수란 \n인간의 비만도를 나타내는 지수로, 체중과 키의 관계로 계산된다.')

height = st.number_input('키 입력: (cm)',100,200,170,1)     
st.write('키: ',height,'cm')

weight = st.number_input('몸무게 입력: (kg)',0,200,70,1)     
st.write('몸무게: ',weight,'kg')

bmi = weight/((height/100)**2)

if st.button('결과'):
    st.write('bmi: ', round(bmi,2))
    bmi_range(bmi)

image = Image.open('s.jpg.jpg')
st.image(image)
  
