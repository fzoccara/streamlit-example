import streamlit as st 
from PIL import Image  
from streamlit_login_auth_ui.widgets import __login__
from functions import show_download_Json

from bob_telegram_tools.bot import TelegramBot

st.set_page_config(
    page_title = 'fzoccara test',
    page_icon = '📈',
    layout = 'centered'
)

__login__obj = __login__(auth_token = st.secrets['courier_auth_token'], 
                    company_name = "test",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout',
                    hide_menu_bool = False, 
                    hide_footer_bool = True, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json'
                    )

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN != True:
    with open('style3.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if LOGGED_IN == True:
    # print(__login__obj)

    # bot = TelegramBot(st.secrets['telegram_bot_token'], st.secrets['telegram_bot_chat'])
    # _ = bot.send_text("test")

    # st.header
    # html_string = "<i>markup for gtm</i>"
    # st.markdown(html_string, unsafe_allow_html=True)


    # with open('_secret_auth_.json') as f:
    #     asd = f.read()
    #     st.markdown("<pre>"+asd+"</pre>", unsafe_allow_html=True)
    #     print(asd)

    # import os
    # print(os.listdir())
    # st.markdown("<pre>"+"<br/>".join(os.listdir())+"</pre>", unsafe_allow_html=True)

    # html_string = "<i>markup for gtm</i>"
    # st.markdown(html_string, unsafe_allow_html=True)
    
    st.markdown("hello world", unsafe_allow_html=True)
try:
    url = st.experimental_get_query_params()
    captured_value = url['get_data'][0]

    if captured_value =='612782549135279473253294137':
        show_download_Json()
except:
    pass