"""
Piratecode Key Generation Module
================================

This module is used to create a `Piratecode` object which will be used for encryption.

Classes
-------
Piratecode:
    A class to represent the encryption key.

Functions
---------
generate_secure_key(size: int) -> bytes:
    Generates a secure random encryption key of specified size.

Attributes
----------
Key : Piratecode
    An instance of Piratecode with a securely generated key.

Example
-------
>>> from piratecode.bytekey import Key
>>> print(Key.key)
b''  # Secure random key bytes
>>> print(Key.size)
32  # Size of the generated key
>>> Key.size = 64  # Set key size to 64 bytes
>>> Key.key = Piratecode.generate(Key.size)  # Regenerate the key with new size
>>> print(Key.key)
b''  # Secure random key bytes of size 64
"""

import os, base64, re, ast
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class Piratecode:
    """
    A class to represent the encryption key.

    Attributes
    ----------
    key : bytes
        The encryption key.
    size : int
        The size of the encryption key.

    Methods
    -------
    generate(size: int = 32) -> bytes:
        Generates a secure random encryption key.
    """

    def __init__(self, key: bytes, size: int = 32):
        """
        Constructs the necessary attributes for the Piratecode object.

        Parameters
        ----------
        key : bytes
            The encryption key.
        size : int, optional
            The size of the encryption key (default is 32 bytes).
        """
        self.key = key
        self.size = size

    @staticmethod
    def generate(size: int = 32) -> bytes:
        """
        Generates a secure random encryption key.

        This function uses the `secrets` module to generate a secure random key of specified size.

        Parameters
        ----------
        size : int, optional
            The size of the encryption key to generate (default is 32 bytes).

        Returns
        -------
        bytes
            A securely generated random encryption key.
        """
        return base64.urlsafe_b64encode(os.urandom(size))

    @staticmethod
    def derive(context: bytes, salt: bytes, length: int = 32) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=length,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(context))

# Create a Piratecode object called Key with a default key size of 32 bytes
Key = Piratecode(Piratecode.generate())


