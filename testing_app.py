import streamlit as st
st.set_page_config(layout='wide')
from load import local_css
import pandas as pd
from forcsv import user_update,user_check
from send_email import send_email
from resend_email import resend_email
import app
import os, random, string,time,datetime
from streamlit.hashing import _CodeHasher

try:
    # Before Streamlit 0.65
    from streamlit.ReportThread import get_report_ctx
    from streamlit.server.Server import Server
except ModuleNotFoundError:
    # After Streamlit 0.65
    from streamlit.report_thread import get_report_ctx
    from streamlit.server.server import Server
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def main():
    # Register your pages
    pages = {
        "Login": page_first,
        "Signup": page_second
    }
    local_css("style.css")
    t = "<div><span class='highlight blue' style='text-align:center; font-family:Roboto; font-size:20.5px;'><b>BANK RECONCILIATION</b> </span></div>"
    st.sidebar.markdown(t, unsafe_allow_html=True)
    st.sidebar.write('')
    st.sidebar.write('')
    lov = ['Sign-in', 'Sign-up']

    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))
    #page = st.sidebar.radio("Select your page", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page]()




def page_first():

    st.sidebar.title('Sign-in')
    st.sidebar.write('Please insert the Credentials below')
    email = st.sidebar.text_input(label='Email')
    pwd = st.sidebar.text_input(label='Password', type='password')
    btn = st.sidebar.beta_columns((9, 20))
    butn = btn[0].checkbox('Signin')
    butn_frgt = btn[1].checkbox('Forget Password')

    if butn:
        x = user_check(email=str(email), password=str(pwd))
        if x == True:
            data = pd.read_csv('user.csv')
            rg_dt = datetime.datetime.now().date()
            ex_dt = pd.to_datetime(data[data['email'] == email]['exp_dt'].values[0]).date()
            finl = (ex_dt - rg_dt).days
            finl = finl
            data.loc[data['email'] == email, ['lft_dys']] = finl
            data.to_csv('user.csv',index=False)
            data = pd.read_csv('user.csv')
            check = data[data['email'] == email]['lft_dys'].values[0]
            if check <= 0:
                st.subheader('Your trial has been ended, Email us @ scdaniyalalam@gmail.com')
            else:
                username = data[data['email'] == email]['username'].values[0]
                trial_dy = data[data['email'] == email]['lft_dys'].values[0]
                st.sidebar.subheader(f"Hello {username}") # \nTrial is ending in {trial_dy} day's
                # st.sidebar.selectbox('',options=['Bank Reconciliation'])
                st.sidebar.markdown(
                    f"<div><a><b>Trial is ending in</b> </a><span class='highlight blue' style='text-align:center; font-family:Roboto; font-size:15.5px;'><b>{trial_dy}</b></span> <a><b>day's</b></a></div>",
                    unsafe_allow_html=True)
                st.sidebar.text('')
                main_pg = {
                    'Bank Reconciliation': page_third
                }
                m_page = st.sidebar.selectbox("Select your page", tuple(main_pg.keys()))
                # page = st.sidebar.radio("Select your page", tuple(pages.keys()))

                # Display the selected page with the session state
                main_pg[m_page]()


    elif butn_frgt:
        email = st.sidebar.text_input('Email', key='email')
        data = pd.read_csv('user.csv')
        if st.sidebar.checkbox('Send Email'):
            if email in data['email'].values:
                name = data[data['email'] == email]['username'].values[0]
                pwd = data[data['email'] == email]['password'].values[0]
                resend_email(name=name, password=pwd, reciver_addr=email)
                st.sidebar.success('Please check your Inbox.')
            else:
                st.warning('You are not registered')



def page_second():
    st.title('Sign-up')
    st.write('Please fill the form below')
    sigup = st.beta_columns((12, 12))
    name = sigup[0].text_input(label='Name')
    org_name = sigup[1].text_input(label='Organization Name')
    email = st.text_input(label='Email')
    veri = st.beta_columns((12, 12))
    signup_btn = veri[0].checkbox('Sign-up')
    if signup_btn:
        data = pd.read_csv('user.csv')
        if email not in data['email'].values:
            length = 13
            chars = string.ascii_letters + string.digits + '!@#$%^&*()'
            random.seed = (os.urandom(1024))
            pwd = ''.join(random.choice(chars) for i in range(length))
            user_update(username=name, email=email, password=pwd, org_name=org_name)
            send_email(name=name, password=pwd, reciver_addr=email)
            st.success('Verification Email has been sent to your Email address')
        else:
            st.warning('Your email is already been used')


def page_third():
    app.app()


if __name__ == "__main__":
    main()