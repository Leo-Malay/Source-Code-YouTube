
# Importing the cryptograpy module for using encryption and decryption method.
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Generating the Secret Key
secret_key = "VerySecretKey"
kdf = PBKDF2HMAC(
    algorithm=SHA256(),
    length=32,
    salt="Pass Salt Here".encode(),
    iterations=100000,
)
key = urlsafe_b64encode(kdf.derive(secret_key.encode()))

# Assign the Method to a vaiable and pass the key
token = Fernet(key)


def encrypt(data):
    return token.encrypt(data)


def decrypt(data):
    return token.decrypt(data)
