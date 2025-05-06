import streamlit as st
import pandas as pd

st.logo('photos/JMC LOGO (White Text).png', size='large')
st.header(f'Hi {st.session_state.user}! How are you doing?')