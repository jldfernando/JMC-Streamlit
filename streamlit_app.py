import streamlit as st

if "banner" not in st.session_state:
    st.session_state.banner = 'jmc_banner.png'
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

## Login functions
def login():
    with st.container():
        st.image(st.session_state.banner)
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
            invalid()
            
    if not st.toggle('Use alt banner'):
        st.session_state.banner = 'jmc_banner_alt.png'
    else:
        st.session_state.banner = 'jmc_banner.png'
        

def logout():
    st.markdown(f'# Blaze a trail {st.session_state.user}!')
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
