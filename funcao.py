import streamlit as st
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def page_init():
    url = 'https://wa.me/13974242919'
    insta_link = 'https://www.instagram.com/corretorfelipecarlos/reels/'
    st.header('Como podemos te ajudar? ', divider='grey')

    visita_bto = st.button(label='Visita', use_container_width=True)
    if visita_bto:
        webbrowser.open_new_tab(url)
    infs_bto = st.button(label='Informações', use_container_width=True)
    outro_bto = st.button(label='Outros imóveis', use_container_width=True)
    if outro_bto:
        webbrowser.open_new_tab(insta_link)
    redes = st.button(label='Contatos', icon='📲')

import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def page_form():
    st.header('Informação sobre outros imóveis', divider='grey')
    form = st.form(key='form', clear_on_submit=True)

    # Use variáveis locais dentro do formulário
    with form:
        nome = st.text_input(label='Nome', placeholder='Nome')
        telefone = st.text_input(label='Telefone', placeholder='Telefone')

        apto = st.checkbox('Apartamento')
        casa = st.checkbox('Casa')
        quartos = st.radio(label='Quartos', options=['1', '2', '3', '4', '+5'], horizontal=True)
        vagas = st.radio(label='Vagas', options=['1', '2', '3', '4', '+5'], horizontal=True)
        bairro = st.selectbox(label='Bairro:',
                              options=['Canto do Forte', 'Boqueirão', 'Guilhermina', 'Aviação',
                                       'Tupi', 'Ocian', 'Mirim', 'Sítio do Campo'])

        permuta = st.checkbox('Permuta')
        vista = st.checkbox('À vista')
        financiamento = st.checkbox('Financiamento bancário')

        submitted = st.form_submit_button('Enviar')

        # Após o envio do formulário, armazene os valores no session_state
        if submitted:
            st.session_state['nome'] = nome
            st.session_state['telefone'] = telefone
            st.session_state['apto'] = apto
            st.session_state['casa'] = casa
            st.session_state['quartos'] = quartos
            st.session_state['vagas'] = vagas
            st.session_state['bairro'] = bairro
            st.session_state['permuta'] = permuta
            st.session_state['vista'] = vista
            st.session_state['financiamento'] = financiamento
            enviar_email()  # Chame a função de envio de e-mail após o envio do formulário

def enviar_email():
    # Extraia as informações do st.session_state para o corpo do e-mail
    nome = st.session_state.get('nome', '')
    telefone = st.session_state.get('telefone', '')
    casa = st.session_state.get('casa', False)
    apto = st.session_state.get('apto', False)
    quartos = st.session_state.get('quartos', '')
    vagas = st.session_state.get('vagas', '')
    bairro = st.session_state.get('bairro', '')
    permuta = st.session_state.get('permuta', False)
    vista = st.session_state.get('vista', False)
    financiamento = st.session_state.get('financiamento', False)

    # Configurações de e-mail
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Novo formulário preenchido"
    mensagem = f"""\
        Nome: {nome}
        Telefone: {telefone}
        Tipo: {'Apartamento' if apto else 'Casa' if casa else 'Não informado'}
        Quartos: {quartos}
        Vagas: {vagas}
        Bairro: {bairro}
        Pagamento: {'Permuta' if permuta else 'À vista' if vista else 'Financiamento' if financiamento else 'Não informado'}
    """
    msg.attach(MIMEText(mensagem, 'plain'))

    # Enviar o e-mail
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        st.success("E-mail enviado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao enviar e-mail: {e}")
