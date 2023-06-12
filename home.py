import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import datetime



st.write('# :blue[GTTG]')               # 제목 출력(파란색)
st.write(':blue[Go To The Gym]')        # 부제목 출력(파란색)
        
        
        # 화면 분할

tab1, tab2, tab3 = st.tabs(["루틴", "헬스장", "My Record"])         # table 분할 

        
        # 루틴 페이지

with tab1:
    st.header("_루틴_")                         # 헤드라인
    image = Image.open('루틴.jpg')              # 사진첨부
    st.image(image)                             # 이미지 출력  

    option = st.selectbox(
        '운동루틴', 
        ('선택','5X5 운동일지_종우.ver', '531 운동일지_종우.ver', 'PHUL 운동일지_종우.ver'))       # selectbox 

    
    if option == '5X5 운동일지_종우.ver':   # option = '5X5 운동일지_종우.ver' => '5X5 운동일지_종우.ver'파일다운 

        st.write(':green[5X5 운동일지_종우.ver]')   # '5X5 운동일지_종우.ver' 텍스트 출력
        st.write('스트렝스 훈련 프로그램으로써 주 3회 정도로 하며')   #  간략한 설명 출력
        st.write('4대 운동인 오버헤드프레스, 벤치프레스, 스쿼트, 데드리프트를 중심으로 하는 운동이다.')       #  간략한 설명 출력
        st.write('main 종목은 5개씩 5set를 하는것이 특징이다.')     #  간략한 설명 출력


            #운동일지 다운버튼 생성 

        df = pd.read_csv('5x5 운동일지_종우.ver.csv')           # csv 파일 불러옴

        @st.cache_data
        def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label=":red[Download : 5x5 운동일지]",          # 버튼이름
            data=csv,                                       # 파일 csv 형태
            file_name='5x5 운동일지_종우.ver.csv',             # 파일이름
            mime='text/csv',
        )

       
    elif option == '531 운동일지_종우.ver':      # option = '531 운동일지_종우.ver' => '531 운동일지_종우.ver'파일다운 

        st.write(':green[531 운동일지_종우.ver]')   # '531 운동일지_종우.ver' 텍스트 출력
        st.write('스트렝스 훈련 프로그램으로써 주 4회 정도로 하며')   #  간략한 설명 출력
        st.write('4대 운동인 오버헤드프레스, 벤치프레스, 스쿼트, 데드리프트를 중심으로 하는 운동이다.')       #  간략한 설명 출력
        st.write('main 종목 + 보조운동으로 이루어지며 main운동은 5회 -> 3회 -> 1회 순으로 돌아간다.')     #  간략한 설명 출력

        df = pd.read_csv('531 운동일지_종우.ver.csv')           # csv 파일 불러옴

             #운동일지 다운버튼 생성 

        @st.cache_data
        def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label=":red[Download : 531 운동일지]",          # 버튼이름
            data=csv,                                       # 파일 csv 형태
            file_name='531 운동일지_종우.ver.csv',             # 파일이름 
            mime='text/csv',
        )


    elif option == 'PHUL 운동일지_종우.ver':      # option = '531 운동일지_종우.ver' => '531 운동일지_종우.ver'파일다운 

        st.write(':green[PHUL 운동일지_종우.ver]')   # '5X5 운동일지_종우.ver' 텍스트 출력
        st.write('스트렝스 + 볼륨 훈련 프로그램으로써 주 4회 정도로 하며')   #  간략한 설명 출력
        st.write('2분할로 상체,하체로 돌아간다.')       #  간략한 설명 출력
        st.write('파워빌딩 프로그램이다.')     #  간략한 설명 출력

        df = pd.read_csv('PHUL 운동일지_종우.ver.csv')          # csv 파일 불러옴

            #운동일지 다운버튼 생성 

        @st.cache_data
        def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label=":red[Download : PHUL 운동일지]",             # 버튼이름
            data=csv,                                           # 파일 csv 형태
            file_name='PHUL 운동일지_종우.ver.csv',                # 파일이름
            mime='text/csv',
        )


         # 헬스장 페이지
with tab2:
    st.header("_헬스장_")                     # 헤드라인
    image = Image.open('헬스장.jpg')        # 사진첨부
    st.image(image)

        # pd.dataframe()을 사용하여 좌표(위도와 경도)로 헬스장 위치 표현

    df = pd.DataFrame(
        [[35.155530, 129.059505],[35.154320, 129.064299],[35.154558, 129.056651],[35.153880, 129.059337],[35.147070, 129.067026],[35.152377, 129.060026]],                # 구글 지도에서 위치를 검색
        columns=['lat', 'lon'])                    # 헬스장의 위치(위도, 경도)

    st.map(df)                                      # 좌표를 지도에 표시 


        # My Record 페이지

with tab3:
    st.header("_My Record_")                  # 헤드라인
    image = Image.open('기록.png')             # 사진첨부
    st.image(image)


    d = st.date_input(
            "# 운동한 날짜",                        
            datetime.date(2023, 6, 7))              # 운동한 날짜 표시 
    st.write('# Today is:', d)                  


    agree = st.checkbox('complete!')              # check box 만듬

    if agree:                                   
        st.write('Great!')                         # check box 체크시 텍스트 출력

        work_t = st.slider('시간입력(분)', 0, 300, step=1)          # st.slider 을 사용하여 운동시간 표시
        st.write("# 운동시간:", work_t,'분')                        # '분' 표시

        work_k = st.slider('kcal', 0, 100000, step=1)          # st.slider 을 사용하여 운동시간 표시
        st.write("# kcal:", work_k,'kcal')                      # 'kcal' 표시 

        if work_t >= 60:                                       # 운동시간 60분 이상 'awesome!!' 출력
            st.write('# awesome!!')
            st.balloons()                                      # 풍선 효과
        else:                                                  # 운동시간 60분 미만 '수고하셨습니다' 출력
            st.write('# 수고하셨습니다:)')                      # 텍스트 출력 
            
