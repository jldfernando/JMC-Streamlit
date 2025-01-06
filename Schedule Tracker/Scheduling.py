import streamlit as st
import pandas as pd
from utilities import *

## Session State stuff

## Main Page
st.logo('JMC LOGO (White Text).png', size='large')
st.title("JMC Streamlit - Version 1.0 beta")
st.header(f'Hi Capt {st.session_state.user}! What are we scheduling today?')
st.text_area('Write whatever, feature still in development')