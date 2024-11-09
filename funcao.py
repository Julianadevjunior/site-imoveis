import streamlit as st
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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


def page_form():
    st.header('Informação sobre outros imóveis', divider='grey')

    form = st.form(key='form', clear_on_submit=True, enter_to_submit=True, border=True)

    with form:
        nome = st.text_input(label='Nome', placeholder='Nome')
        telefone = st.text_input(label='Telefone', placeholder='Telefone')

        col_casa, col_apto, colpausa = st.columns([20, 20, 40])
        with col_apto:
            apto = st.checkbox('Apartamento')
        with col_casa:
            casa = st.checkbox('Casa')

        quartos = st.radio(label='Quartos', options=['1', '2', '3', '4', '+5'], horizontal=True)
        vagas = st.radio(label='Vagas', options=['1', '2', '3', '4', '+5'], horizontal=True)
        bairro = st.selectbox(label='Bairro:', options=['Canto do Forte', 'Boqueirão',
                                                        'Guilhermina', 'Aviação',
                                                        'Tupi', 'Ocian',
                                                        'Mirim', 'Sítio do Campo', ])
        st.text('Forma de pagamento:')
        col_permuta, col_vista, col_financiamento = st.columns(3)
        with col_permuta:
            permuta = st.checkbox('Permuta')
        with col_vista:
            vista = st.checkbox('À vista')
        with col_financiamento:
            financimento = st.checkbox('Financiamento bancário')
        st.form_submit_button('Enviar')

        infs_form = {'nome': [nome], 'telefone': [telefone], 'casa': [casa],
                     'apto': [apto], 'quartos': [quartos], 'vagas': [vagas],
                     'bairro': [bairro], 'permuta': [permuta], 'vista': [vista],
                     'financimento': [financimento]}

        return infs_form


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
