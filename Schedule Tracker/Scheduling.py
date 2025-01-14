import streamlit as st
import pandas as pd
from utilities import *

## Session State stuff
if 'readback' not in st.session_state:
    st.session_state.readback = 'None'

if 'results' not in st.session_state:
    st.session_state.results = None
    
if 'indiv_sched' not in st.session_state:
    st.session_state.indiv_sched = 'Eara Cayañga'
    
def prev_sched():
    index = all_jmcs.index(st.session_state.indiv_sched)
    if index != 0:
        new_index = index-1
    else:
        new_index = len(all_jmcs)-1
    next_jmc = all_jmcs[new_index]
    st.session_state.indiv_sched = next_jmc

def next_sched():
    index = all_jmcs.index(st.session_state.indiv_sched)
    if index != len(all_jmcs) - 1:
        new_index = index+1
    else:
        new_index = 0
    next_jmc = all_jmcs[new_index]
    st.session_state.indiv_sched = next_jmc
    
indiv_df = update_indiv_display(st.session_state.indiv_sched)
display_df = df_highlight_value(indiv_df)

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
        st.session_state.readback = format_input(event_name,event_type, event_date, event_start, event_end)
        st.session_state.results = check_availability(event_type, event_date, event_start, event_end, st.session_state.compiled_schedules)
    st.write(st.session_state.readback)
    st.dataframe(st.session_state.results, use_container_width=True)
        
left, center, right = st.columns([0.1, 0.8, 0.1], vertical_alignment='bottom')
left.button(":material/arrow_back_ios:", on_click=prev_sched)
center.selectbox('JMC',all_jmcs, label_visibility='collapsed', key='indiv_sched')
right.button(":material/arrow_forward_ios:", on_click=next_sched)
st.dataframe(display_df, use_container_width=True, height=982)