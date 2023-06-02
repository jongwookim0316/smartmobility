import streamlit as st

st.write('# Hi Welcome To My App!')

st.write('안녕하세요:)')        # print()함수와 유사 


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

import streamlit as st

option = st.selectbox(
    '좋아하는 동물은?',
    ('토끼', '고양이', '말','강아지','코끼리'))

st.write('내가 좋아하는 동물은? : ', option, '입니다.')
st.write(f'내가 좋아하는 동물은 {option} 입니다.')

import streamlit as st

txt = st.text_area('자신을 소개해 보세요', '''
    
    ''')
st.write('입력한 내용:', txt)

age = st.slider('나이를 선택 하세요', 0, 130, 25)
st.write("저의 나이는", age, '입니다.')