# import streamlit as st
# import webbrowser
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from teste import page_form, email
#
# url = 'https://wa.me/13974242919'
# insta_link = 'https://www.instagram.com/corretorfelipecarlos/reels/'
# tree_link = 'https://linktr.ee/imoveisfelipecarlos'
# st.header('Como podemos te ajudar? ', divider='grey')
#
# st.markdown("[Visita](https://wa.me/13974242919)", unsafe_allow_html=True)
# if 'form' not in st.session_state:
#       st.session_state.form = []
#
# infs_bto = st.button(label='Informações', use_container_width=True)
# if infs_bto:
#       infs = page_form()
#       st.session_state.form = infs
#       email(nome=infs['nome'][0], telefone=infs['telefone'][0], casa=infs['casa'][0], apto=infs['apto'][0],
#             quartos=infs['quartos'][0], vagas=infs['vagas'][0],
#             bairro=infs['bairro'][0], permuta=infs['permuta'][0], vista=infs['vista'][0],
#             financiamento=f'{st.session_state.form}')
#
# st.markdown("[Outros imóveis](https://www.instagram.com/corretorfelipecarlos/reels/)", unsafe_allow_html=True)
#
# st.markdown("[Contatos](https://linktr.ee/imoveisfelipecarlos)", unsafe_allow_html=True)
#
import streamlit as st
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def page_form():
    st.header('Informação sobre outros imóveis', divider='grey')
    form = st.form(key='form', clear_on_submit=True)

    with form:
        st.session_state['nome'] = st.text_input(label='Nome', placeholder='Nome')
        st.session_state['telefone'] = st.text_input(label='Telefone', placeholder='Telefone')

        # Salve os dados no st.session_state conforme são preenchidos
        st.session_state['apto'] = st.checkbox('Apartamento')
        st.session_state['casa'] = st.checkbox('Casa')
        st.session_state['quartos'] = st.radio(label='Quartos', options=['1', '2', '3', '4', '+5'], horizontal=True)
        st.session_state['vagas'] = st.radio(label='Vagas', options=['1', '2', '3', '4', '+5'], horizontal=True)
        st.session_state['bairro'] = st.selectbox(label='Bairro:',
                                                  options=['Canto do Forte', 'Boqueirão', 'Guilhermina', 'Aviação',
                                                           'Tupi', 'Ocian', 'Mirim', 'Sítio do Campo'])

        # Formas de pagamento
        st.session_state['permuta'] = st.checkbox('Permuta')
        st.session_state['vista'] = st.checkbox('À vista')
        st.session_state['financiamento'] = st.checkbox('Financiamento bancário')

        submitted = st.form_submit_button('Enviar')

        if submitted:
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
    sender_email = "seu_email@gmail.com"
    receiver_email = "destinatario@gmail.com"
    password = "sua_senha"

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

page_form()