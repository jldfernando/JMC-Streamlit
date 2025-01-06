import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
valid_accounts = {
    'Therese': 'ringring',
    'Gabby': 'ringring',
    'Josh': 'ringring'
}

## Login functions
def login():
    UN = st.text_input('Username')
    PW = st.text_input('Password', type="password")
    if st.button("Log in"):
        if UN in valid_accounts.keys() and PW == valid_accounts[UN]:
            st.session_state.logged_in = True
            st.session_state.user = UN
            st.session_state.user_type = 'Admin'
            st.rerun()
        elif PW == 'TBA':
            st.session_state.logged_in = True
            st.session_state.user = UN
            st.session_state.user_type = 'Guest'
        else:
            st.write('Invalid username or password')

def logout():
    st.write(f'Blaze a trail {st.session_state.user}!')
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

## Define Pages
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
overview = st.Page(
    "Schedule Tracker/Schedule Overview.py", title="Schedule Overview", icon=":material/schedule:", default=True
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
