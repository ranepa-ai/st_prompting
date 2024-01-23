import pandas as pd
from io import BytesIO
import requests

import streamlit as st
from streamlit_option_menu import option_menu

from pages_list import *


r = requests.get('https://docs.google.com/spreadsheet/ccc?key=1ePOZXadY5GG1L7yXrfSgNpa-JKeeHgfrYYogdDVTi2k&output=csv')
df_search = pd.read_csv(BytesIO(r.content), index_col=0)


st.set_page_config(page_title="Лаборатория цифровых компетенций", page_icon="👾", layout="wide")

with st.sidebar:
    redirect_url = "http://83.143.66.61:27369/"
    logo_image = 'https://raw.githubusercontent.com/Chetoff1228/images/main/logo.png'
    st.markdown(f'<a href="{redirect_url}"><img src="{logo_image}" alt="Foo" width="150" height="150"/></a>', unsafe_allow_html=True)
  
with st.sidebar:
    selected = option_menu('', ["🚀 Введение", "🔍 Теория", "🧩 Проверка знаний", "📜 Практика", "🔄 Заключение"])

if selected == "🚀 Введение":
    intro_page()
elif selected == "🔍 Теория":
    theory_page()
elif selected == "🧩 Проверка знаний":
    check_page()
elif selected == "📜 Практика":
    practice_page()
else:
    result_page(df_search)
