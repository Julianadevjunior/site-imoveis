import streamlit as st
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from funcao import page_form, email

url = 'https://wa.me/13974242919'
insta_link = 'https://www.instagram.com/corretorfelipecarlos/reels/'
tree_link = 'https://linktr.ee/imoveisfelipecarlos'
st.header('Como podemos te ajudar? ', divider='grey')

visita_bto = st.button(label='Visita', use_container_width=True)
st.markdown("[Visita](https://wa.me/13974242919)", unsafe_allow_html=True)

infs_bto = st.button(label='Informações', use_container_width=True)
if infs_bto:
      infs = page_form()
      email(nome=infs['nome'][0], telefone=infs['telefone'][0], casa=infs['casa'][0], apto=infs['apto'][0],
            quartos=infs['quartos'][0], vagas=infs['vagas'][0],
            bairro=infs['bairro'][0], permuta=infs['permuta'][0], vista=infs['vista'][0],
            financiamento=infs['financimento'][0])
outro_bto = st.button(label='Outros imóveis', use_container_width=True)
if outro_bto:
      webbrowser.open_new_tab(insta_link)

redes = st.button(label='Contatos', icon='📲')
if redes:
      webbrowser.open_new_tab(tree_link)