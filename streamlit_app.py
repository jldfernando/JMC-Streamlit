import streamlit as st
import csv
from datetime import datetime

if "banner" not in st.session_state:
    st.session_state.banner = False
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
valid_accounts = {
    'Therese': 'ringring',
    'Gabby': 'ringring',
    'Josh': 'ringring'
}

## Dialog
@st.dialog('Failed login')
def invalid():
    st.write('Invalid Username or Password')
    
## Fragment
@st.fragment
def show_banner():
    if st.session_state.banner:
        banner = 'jmc_banner_alt.png'
    else:
        banner = 'jmc_banner.png'
    st.image(banner)

## Login functions
def login():
    show_banner()
    UN = st.text_input('Username')
    PW = st.text_input('Password', type="password")
    if st.button("Log in"):
        if UN in valid_accounts.keys() and PW == valid_accounts[UN]:
            st.session_state.logged_in = True
            st.session_state.user = UN
            st.session_state.user_type = 'Admin'
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('logins.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows([[timestamp,UN, PW, 'Admin']])         
            st.rerun()
        elif PW == 'TBA':
            st.session_state.logged_in = True
            st.session_state.user = UN
            st.session_state.user_type = 'Guest'
            with open('logins.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows([[timestamp, UN, PW, 'Guest']])
            st.rerun()
        else:
            invalid()
    st.toggle('Use alt banner', key='banner')    
        

def logout():
    st.logo('JMC LOGO (White Text).png', size='large')
    st.markdown(f'# Blaze a trail {st.session_state.user}!')
    st.image('jmc_team.JPG')
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

## Define Pages
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
overview = st.Page(
    "Schedule Tracker/Schedule Overview.py", title="Schedule Overview", icon=":material/schedule:", default=True
)
scheduling = st.Page(
    "Schedule Tracker/Scheduling.py", title='Schedule an event', icon=':material/person_check:'
)


## Define Navigation
if st.session_state.logged_in:
    if st.session_state.user_type == 'Admin':
        pg = st.navigation(
            {
                "Account": [logout_page],
                "Schedule": [overview, scheduling],
            }
        )
    else:
        pg = st.navigation(
            {
                "Account": [logout_page],
                "Schedule": [overview]
            }
        )
else:
    pg = st.navigation([login_page])

pg.run()
