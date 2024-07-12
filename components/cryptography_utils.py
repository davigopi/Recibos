# from msilib import datasizemask
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidTag
# from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode
import os
import json
import requests
from pathlib import Path


class Key_encrypt:
    def __init__(self, *args, **kwargs) -> None:
        self.key = ''
        self.dictionary_encrypt = ''
        self.path_source = Path(__file__).parent
        if 'components' in self.path_source.parts:
            self.path_tables = self.path_source
        else:
            self.path_tables = self.path_source / 'components'
        self.name_arq = 'crypto_key.json'
        self.arqKey = self.path_tables / self.name_arq
        self.name_arq = 'crypto_user.json'
        self.arqUser = self.path_tables / self.name_arq
        self.url = 'https://raw.githubusercontent.com/davigopi/crypto_user/main/crypto_user.json'  # noqa

        # self.name_arq = 'crypto_user_crypto.json'
        # self.arqUserCrypto = self.path_tables / self.name_arq

    def generate_key(self):
        # Gera uma chave secreta de 256 bits (32 bytes)
        key = os.urandom(32)
        key64 = b64encode(key).decode('utf-8')
        data = {"key": key64}
        with open(self.arqKey, 'w') as file:
            json.dump(data, file, indent=4)
        return data

    def read_key_file(self):
        # ler a chave gerada
        with open(self.arqKey, 'r') as file:
            data = json.load(file)
            key64 = data['key']
            self.key = b64decode(key64)
            return self.key

    def create_user_crypt(self, list_user, list_password):
        list_password_crypt = []
        dictionary_encrypt = {}
        for password in list_password:
            if password != '':
                list_password_crypt.append(self.encrypt(password))
        for index, password_crypt in enumerate(list_password_crypt):
            user = list_user[index]
            dictionary_encrypt[user] = password_crypt
        with open(self.arqUser, 'w') as file:
            file.write('\n')
            json.dump(dictionary_encrypt, file, indent=4)
        return dictionary_encrypt

    def read_user_crypt_web(self):
        response = requests.get(self.url)
        self.dictionary_encrypt = response.json()
        return self.dictionary_encrypt

    def password_decrypt(self, user):
        try:
            password_crypt = self.dictionary_encrypt[user]
        except KeyError:
            print(f"Erro: O usuário {user} não existe.")
            return None
        try:
            password = self.decrypt(password_crypt)
        except InvalidTag:
            print("Erro: key de autenticação inválida.")
            return None
        return password

    def encrypt(self, password):
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv), backend=default_backend())  # noqa
        encryptor = cipher.encryptor()
        password_crypted = encryptor.update(password.encode()) + encryptor.finalize()  # noqa
        tag = encryptor.tag
        return b64encode(iv).decode(
            'utf-8') + '.' + b64encode(password_crypted).decode('utf-8') + '.' + b64encode(tag).decode('utf-8')  # noqa

    def decrypt(self, password_crypted):
        iv_base64, encrypted_base64, tag_base64 = password_crypted.split('.')
        iv = b64decode(iv_base64)
        encrypted_content = b64decode(encrypted_base64)
        tag = b64decode(tag_base64)

        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv, tag), backend=default_backend())  # noqa
        decryptor = cipher.decryptor()

        password_decrypted = decryptor.update(encrypted_content) + decryptor.finalize()  # noqa
        return password_decrypted.decode('utf-8')


if __name__ == '__main__':
    # Exemplos de uso
    key_encrypt = Key_encrypt()
    user0 = "davi"
    senha0 = "3628"
    user1 = "select"
    senha1 = "789321"
    user2 = ""
    senha2 = ""
    user3 = ""
    senha3 = ""

    list_user = [user0, user1, user2, user3]
    list_senha = [senha0, senha1, senha2, senha3]

    # dictionary_key = key_encrypt.generate_key()

    key_encrypt.read_key_file()

    key_encrypt.create_user_crypt(list_user, list_senha)

    key_encrypt.read_user_crypt_web()

    password = key_encrypt.password_decrypt('select')
