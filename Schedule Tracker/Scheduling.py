import streamlit as st
import pandas as pd
from utilities import *

## Session State stuff

## Main Page
st.logo('photos/JMC LOGO (White Text).png', size='large')
st.header(f'Hi Capt {st.session_state.user}! What are we scheduling today?')
with st.form('Scheduling Form'):
    row1 = st.columns(2)
    event_type = row1[0].selectbox('Type', options=['Visit','Tour','Event'])
    event_date = row1[1].date_input('Date')
    row2 = st.columns(2)
    event_start = row1[0].time_input('Start time')
    event_end = row1[1].time_input('End time')
    st.form_submit_button('Check who\'s available')
with st.container(border=True):
    st.text(f'The {event_type} is on {event_date} from {event_start} to {event_end}')
st.text_area('Write whatever, feature still in development')