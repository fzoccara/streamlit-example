import streamlit as st
import fredapi as fa
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import requests
import yfinance as yf
from streamlit_login_auth_ui.widgets import __login__
fred = fa.Fred(st.secrets['fred'])
from functions import st_button, load_css
#fred = fa.Fred(settings['apikey'])


####################################################################################
st.set_page_config(
    page_title = 'Net Liquidity',
    page_icon = '📊',
    layout = 'wide'
)

__login__obj = __login__(auth_token = st.secrets['courier_auth_token'], 
                    company_name = "The Suite",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout',
                    hide_menu_bool = False, 
                    hide_footer_bool = True, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN != True:
    with open('style4.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if LOGGED_IN == True:
    st.title('Net Liquidity vs S&P 500')
