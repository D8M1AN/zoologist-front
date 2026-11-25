import streamlit as st
from predict import predict
import pandas as pd

"""
# Zoologist front
"""

'''
# Whats that bird 🦅?
'''


island = st.selectbox(
    label='Select:',
    options=[
            'Biscoe',
            "Dream",
            'Torgersen'
            ]
)

sex = st.selectbox(
    label='',
    options=['Male', 'Female']
)

bill_len = st.number_input(
    label='(mm)',
    key=1,
    min_value=0,
    max_value=550
)

bill_depth = st.number_input(
    label='(mm)',
    key=2,
    min_value=0,
    max_value=500
)

flipper_len = st.number_input(
    label='(mm)',
    key=3,
    min_value=0,
    max_value=500
)

bm = st.number_input(
    label='(g)',
    key=4,
    min_value=0
)

data = [
    island,
    bill_len,
    bill_depth,
    flipper_len,
    bm,
    sex
]

if st.button('Predict Bird'):

    prediction = predict(data=data)

    st.success(f'Predicted penguin species {prediction}')
