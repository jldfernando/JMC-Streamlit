import streamlit as st
import pandas as pd

## Session State stuff
if 'visits' not in st.session_state:
    st.session_state.visits = pd.read_csv('data/visits.csv', skiprows=1)
    pass

if 'tours' not in st.session_state:
    st.session_state.tours = None
    pass

if 'ext_events' not in st.session_state:
    st.session_state.ext_events = None
    pass

if 'int_events' not in st.session_state:
    st.session_state.int_events = None
    pass

## Main Page
st.logo('photos/JMC LOGO (White Text).png', size='large')
col1, col2 = st.columns([0.15, 0.85], vertical_alignment='center')
col1.image('photos/JMC LOGO (White Text).png', use_container_width=True)
col2.header(f'JMC/CCO Initiatives')

tab1, tab2, tab3, tab4 = st.tabs(['Visits','Tours','External Events','Internal Events'])
with tab1.expander('Filters'):
    st.segmented_control('Filters',['All','Upcoming','Complete','This Week','Next 2 Weeks'])
    st.date_input('Date')
tab1.dataframe(st.session_state.visits)
# tab2.dataframe(st.session_state.tours)
# tab3.dataframe(st.session_state.ext_events)
# tab4.dataframe(st.session_state.int_events)
