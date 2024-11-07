""" Encrypt Piratecode Module """
import os
import piratecode
from cryptography.fernet import Fernet


def files(file_path, fernet_obj):
    with open(file_path, 'rb') as file:
        file_data = file.read()

        filename = os.path.basename(file_path)
        name_without_ext = os.path.splitext(filename)[0]
        extension = os.path.splitext(file_path)[1]

        header = f"{len(name_without_ext)}|{extension}".encode()
        combined_data = header + b'|' + file_data
        encrypted_data = fernet_obj.encrypt(combined_data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

    encrypted_path = os.path.splitext(file_path)[0] + '.piratecode'
    os.rename(file_path, encrypted_path)


def payloads(payload: bytes, key: bytes | None):
    try:
        if not key:
            key = piratecode.get_apiKey()
        return Fernet(key).encrypt(payload)
    except Exception as e:
        print(e)
        return False
