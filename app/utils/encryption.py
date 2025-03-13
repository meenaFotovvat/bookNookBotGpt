import os
import base64
import gzip
from cryptography.fernet import Fernet

encryption_key = os.getenv("ENCRYPTION_KEY").encode()
cipher = Fernet(encryption_key)

def compress_data(data: bytes) -> bytes:
    return gzip.compress(data)

def decompress_data(data: bytes) -> bytes:
    return gzip.decompress(data)

def encrypt_session(data: bytes) -> str:
    return base64.b64encode(cipher.encrypt(compress_data(data))).decode()

def decrypt_session(data: str) -> bytes:
    return decompress_data(cipher.decrypt(base64.b64decode(data)))
