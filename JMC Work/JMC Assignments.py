import streamlit as st
import pandas as pd
from utilities import *

# Session State stuff ---------------------------------------------------
if 'visit_data' not in st.session_state:
    st.session_state.visit_data = None
else:
    st.session_state.visit_data = get_visits(st.session_state.time_filter, st.session_state.jmc_selected)
    
if 'tour_data' not in st.session_state:
    st.session_state.tour_data = None
    
if 'event_data' not in st.session_state:
    st.session_state.event_data = None

display_filters = ['time_filter', 'jmc_selected']
for d_filter in display_filters:
    if d_filter not in st.session_state:
        st.session_state[d_filter] = None
        

# Main Page -------------------------------------------------------------
st.logo('photos/JMC LOGO (White Text).png', size='large')
st.header(f'Hi {st.session_state.user}! How are you doing?')
# st.title('JMC Activity')
st.divider()

col1, col2 = st.columns([1,1], vertical_alignment='center')
col1.segmented_control('Time Period', ['Campaign Year','1st Sem','2nd Sem'], label_visibility='collapsed',
                       key='time_filter')
col2.selectbox('JMC', all_jmcs, index=None, label_visibility='collapsed', placeholder='JMC', key='jmc_selected')

dashboard, table, editor = st.tabs(["Dashboard","Table","Editor"])

with dashboard:
    cola, colb, colc = st.columns(3)
    cola.metric('Visits', 5, border=True)
    colb.metric('Tours', 6, border=True)
    colc.metric('Events', 7, border=True)
    
with table:
    st.write(st.session_state.jmc_selected)
    st.write(st.session_state.time_filter)
    st.dataframe(st.session_state.visit_data)
    
    
with editor:
    st.write('Data Editor')
    # st.data_editor()