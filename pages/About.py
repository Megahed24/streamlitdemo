import streamlit as st

st.info('this is a test')

st.success('Welcome to our page!')

st.text_input('what is your name')

st.number_input('what is your age',step= 1)

st.slider('what is your height',min_value=1.00, max_value= 3.00, step= 0.001)
