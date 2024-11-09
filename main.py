import streamlit as st
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from teste import page_form


url = 'https://wa.me/13974242919'
insta_link = 'https://www.instagram.com/corretorfelipecarlos/reels/'
tree_link = 'https://linktr.ee/imoveisfelipecarlos'
st.header('Como podemos te ajudar? ', divider='grey')

def email(nome='', telefone='', casa='', apto='', quartos='', vagas='', bairro='', permuta='', vista='', financiamento=''):
    # Configurações de e-mail
    sender_email = "jucarlos.jv@gmail.com"
    receiver_email = "jucarlos.jv@gmail.com"
    password = "qdhq khui gfuz hhci"

    def enviar_email(mensagem):
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Novo formulário preenchido"
        msg.attach(MIMEText(mensagem, 'plain'))

        # Enviando o e-mail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

    # Chame a função ao final do preenchimento do formulário
    enviar_email(f'''Uma nova resposta foi enviada no formulário!
    Nome:{nome}, telefone:{telefone}
    Casa:{casa}, Apto: {apto}
    Quatos:{quartos}, vagas: {vagas}
    Bairro: {bairro}, permuta:{permuta}, à vista:{vista}, financiamento:{financiamento}
    ''')


st.markdown("[Visita](https://wa.me/13974242919)", unsafe_allow_html=True)
if 'form' not in st.session_state:
      st.session_state.form = []

infs_bto = st.button(label='Informações', use_container_width=True)
if infs_bto:
      infs = page_form()
      st.session_state.form = infs
      email(nome=infs['nome'][0], telefone=infs['telefone'][0], casa=infs['casa'][0], apto=infs['apto'][0],
            quartos=infs['quartos'][0], vagas=infs['vagas'][0],
            bairro=infs['bairro'][0], permuta=infs['permuta'][0], vista=infs['vista'][0],
            financiamento=f'{st.session_state.form}')

st.markdown("[Outros imóveis](https://www.instagram.com/corretorfelipecarlos/reels/)", unsafe_allow_html=True)

st.markdown("[Contatos](https://linktr.ee/imoveisfelipecarlos)", unsafe_allow_html=True)

