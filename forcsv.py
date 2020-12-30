import csv
import streamlit as st
import pandas as pd
# import SessionState
import datetime
from datetime import timedelta


date = datetime.datetime.now()
rg_dt = date.date()
ex_dt = rg_dt + timedelta(30)
lft = (ex_dt - rg_dt).days

def user_update(username,email,password,org_name):
    with open('user.csv','a') as f:
        data = csv.DictWriter(f,lineterminator='\r',fieldnames=['TenantID','username','email','password','org_name','reg_dt','exp_dt','lft_dys'])
        with open('user.csv','r') as read:
            check_data = pd.read_csv(read)
            # if check_data.loc[check_data['org_name'] != org_name]:
            lis = list(check_data['org_name'].unique())
            if org_name in lis:
                index = lis.index(org_name)
                data.writerow({'TenantID': index,
                               'username':str(username),
                               'email':str(email),
                               'password':str(password),
                               'org_name':str(org_name),
                               'reg_dt':f'{rg_dt}',
                               'exp_dt':f'{ex_dt}',
                               'lft_dys':f'{lft}'})
            else:

                data.writerow({'TenantID': len(lis)+1,
                               'username': str(username),
                               'email': str(email),
                               'password': str(password),
                               'org_name': str(org_name),
                               'reg_dt':f'{rg_dt}',
                               'exp_dt':f'{ex_dt}',
                               'lft_dys':f'{lft}'})

def user_check(email,password):
    data = pd.read_csv('user.csv')
    if email in data['email'].values and password in data['password'].values:
        # successful = st.success('User Verified')
        return True
    elif email not in data['email'].values or password not in data['password'].values:
        st.sidebar.text('Your Email OR Password is incorrect')
        return False



