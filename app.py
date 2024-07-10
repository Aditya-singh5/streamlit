import streamlit as st
import pandas as pd

st.title("creating webpage using streamlit")

st.write('The weather is good')

option = st.selectbox(
    "How's the weather today?",
    ('Sunny','Overcast','Rainy','foggy'),

)

st.write('Weather is ',option)

temperature = st.slider('Select the Temperature',0,40,25)
st.write('Temperature is ',temperature)

df = pd.DataFrame(
    {
        'col1':[1,2,3,4,5,6],
        'col2':[23,65,45,89,100,43]
    }
)
st.write(df)
st.line_chart(df)

colors = st.multiselect(
    'What are your favorite colors?',
    ['Red','Yellow','Blue','Green'],
    ['Yellow','Red']
)

st.write('Your colors are ',colors)