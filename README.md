# Piratecode

Piratecode is a Python library designed to facilitate secure encryption and decryption of files and payloads using a custom encryption key. This repository contains the following modules:

- `bytekey.py`
- `__init__.py`
- `decrypt.py`
- `encrypt.py`

## Overview

### bytekey.py

This module is responsible for generating and managing encryption keys.

**Classes**

- `Piratecode`: Represents the encryption key.

**Functions**

- `generate_secure_key(size: int) -> bytes`: Generates a secure random encryption key of the specified size.

**Usage Example**

```python
from piratecode.bytekey import Key

print(Key.key)  # Secure random key bytes
print(Key.size)  # Size of the generated key

Key.size = 64  # Set key size to 64 bytes
Key.key = Piratecode.generate(Key.size)  # Regenerate the key with a new size
print(Key.key)  # Secure random key bytes of size 64
```

### __init__.py

This file serves as the initializer for the package and provides an interface for encryption and decryption functionalities.

**Functions**

- `generate_key()`: Generates a new encryption key.

**Classes**

- `Encrypt`: Contains static methods for file and payload encryption.
  - `files(filepath, fernet_obj)`: Encrypts files.
  - `payloads(payload: bytes, key: str | None = None)`: Encrypts API payloads.

- `Decrypt`: Contains static methods for file and payload decryption.
  - `files(filepath, fernet_obj)`: Decrypts files.
  - `payloads(payload: bytes, key: str | None = None)`: Decrypts API payloads.

### decrypt.py

This module handles decryption of encrypted files and payloads.

**Functions**

- `files(file_path, fernet_obj)`: Decrypts a file using the provided `fernet_obj`.
- `payloads(payload: bytes, key: bytes | None)`: Decrypts an API payload using the provided key.

### encrypt.py

This module handles encryption of files and payloads.

**Functions**

- `files(file_path, fernet_obj)`: Encrypts a file using the provided `fernet_obj`.
- `payloads(payload: bytes, key: bytes | None)`: Encrypts an API payload using the provided key.

## Installation

You can install the package using pip:

```bash
pip install piratecode
```

## Usage

Here is a basic example of how you can use this library to encrypt and decrypt files and payloads:

**Encrypting Files**

```python
from piratecode import Encrypt, Piratecode
from cryptography.fernet import Fernet

fernet_obj = Fernet(Piratecode.generate())
Encrypt.files('path/to/your/file.txt', fernet_obj)
```

**Decrypting Files**

```python
from piratecode import Decrypt, Piratecode
from cryptography.fernet import Fernet

fernet_obj = Fernet(Piratecode.generate())
Decrypt.files('path/to/your/file.piratecode', fernet_obj)
```

**Encrypting Payloads**

```python
encrypted_payload = Encrypt.payloads(b'sample payload')
```

**Decrypting Payloads**

```python
decrypted_payload = Decrypt.payloads(encrypted_payload)
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy coding with Piratecode!
