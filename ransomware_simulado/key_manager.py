'''
# key_manager.py
# Script para gerar e salvar a chave de criptografia

from cryptography.fernet import Fernet

def generate_key():
    """Gera uma chave para criptografia e a salva no arquivo 'secret.key'."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Chave gerada e salva como secret.key")

if __name__ == "__main__":
    generate_key()
'''
