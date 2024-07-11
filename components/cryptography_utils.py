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
        self.key64 = ''
        self.path_source = Path(__file__).parent
        if 'components' in self.path_source.parts:
            self.path_tables = self.path_source
        else:
            self.path_tables = self.path_source / 'components'
        self.name_arq = 'crypto_key.json'
        self.arqKey = self.path_tables / self.name_arq
        self.name_arq = 'crypto_user.json'
        self.arqUser = self.path_tables / self.name_arq
        self.name_arq = 'crypto_user_crypto.json'
        self.arqUserCrypto = self.path_tables / self.name_arq

    def generate_key(self):
        # Gera uma chave secreta de 256 bits (32 bytes)
        self.key = os.urandom(32)
        self.key64 = b64encode(self.key).decode('utf-8')
        data = {"key": self.key64}
        with open(self.arqKey, 'w') as file:
            json.dump(data, file, indent=4)

    def read_key_from_file(self):
        # ler a chave gerada
        with open(self.arqKey, 'r') as file:
            data = json.load(file)
            self.key64 = data['key']
            self.key = b64decode(self.key64)
            return self.key

    def create_user_crypt(self, list_user, list_password):
        list_password_crypt = []
        dictionary_encrypt = {}
        # for user in list_user:
        #     list_user_crypt.append(self.encrypt(user))
        for password in list_password:
            if password != '':
                list_password_crypt.append(self.encrypt(password))
        for index, password_crypt in enumerate(list_password_crypt):
            user = list_user[index]
            dictionary_encrypt[user] = password_crypt
        with open(self.arqUser, 'w') as file:
            file.write('\n')
            json.dump(dictionary_encrypt, file, indent=4)
        print(f'Chave gerada e salva: {dictionary_encrypt}')
        return dictionary_encrypt

    def decrypt_user(self, user):
        with open(self.arqUser, 'r') as file:
            dictionary_encrypt = json.load(file)
            try:
                password_crypt = dictionary_encrypt[user]
            except KeyError:
                print(f"Erro: O usuário {user} não existe.")
                return None
            try:
                password = self.decrypt(password_crypt)
            except InvalidTag:
                print("Erro: key de autenticação inválida.")
                return None
            return password

    def encrypt(self, text):
        # self.key = self.generate_key()
        iv = os.urandom(12)  # Gera um vetor de inicialização de 12 bytes
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv), backend=default_backend())  # noqa
        encryptor = cipher.encryptor()

        encrypted_text = encryptor.update(text.encode()) + encryptor.finalize()
        tag = encryptor.tag
        return b64encode(iv).decode(
            'utf-8') + '.' + b64encode(encrypted_text).decode('utf-8') + '.' + b64encode(tag).decode('utf-8')  # noqa

    def decrypt(self, encrypted_text):
        # self.key = generate_key()
        iv_base64, encrypted_base64, tag_base64 = encrypted_text.split('.')
        iv = b64decode(iv_base64)
        encrypted_content = b64decode(encrypted_base64)
        tag = b64decode(tag_base64)

        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv, tag), backend=default_backend())  # noqa
        decryptor = cipher.decryptor()

        decrypted_text = decryptor.update(encrypted_content) + decryptor.finalize()  # noqa
        return decrypted_text.decode('utf-8')

    def import_repository(self):

        # URL do arquivo JSON no seu repositório do GitHub
        url = 'https://github.com/davigopi/crypto_user/blob/main/crypto_user.json'

        # Faz uma solicitação GET para obter o conteúdo do arquivo
        response = requests.get(url)

        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Content:", response.content[:100])
        # data = response.json()
        # Verifica se a solicitação foi bem-sucedida
        # if response.status_code == 200:
        #     # Converte o conteúdo da resposta para JSON
        #     data = response.json()
        #     print(data)
        # else:
        #     print(f"Erro ao acessar o arquivo: {response.status_code}")
        return response


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

    # key_encrypt.generate_key()

    key_encrypt.read_key_from_file()

    key_encrypt.create_user_crypt(list_user, list_senha)

    password = key_encrypt.decrypt_user('select')

    print(password)

    data = key_encrypt.import_repository()

    # print(data)
