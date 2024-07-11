from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidTag
# from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode
import os
import json
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

    def create_user_crypt(self, user, password):
        user_encrypt = self.encrypt(user)
        password_encrypt = self.encrypt(password)
        data = {"user": user_encrypt, "password": password_encrypt}
        with open(self.arqUser, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'Chave gerada e salva: {data}')
        return data

    def decrypt_user(self):
        with open(self.arqUser, 'r') as file:
            data = json.load(file)
            user_encrypt = data["user"]
            password_encrypt = data["password"]
            try:
                user = self.decrypt(user_encrypt)
                password = self.decrypt(password_encrypt)
                list_user = [user, password]
            except InvalidTag:
                print("Erro: tag de autenticação inválida. A mensagem pode ter sido adulterada.")
                return None

            return list_user

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


if __name__ == '__main__':
    # Exemplos de uso
    key_encrypt = Key_encrypt()
    user = "select"
    senha = '789321'
    # key_encrypt.generate_key()

    key_encrypt.read_key_from_file()

    key_encrypt.create_user_crypt(user, senha)

    list_user = key_encrypt.decrypt_user()

    print(list_user)
