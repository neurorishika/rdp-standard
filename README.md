# RDP: Rishika's Data Protection for Python

This is a collection of general purpose data protection scripts for Python used by [Rishika Mohanta](https://neurorishika.github.io) for protecting data in her research. It is based on AES-128 (Fernet) encryption and decryption. It is a wrapper around the [cryptography](https://cryptography.io/en/latest/) library.

## Usage

`rdp_gen.py` can be used to generate a new `key.key` file for use in projects. This key is used to encrypt and decrypt data. The generated key will have to be placed in the same directory as the project using the RDP encryption standard.

`*.ezip` files are encrypted zip files used to store data under the RDP standard. The `rdp_client.py` module includes the following functions for use in projects:

- [x] `rdp_client.unlock_and_unzip_file(data2unzip, key_dir='key.key')` which takes in a `*.ezip` file and returns the unzipped data in the same directory as the `*.ezip` file.
- [x] `rdp_client.zip_and_lock_file(data2zip, key_dir='key.key')` which takes in data and returns a `*.ezip` file in the same directory as the data.

## Installation

Make sure you have python >=3.9 and cryptography installed. If not, run `pip install cryptography` in your terminal.

Place the `rdp_client.py` in the same directory as the project using the RDP standard. The `key.key` file for that project should also be placed in the same directory. The `rdp_gen.py` file can be used to generate a new `key.key` file.

Finally, add the following lines to your `.gitignore` file:

```
# key files anywhere in the project directory and subfolders
*.key
# data files anywhere in the project directory and subfolders
**/data/*
# unprotected zip files anywhere in the project directory and subfolders
**/*.zip
```