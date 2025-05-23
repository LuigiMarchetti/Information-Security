from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def create_and_save_keys():
    # Gera um par de chaves RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("private_key.pem", "wb") as f:
        f.write(pem_private_key)
    
    # Retorna a chave pública em formato PEM
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1,
    )
    with open("public_key.pem", "wb") as f:
        f.write(public_pem)

#create_and_save_keys()

def create_and_save_message():
    message = b"Hey Martin my friend!"
    with open("./new_martin_public_key.pem", "rb") as file:
        martin_public_key = serialization.load_pem_public_key(
            file.read(),
            backend=default_backend()
        )
        encrypted = martin_public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            ))
        with open("new_file_to_martin.bin", "wb") as f:
            f.write(encrypted)


#create_and_save_message()

def read_and_show_message():
    with open("file_from_martin.bin", "rb") as f:
        file_from_martin = f.read()

        with open("private_key.pem", "rb") as file:
            my_private_key = serialization.load_pem_private_key(
                file.read(),
                password=None,
                backend=default_backend()
            )
        message_decrypted = my_private_key.decrypt(
            file_from_martin,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    print("Decrypted message:", message_decrypted.decode('utf-8'))

#read_and_show_message()

def read_and_crypt_pdf():
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
        with open("L09 - Chave assimétrica.pdf", "rb") as file:
            pdf = file.read()
            encrypted = public_key.encrypt(
                pdf,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                ))
            with open("pdf_decrypted.bin", "wb") as f:
                f.write(encrypted)
#read_and_crypt_pdf()
# R: Algoritmos de chave assimétrica, como RSA, só podem criptografar dados com tamanho menor ou igual ao tamanho da chave (em bytes), menos alguns bytes para padding.
# Um arquivo PDF é muito maior que isso, o que excede a capacidade do algoritmo.
# Deve ser usada uma criptografia híbrida (RSA + AES) para resolver o problema.


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding

import os

def read_and_crypt_jpg():
    aes_key = os.urandom(32)
    with open("./new_martin_public_key.pem", "rb") as file:
        martin_public_key = serialization.load_pem_public_key(
            file.read(),
            backend=default_backend()
        )
        encrypted = martin_public_key.encrypt(
            aes_key,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            ))
        with open("./imgs/encrypted_aes_key_to_martin.bin", "wb") as f:
            f.write(encrypted)
        with open("./imgs/my_image.jpg", "rb") as f:
            cipher = Cipher(algorithms.AES(aes_key), modes.ECB())
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(128).padder()


            image_data = f.read()
            padded_data = padder.update(image_data) + padder.finalize()

            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

            with open("./imgs/encrypted_ecb_image_to_martin.bin", "wb") as f:
                f.write(encrypted_data)

#read_and_crypt_jpg()

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, hashes, padding as symmetric_padding
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.backends import default_backend

def read_and_uncrypt_png():
    try:
        # Carrega chave privada
        with open("private_key.pem", "rb") as f:
            my_private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

        # Lê chave AES cifrada e decifra
        with open("./imgs-received/chave_aes_cifrada.bin", "rb") as f:
            aes_ciphered_key = f.read()
        aes_deciphered_key = my_private_key.decrypt(
            aes_ciphered_key,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Lê dados cifrados
        with open("./imgs-received/imagem_cifrada.bin", "rb") as f:
            ciphered_data = f.read()

        # Decifra com AES ECB
        cipher = Cipher(algorithms.AES(aes_deciphered_key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphered_data) + decryptor.finalize()

        # Remove padding PKCS7 (128 bits = 16 bytes)
        unpadder = symmetric_padding.PKCS7(128).unpadder()
        image_data = unpadder.update(padded_data) + unpadder.finalize()

        # Salva imagem decifrada
        with open("./imgs-received/image_received_decrypted.png", "wb") as f:
            f.write(image_data)

        print("Imagem decifrada com sucesso!")

    except Exception as e:
        print("Erro durante a decifragem:", e)

read_and_uncrypt_png()