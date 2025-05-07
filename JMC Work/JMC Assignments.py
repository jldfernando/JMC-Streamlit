import streamlit as st
import pandas as pd
from utilities import *

# Session State stuff ---------------------------------------------------
display_filters = ['time_filter', 'jmc_selected']
for d_filter in display_filters:
    if d_filter not in st.session_state:
        st.session_state[d_filter] = None
        
if 'visit_data' not in st.session_state:
    st.session_state.visit_data = get_visits(None, None)
else:
    st.session_state.visit_data = get_visits(st.session_state.time_filter, st.session_state.jmc_selected)
    
if 'tour_data' not in st.session_state:
    st.session_state.tour_data = None
    
if 'event_data' not in st.session_state:
    st.session_state.event_data = None

        

# Main Page -------------------------------------------------------------
st.logo('photos/JMC LOGO (White Text).png', size='large')
st.header(f'Hi {st.session_state.user}! How are you doing?')
# st.title('JMC Activity')
st.divider()

col1, col2 = st.columns([1,1], vertical_alignment='center')
col1.segmented_control('Time Period', ['Campaign Year','1st Sem','2nd Sem'], label_visibility='collapsed',
                       key='time_filter')
col2.selectbox('JMC', jmc_filters, index=None, label_visibility='collapsed', placeholder='JMC', key='jmc_selected')

dashboard, visits, tours, events = st.tabs(["Dashboard","Visits","Tours","Events"])

with dashboard:
    cola, colb, colc = st.columns(3)
    cola.metric('Visits', st.session_state.visit_data.shape[0], border=True)
    colb.metric('Tours', 6, border=True)
    colc.metric('Events', 7, border=True)
    
with visits:
    st.dataframe(st.session_state.visit_data, use_container_width=True, hide_index=True)
    
with tours:
    st.write('Data Editor')
    # st.data_editor()
    
with events:
    st.write('events')