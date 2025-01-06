import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

## Login functions
def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

## Define Pages
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
overview = st.Page(
    "Schedule Tracker/overview.py", title="Schedule Overview", icon=":material/Schedule:", default=True
)


## Define Navigation Directory
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Schedule": [overview]
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
