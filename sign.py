import streamlit as st
from load import local_css
import pandas as pd
from forcsv import user_update,user_check
from send_email import send_email
from resend_email import resend_email
import os, random, string





st.set_page_config(initial_sidebar_state='collapsed')
local_css("style.css")
t = "<div><span class='highlight blue' style='text-align:center; font-family:Roboto; font-size:20.5px;'><b>BANK RECONCILIATION</b> </span></div>"
st.sidebar.markdown(t, unsafe_allow_html=True)
st.sidebar.write('')
st.sidebar.write('')
lov = ['Sign-in','Sign-up']

select = st.sidebar.beta_columns((12,1))

main = select[0].selectbox('Please verify first',options=lov,index=0)


if main == 'Sign-in':
    st.title('Sign-in')
    st.write('Please insert the Credentials below')
    email = st.text_input(label='Email')
    pwd = st.text_input(label='Password',type='password')
    btn = st.beta_columns((9,70))
    butn = btn[0].button('Sign-in')
    butn_frgt = btn[1].button('Forget Password')

    if butn:
        x = user_check(email=str(email), password=str(pwd))
        # if x == True:
        #     href = f'<a href="http://192.168.1.89:1253">Continue</a>'
        #     st.markdown(href, unsafe_allow_html=True)
    elif butn_frgt:
        email = st.text_input('Email',key='email')
        data = pd.read_csv('user.csv')
        name = data[data['email'] == email]['username']
        pwd = data[data['email'] == email]['password']
        if st.button('Submit'):
            resend_email(name=name,password=pwd,reciver_addr=email)

if main == 'Sign-up':
    st.title('Sign-up')
    st.write('Please fill the form below')
    sigup = st.beta_columns((12,12))
    name = sigup[0].text_input(label='Name')
    org_name = sigup[1].text_input(label='Organization Name')
    email = st.text_input(label='Email')
    veri = st.beta_columns((12,12))
    signup_btn = veri[0].button('Sign-up')
    if signup_btn:
        data = pd.read_csv('user.csv')
        if email not in data['email'].values:
            length = 13
            chars = string.ascii_letters + string.digits + '!@#$%^&*()'
            random.seed = (os.urandom(1024))
            pwd = ''.join(random.choice(chars) for i in range(length))
            user_update(username=name, email=email, password=pwd,org_name=org_name.lower().split()[:2])
            send_email(name=name,password=pwd,reciver_addr=email)
            st.success('Verification Email has been sent to your Email address')
        else:
            st.warning('Your Email is already been used')



