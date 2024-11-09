import streamlit as st
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from funcao import page_form

st.header('Como podemos te ajudar? ', divider='grey')

st.markdown("[Visita](https://wa.me/13974242919)", unsafe_allow_html=True)
if 'form' not in st.session_state:
      st.session_state.form = []

infs_bto = st.button(label='Informações', use_container_width=True)
if infs_bto:
    page_form()

st.markdown("[Outros imóveis](https://www.instagram.com/corretorfelipecarlos/reels/)", unsafe_allow_html=True)

st.markdown("[Contatos](https://linktr.ee/imoveisfelipecarlos)", unsafe_allow_html=True)

