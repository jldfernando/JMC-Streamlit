import streamlit as st
import pandas as pd
from utilities import *

## Session State stuff

## Main Page
st.logo('photos/JMC LOGO (White Text).png', size='large')
st.header(f'Hi Capt {st.session_state.user}! What are we scheduling today?')
st.selectbox('type', options=['Visit','Tour','Event'])
st.date_input('Date')
st.time_input('Time')
st.text_area('Write whatever, feature still in development')