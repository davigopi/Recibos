from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidTag
from base64 import b64decode
import json
import requests
from pathlib import Path
import sys

try:
    from path_file import Path_file
except ImportError:
    parent_dir = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(parent_dir))
    try:
        from path_file import Path_file
    except ImportError:
        raise ImportError("Não foi possível importar 'Path_fiel'")


class Key_encrypt:
    def __init__(self, *args, **kwargs) -> None:
        self.key = ''
        self.dictionary_encrypt = ''
        path_file = Path_file()
        self.arqKey = path_file.path_file_create('components', 'crypto_key.json')  # noqa
        self.arqUser = path_file.path_file_create('components', 'crypto_user.json')  # noqa
        self.url = 'https://raw.githubusercontent.com/davigopi/crypto_user/main/crypto_user.json'  # noqa

    def read_key_file(self):
        # ler a chave gerada
        with open(self.arqKey, 'r') as file:
            data = json.load(file)
            key64 = data['key']
            self.key = b64decode(key64)
            return self.key

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

    def decrypt(self, password_crypted):
        iv_base64, encrypted_base64, tag_base64 = password_crypted.split('.')
        iv = b64decode(iv_base64)
        encrypted_content = b64decode(encrypted_base64)
        tag = b64decode(tag_base64)
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv, tag), backend=default_backend())  # type: ignore # noqa
        decryptor = cipher.decryptor()
        password_decrypted = decryptor.update(encrypted_content) + decryptor.finalize()  # noqa
        return password_decrypted.decode('utf-8')
