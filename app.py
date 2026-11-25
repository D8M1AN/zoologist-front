import streamlit as st
import requests

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

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

if st.button('Predict Bird'):


    url = 'http://localhost:8501/'

    req = {
        'island' : island,
        'bill_len' : bill_len,
        'bill_depth' : bill_depth,
        'flipper_len' : flipper_len,
        'body mass' : bm,
        'sex' : sex
    }

    response = requests.get(url, req)

    if response.status_code == 200:
        prediction = response.json()['Prediction']
        st.success(f'Predicted penguin species {prediction}')
    else:
        st.error(f'API error: {response.status_code}')



"""
1. Let's ask for:
- island (the location where the penguin lives: Biscoe, Dream or Torgersen)
- bill length (in mm)
- bill depth (in mm)
- flipper length (in mm)
- body mass (in g)
- sex ("Male" or "Female")
"""

"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""
