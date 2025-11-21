'''
# decrypt.py
# Script para descriptografar os arquivos

import os
from cryptography.fernet import Fernet

# Carrega a chave
try:
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    print("Erro: Arquivo 'secret.key' não encontrado. Não é possível descriptografar.")
    exit()

cipher = Fernet(key)

# Diretório dos arquivos
target_dir = "arquivos_teste"

# Lista os arquivos no diretório (exceto a própria nota de resgate)
files_to_decrypt = []
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file != "LEIA_ME.txt":
            files_to_decrypt.append(os.path.join(root, file))

# Descriptografa cada arquivo
for file_path in files_to_decrypt:
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        print(f"Arquivo descriptografado: {file_path}")
    except Exception as e:
        print(f"Falha ao descriptografar {file_path}: {e}")

# Remove a mensagem de resgate
rescue_file = os.path.join(target_dir, "LEIA_ME.txt")
if os.path.exists(rescue_file):
    os.remove(rescue_file)
    print("\nMensagem de resgate removida.")
'''
