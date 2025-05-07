import streamlit as st
import pandas as pd
from utilities import *

# Session State stuff ---------------------------------------------------
display_filters = ['time_filter', 'jmc_selected']
for d_filter in display_filters:
    if d_filter not in st.session_state:
        st.session_state[d_filter] = None

st.session_state.jmc_selected = st.session_state.user

if 'visit_data' not in st.session_state:
    st.session_state.visit_data = get_visits(None, None)
else:
    st.session_state.visit_data = get_visits(st.session_state.time_filter, st.session_state.jmc_selected)
    
if 'tour_data' not in st.session_state:
    st.session_state.tour_data = get_tours(None, None)
else:
    st.session_state.tour_data = get_tours(st.session_state.time_filter, st.session_state.jmc_selected)
    
if 'event_data' not in st.session_state:
    st.session_state.event_data = None

if 'plot_data' not in st.session_state:
    st.session_state.plot_data = get_plot_data(st.session_state.visit_data, st.session_state.tour_data)
else:
    st.session_state.plot_data = get_plot_data(st.session_state.visit_data, st.session_state.tour_data)

# Main Page -------------------------------------------------------------
st.logo('photos/JMC LOGO (White Text).png', size='large')
st.header(f'Hi {st.session_state.user}! How are you doing?')
# st.title('JMC Activity')
# st.divider()

st.segmented_control('Time Period', ['Campaign Year','1st Sem','2nd Sem'], label_visibility='collapsed',
                       key='time_filter')

dashboard, visits, tours, events = st.tabs(["Dashboard","Visits","Tours","Events"])

with dashboard:
    cola, colb, colc = st.columns(3)
    cola.metric('Visits', st.session_state.visit_data.shape[0], border=True)
    colb.metric('Tours', st.session_state.tour_data.shape[0], border=True)
    colc.metric('Events', 'N/A', border=True)
    cold, cole, colf,colg,colh = st.columns(5)
    cold.metric('MT', st.session_state.visit_data['MT'].sum(), border=True)
    cole.metric('Modules', st.session_state.visit_data['Module'].sum(), border=True)
    colf.metric('Fairs', st.session_state.visit_data['Fair'].sum(), border=True)
    colg.metric('Onsite', st.session_state.visit_data['Onsite'].sum(), border=True)
    colh.metric('Online', st.session_state.visit_data['Online'].sum(), border=True)
    with st.container(border=True):
        st.subheader('2024-2025 Visits')
        st.line_chart(st.session_state.plot_data, color=['#F6BE00', '#A70012'])
        # st.dataframe(st.session_state.plot_data)
    
with visits:
    st.dataframe(st.session_state.visit_data[st.session_state.visit_data.columns[:-1]], use_container_width=True, hide_index=True)
    
with tours:
    st.dataframe(st.session_state.tour_data[st.session_state.tour_data.columns[:-1]], use_container_width=True, hide_index=True)
    # st.data_editor()
    
with events:
    st.write('To Be Added')