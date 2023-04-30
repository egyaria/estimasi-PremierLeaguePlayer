import pickle
import streamlit as st

model = pickle.load(open('estimasi_goal.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Goal Premier League Player')


GP = st.number_input('Input Game dimainkan')
GS = st.number_input('Input Permainan dimulai')
MIN = st.number_input('Input Menit dimainkan')
ASST = st.number_input('Input Assist')
SHOTS = st.number_input('Input Total tembakan')
SOG = st.number_input('Input Tembakan ke gawang')

predict = ''

if st.button('Cetak Goal'):
    predict = model.predict(
        [[GP,GS,MIN,ASST,SHOTS,SOG]]
    )
    st.write ('Estimasi jumlah Goal Para Pemain Liga Inggris : ', predict)