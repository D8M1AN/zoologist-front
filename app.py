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
    label='Island',
    options=[
            'Biscoe',
            "Dream",
            'Torgersen'
            ]
)

sex = st.selectbox(
    label='Sex',
    options=['Male', 'Female']
)

bill_len = st.number_input(
    label='Bill Length (mm)',
    key=1,
    min_value=0,
    max_value=550
)

bill_depth = st.number_input(
    label='Bill Depth (mm)',
    key=2,
    min_value=0,
    max_value=500
)

flipper_len = st.number_input(
    label='Flipper Length(mm)',
    key=3,
    min_value=0,
    max_value=500
)

bm = st.number_input(
    label='Body Mass (g)',
    key=4,
    min_value=0
)

data = pd.DataFrame([{
    'island': island,
    'bill_length_mm': bill_len,
    'bill_depth_mm': bill_depth,
    'flipper_length_mm': flipper_len,
    'body_mass_g': bm,
    'sex': sex
}])

if st.button('Predict Bird'):

    prediction = predict(data=data)

    st.success(f'Predicted penguin species {prediction}')
