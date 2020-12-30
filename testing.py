# import pandas as pd
#
# data = pd.read_csv('user.csv')
# user = input('Please enter your id:')
# if user not in data['email'].values:
#     print('adding new user')
# else:
#     print('Already Available')
# import os, random, string
#
# length = 13
# chars = string.ascii_letters + string.digits + '!@#$%^&*()'
# random.seed = (os.urandom(1024))
#
# print(''.join(random.choice(chars) for i in range(length)))
# import pandas as pd
#
# data = pd.read_csv('user.csv')
# print(data[data['email'] == 'scdaniyalalam@gmail.com']['password'])
import streamlit as st

import bokeh
import bokeh.layouts
import bokeh.models
import bokeh.plotting
# import pandas as pd
# # import numpy as np
# # import streamlit as st
# with open('user.csv','r') as f:
#     data = pd.read_csv(f)
#
# print(len(data['TenantID'].unique()))

# x = 'Software Channel Pvt. Ltd.'
# x = x.split()[:-2]
# x = ' '.join(x)
# print(x)

import datetime
from datetime import timedelta
#
# date = datetime.datetime.now().date()
# print(date)
# exp = date + timedelta(10)
# print(exp)
# yes = datetime.datetime.now().date()
# yess = yes + timedelta(1)
# print(yess)
# print((exp-yess).days)
import pandas as pd
import numpy as np

data = pd.read_csv('user.csv')

# rg_dt = datetime.datetime.now().date()
# ex_dt = pd.to_datetime(data[data['email'] == 'scdaniyalalam@gmail.com']['exp_dt'].values[0]).date()
# print(rg_dt)
# print(ex_dt)
# finl = (ex_dt - rg_dt).days
# print(str(finl))
# data.loc[data['email'] == 'scdaniyalalam@gmail.com', ['lft_dys']] = finl
# print(finl)

# print(data)

# if data[data['email'].any() == 'scdaniyalalam@gmail.com']:
#     print(data)
# rg_dt = pd.to_datetime(x['reg_dt'])
# ex_dt = pd.to_datetime(x['exp_dt'])
# finl = (ex_dt - rg_dt)
# finl = finl.astype('str')
# lft = finl.values[0]
# data['lft_dys'] = lft
# data.loc[data['email']=='scdaniyalalam@gmail.com', ['lft_dys']] = 25
# x = np.where(data['email'] == 'scdaniyalalam@gmail.com')
# data.loc[data['email'] == 'scdaniyalalam@gmail.com', ['lft_dys']] = 25
# print(data)
# x = pd.to_datetime(data[data['email'] == 'scdaniyalalam@gmail.com']['reg_dt'].values[0]).date()
# y = datetime.datetime.now().date()
#
# print((y-x).days)

lis = list(data['org_name'])
x = [x.lower().split()[:2] for x in lis]
val = 'software channel pvt. ltd.'
if val.lower().split()[:2] in x:
    print(x)

