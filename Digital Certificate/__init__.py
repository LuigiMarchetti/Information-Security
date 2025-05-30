from __future__ import print_function
from cryptography import x509
from cryptography.hazmat.backends import default_backend

import jks


def read_keystore():
    ks = jks.KeyStore.load('keystore', '123')


    for alias, c in ks.certs.items():
        print("Certificate: " + c.alias)

        cert = x509.load_der_x509_certificate(c.cert, default_backend())

        # a) Owner (subject)
        print("a) Proprietário:", cert.subject.rfc4514_string())

        # b) Issuer
        print("b) Emissor:", cert.issuer.rfc4514_string())

        # c) Self-signed check
        is_self_signed = cert.subject == cert.issuer
        print("c) É autoassinado?", "Sim" if is_self_signed else "Não")

        # d) Validity
        print("d) Válido de:", cert.not_valid_before)
        print("   Até:", cert.not_valid_after)
        print("\n\n")

#read_keystore()


import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import hashes



def cipher_image(key, image):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = pad(image, AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(cipher.iv + encrypted)


with open("./files/imagemparacifrar.jpg", "rb") as f:
    image_data = f.read()
key = b"AAAAAAAAAAAAAAAA"

image_ciphered = cipher_image(key, image_data)
with open("./files/my_image_encrypted.bin", "wb") as f:
    f.write(image_ciphered)

ks = jks.KeyStore.load('keystore', '123')

alias, c = list(ks.certs.items())[1] # 1 == furb
print("Certificate: " + c.alias)
cert = x509.load_der_x509_certificate(c.cert, default_backend())
public_key_furb = cert.public_key()

key_encrypted = public_key_furb.encrypt(
    key,
    asymmetric_padding.OAEP(
        mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
with open("./key.aes.bin", "wb") as f:
    f.write(key_encrypted)