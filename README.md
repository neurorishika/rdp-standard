# RDP: Rishika's Data Protection Standard for Python

This is a collection of general purpose data protection scripts for Python used by [Rishika Mohanta](https://neurorishika.github.io) for protecting data in her research. It is based on AES-128 (Fernet) encryption and decryption. It is a wrapper around the [cryptography](https://cryptography.io/en/latest/) library.

## Usage

`rdp_gen.py` can be used to generate a new `key.key` file for use in projects. This key is used to encrypt and decrypt data. The generated key will have to be placed in the same directory as the project using the RDP encryption standard.

`*.ezip` files are encrypted zip files used to store data under the RDP standard. The `rdp_client.py` module includes the following functions for use in projects:

- `rdp_client.unlock_and_unzip_file(data2unzip, key_dir='key.key',multifile=False)` which takes in a `*.ezip` file and returns the unzipped data in the same directory as the `*.ezip` file. It can also be used to unzip multiple split and encrypted ezip files at once if `multifile=True`. Target the data to the first in the series of split files i.e. `<name>.ezip.000` and the function will automatically unzip all the files in the series.

- `rdp_client.zip_and_lock_file(data2zip, key_dir='key.key',multifile=False,split_size_bytes=50_000_000)` which takes in data and returns a `*.ezip` file in the same directory as the data. `multifile` and `split_size_bytes` can be used to split the data into multiple files if the data is too large to be stored in a single file. The default split size is 50MB. The value should be less than 100MB i.e. the maximum size of a single file on GitHub and be define in bytes.

## Installation (standalone)

Make sure you have python >=3.9 and cryptography installed. If not, run `pip install cryptography` in your terminal.

Place the `rdp_client.py` in the same directory as the project using the RDP standard. The `key.key` file for that project should also be placed in the same directory. The `rdp_gen.py` file can be used to generate a new `key.key` file.

Finally, add the following lines to your `.gitignore` file:

```
# key files anywhere in the project directory and subfolders
*.key
# data files anywhere in the project directory and subfolders
**/data/*/
# unprotected zip files anywhere in the project directory and subfolders
**/*.zip
```

## Installation (for Rishika's PyProject Templates)

`rdp_client.py` is built into the [Rishika Python Project Template]() however the `key.key` file is not. Generate a new `key.key` file using `rdp_gen.py` and place it in the same directory as the project using the RDP standard. The `rdp_gen.py` file can be used to generate a new `key.key` file.

To access the module inside the template, make sure the package has been built. After that
use:

- `<package-name>.rdp_client.unlock_and_unzip_file(data2unzip, key_dir='key.key',multifile=False)` which takes in a `*.ezip` file and returns the unzipped data in the same directory as the `*.ezip` file. It can also be used to unzip multiple split and encrypted ezip files at once if `multifile=True`. Target the data to the first in the series of split files i.e. `<name>.ezip.000` and the function will automatically unzip all the files in the series.

- `<package-name>.rdp_client.zip_and_lock_file(data2zip, key_dir='key.key',multifile=False,split_size_bytes=50_000_000)` which takes in data and returns a `*.ezip` file in the same directory as the data. `multifile` and `split_size_bytes` can be used to split the data into multiple files if the data is too large to be stored in a single file. The default split size is 50MB. The value should be less than 100MB i.e. the maximum size of a single file on GitHub and be define in bytes.


Alternatively, you can run the `rdp_client.py` file directly from the terminal using `poetry run python <package-name>/rdp_client.py`. Use `--help` to see the available options.
