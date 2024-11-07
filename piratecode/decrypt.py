""" Decrypt Piratecode Module """
import os
import piratecode
from cryptography.fernet import Fernet



def files(file_path, fernet_obj):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    decrypted_combined_data = fernet_obj.decrypt(encrypted_data)
    header_data, decrypted_data = decrypted_combined_data.rsplit(b'|', 1)

    name_length, extension = header_data.decode().rsplit('|', 1)

    base_name = os.path.basename(file_path)[:int(name_length)]
    new_path = os.path.join(os.path.dirname(file_path), base_name + extension)

    with open(new_path, 'wb') as file:
        file.write(decrypted_data)

    os.remove(file_path)


def payloads(payload: bytes, key: bytes | None):
    if not key:
        key = piratecode.get_apiKey()
    return Fernet(key).decrypt(payload)