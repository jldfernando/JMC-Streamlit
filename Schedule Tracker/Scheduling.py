import streamlit as st
import pandas as pd
from utilities import *

## Session State stuff

## Main Page
st.logo('photos/JMC LOGO (White Text).png', size='large')
st.header(f'Hi Capt {st.session_state.user}! What are we scheduling today?')
with st.expander('Scheduling Form'):
    with st.form('Scheduling Form', border=False):
        event_name = st.text_input('Event_name')
        row1 = st.columns(2)
        event_type = row1[0].selectbox('Type', options=event_options, key='event_type')
        event_date = row1[1].date_input('Date', key='event_date')
        row2 = st.columns(2)
        event_start = row1[0].time_input('Start time', key='event_start')
        event_end = row1[1].time_input('End time', key='event_end')
        submit = st.form_submit_button('Check who\'s available')
        
with st.container(border=True):
    if submit:
        readback = format_input(event_name,event_type, event_date, event_start, event_end)
        results = check_availability(event_type, event_date, event_start, event_end, st.session_state.compiled_schedules)
        st.write(readback)
        st.dataframe(results, use_container_width=True)