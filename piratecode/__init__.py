from .bytekey import Piratecode
from .encrypt import files, payloads
from .decrypt import files, payloads


def generate_key():
    return Piratecode.generate()

class Encrypt:
    @staticmethod
    def files(filepath, fernet_obj):
        """Used to encrypt Files only"""
        return encrypt.files(filepath, fernet_obj)

    @staticmethod
    def payloads(payload: bytes, key: str | None = None):
        """Used to encrypt API Payloads only"""
        if not key:
            key = generate_key()
        return encrypt.payloads(payload, key=key)


class Decrypt:
    @staticmethod
    def files(filepath, fernet_obj):
        """Used to decrypt Files only"""
        return decrypt.files(filepath, fernet_obj)

    @staticmethod
    def payloads(payload: bytes, key: str | None = None):
        """Used to decrypt API Payloads only"""
        if not key:
            key = generate_key()
        return decrypt.payloads(payload, key=key)

