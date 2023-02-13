import streamlit as st
choosen_algo=st.radio(label='Choose Algorithm',options=['Needleman','Smith_Waterman'])
seq_1=st.text_input("Enter Sequence 1")
seq_2=st.text_input("Enter Sequence 2")
button=st.button("Submit")

