from cryptography.fernet import Fernet
import zipfile
import os

def generate_key(key_dir='key.key'):
    key = Fernet.generate_key()
    with open(key_dir, "wb") as key_file:
        key_file.write(key)

if __name__ == '__main__':
    generate_key()
    print("Key generated, please locate the key and store it in a safe location.")
    print("You can now use the key to encrypt and decrypt files.")
    print("For more information, please refer to the documentation.")