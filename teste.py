import streamlit as st
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações de e-mail
sender_email = "jucarlos.jv@gmail.com"
receiver_email = "jucarlos.jv@gmail.com"
password = "qdhq khui gfuz hhci"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Novo formulário preenchido"
mensagem = f""" teste
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



