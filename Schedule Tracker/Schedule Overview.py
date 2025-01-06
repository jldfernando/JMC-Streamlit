import streamlit as st
import pandas as pd
from utilities import *

### Session State Stuff ---------------------------------------------------------------------------------
if 'indiv_schedules' not in st.session_state:
    file = 'schedules.xlsx'
    sheets_to_drop = ['Read Me!','Dashboard']
    st.session_state.indiv_schedules = get_indiv_schedules_dict(file, sheets_to_drop)

if 'compiled_schedules' not in st.session_state:
    st.session_state.compiled_schedules = compile_schedules(st.session_state.indiv_schedules)
    
display_filters = ['group_filter', 'people_filter']
for d_filter in display_filters:
    if d_filter not in st.session_state:
        st.session_state[d_filter] = []

toggles = ['show_names', 'exclude']
for toggle in toggles:
    if toggle not in st.session_state:
        st.session_state[toggle] = False
    
df, people = update_total_availability_display(st.session_state.compiled_schedules,
                                            st.session_state.group_filter,
                                            st.session_state.people_filter,
                                            st.session_state.show_names,
                                            st.session_state.exclude)

if len(st.session_state.people_filter) == 1 and st.session_state.exclude == False:
    schedule_display = df_highlight_value(df, [1], "darkgreen")
else:
    schedule_display = df_colormap_values(df, 'Greens')
    
def reset_people_filter():
    st.session_state.people_filter = []
    
def check_exclude():
    if st.session_state.people_filter == []:
        st.session_state.exclude = False

def reset_filters():
    for d_filter in display_filters:
        st.session_state[d_filter] = []
    for toggle in toggles:
        st.session_state[toggle] = False

### Main Page -------------------------------------------------------------------------------------
st.logo('photos/JMC LOGO (White Text).png', size='large')
st.header(f'Hi {st.session_state.user}! How are you doing?')

with st.expander("Filters"):
    col1, col2 = st.columns([3,1], vertical_alignment='top')
    col1.segmented_control('Filters', jmc_group_filters.keys(), selection_mode='multi',
                           label_visibility='collapsed', key='group_filter', on_change=reset_people_filter)
    col2.toggle("show names", key='show_names', help='Shows who is available but without the heatmap')
    col1.multiselect('People', people, label_visibility='collapsed', placeholder='Select People', key='people_filter', on_change=check_exclude)
    col2.toggle("Exclude", key='exclude', help='changes the filter to exclude the selected names instead (why though?)')
    col2.button('Reset filters :material/restart_alt:', on_click=reset_filters)

st.dataframe(schedule_display, use_container_width=True, height=982)