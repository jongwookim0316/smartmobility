import streamlit as st
from PIL import Image
import pandas as pd 
import matplotlib.pyplot as plt

    # 화면 분할

add_selectbox = st.sidebar.selectbox(
    "목차",
    ("bmi", "gapminder", "my page")
)

if add_selectbox == 'bmi':


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
  
elif add_selectbox == 'gapminder':


        # gapminder


    st.write('# gapminder')

    data = pd.read_csv('gapminder.csv')
    st.write(data)

    colors = []
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x == 'Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('olive') 
        elif x == 'Americas':
            colors.append('green')
        else:
            colors.append('orange')

    data['colors']=colors

    year = st.slider('년도 선택', 1952, 2007, 1952, 5)
    st.write("year", year)

    data = data[data['year']==year]

    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.000001, color=data['colors'])
    ax.set_title('how does gdp per capital relate to life expectancy')
    ax.set_xlabel('gdp per capital')
    ax.set_ylabel('life expectancy')
    st.pyplot(fig)



else:
    st.write('# my page')

